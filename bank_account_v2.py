"""Расширенный модуль с классом BankAccount и Bank."""

from datetime import datetime
from typing import Optional, List


class BankAccount:
    """Класс банковского счёта с историей операций."""
    
    _all_accounts: List['BankAccount'] = []  # Список всех счетов
    
    def __init__(self, owner_name: str, initial_balance: float = 0):
        """Инициализация счёта."""
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = len(BankAccount._all_accounts) + 1
        self._history: List[str] = []  # История операций
        
        # Добавляем счёт в общее хранилище
        BankAccount._all_accounts.append(self)
        
        # Записываем начальную операцию
        self._add_to_history(f"Счёт открыт. Начальный баланс: {initial_balance}")
    
    def _add_to_history(self, operation: str) -> None:
        """Добавляет запись в историю операций с временной меткой."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._history.append(f"[{timestamp}] {operation}")
    
    def get_history(self) -> List[str]:
        """Возвращает историю операций счёта."""
        return self._history.copy()
    
    def print_history(self) -> None:
        """Выводит историю операций."""
        print(f"\n=== История операций счёта #{self.account_number} ===")
        if not self._history:
            print("История пуста")
        else:
            for record in self._history:
                print(record)
        print("=" * 45)
    
    def deposit(self, amount: float) -> bool:
        """Пополнение баланса (макс. 50000)."""
        if amount > 50000:
            print(f"Ошибка: максимальная сумма пополнения 50000. Вы ввели {amount}")
            return False
        if amount <= 0:
            print("Ошибка: сумма пополнения должна быть положительной")
            return False
        self.balance += amount
        self._add_to_history(f"Пополнение на {amount}. Баланс: {self.balance}")
        print(f"Пополнение на {amount}. Баланс: {self.balance}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Снятие денег (макс. 50000, достаточно средств)."""
        if amount > 50000:
            print(f"Ошибка: максимальная сумма снятия 50000. Вы ввели {amount}")
            return False
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной")
            return False
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств. Доступно: {self.balance}")
            return False
        self.balance -= amount
        self._add_to_history(f"Снятие {amount}. Баланс: {self.balance}")
        print(f"Снятие {amount}. Баланс: {self.balance}")
        return True
    
    def get_owner_info(self) -> str:
        """Получение информации о владельце."""
        return f"Владелец: {self.owner_name}, Счёт: {self.account_number}, Баланс: {self.balance}"
    
    def transfer_to(self, target_account: 'BankAccount', amount: float) -> bool:
        """Перевод средств на другой счёт (макс. 20000)."""
        if amount > 20000:
            print(f"Ошибка: максимальная сумма перевода 20000. Вы ввели {amount}")
            return False
        if amount <= 0:
            print("Ошибка: сумма перевода должна быть положительной")
            return False
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств для перевода. Доступно: {self.balance}")
            return False
        
        self.balance -= amount
        target_account.balance += amount
        
        # Записываем в историю обоих счетов
        self._add_to_history(f"Перевод {amount} на счёт #{target_account.account_number} ({target_account.owner_name}). Баланс: {self.balance}")
        target_account._add_to_history(f"Перевод {amount} со счёта #{self.account_number} ({self.owner_name}). Баланс: {target_account.balance}")
        
        print(f"Перевод {amount} со счёта {self.account_number} на счёт {target_account.account_number}")
        print(f"Ваш баланс: {self.balance}")
        return True
    
    def get_account_info(self) -> str:
        """Получение информации о счёте."""
        return f"Счёт #{self.account_number}: {self.owner_name}, баланс: {self.balance}"
    
    @classmethod
    def get_all_accounts(cls) -> List['BankAccount']:
        """Получить список всех счетов."""
        return cls._all_accounts.copy()
    
    @classmethod
    def print_all_accounts(cls) -> None:
        """Вывести список всех счетов."""
        if not cls._all_accounts:
            print("Счета отсутствуют")
            return
        print("\n=== Список всех счетов ===")
        for account in cls._all_accounts:
            print(account.get_account_info())
        print("==========================\n")
    
    @classmethod
    def find_account(cls, account_number: int) -> Optional['BankAccount']:
        """Найти счёт по номеру."""
        for account in cls._all_accounts:
            if account.account_number == account_number:
                return account
        return None


class Bank:
    """Класс банка для управления счетами и переводами."""
    
    @staticmethod
    def transfer(from_account_number: int, to_account_number: int, amount: float) -> bool:
        """Перевод между счетами через банк."""
        from_account = BankAccount.find_account(from_account_number)
        to_account = BankAccount.find_account(to_account_number)
        
        if from_account is None:
            print(f"Ошибка: счёт #{from_account_number} не найден")
            return False
        if to_account is None:
            print(f"Ошибка: счёт #{to_account_number} не найден")
            return False
        
        print(f"\n--- Перевод через банк ---")
        print(f"Отправитель: {from_account.get_account_info()}")
        print(f"Получатель: {to_account.get_account_info()}")
        
        return from_account.transfer_to(to_account, amount)
    
    @staticmethod
    def print_all_accounts_info() -> None:
        """Вывести информацию о всех счетах."""
        BankAccount.print_all_accounts()
    
    @staticmethod
    def get_account_history(account_number: int) -> Optional[List[str]]:
        """Получить историю операций счёта по номеру."""
        account = BankAccount.find_account(account_number)
        if account is None:
            print(f"Ошибка: счёт #{account_number} не найден")
            return None
        return account.get_history()
