"""Модуль с классом BankAccount."""

class BankAccount:
    """Класс банковского счёта."""
    
    _all_accounts = []  # Список всех счетов
    
    def __init__(self, owner_name: str, initial_balance: float = 0):
        """Инициализация счёта."""
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = len(BankAccount._all_accounts) + 1
        BankAccount._all_accounts.append(self)
    
    def deposit(self, amount: float) -> None:
        """Пополнение баланса (макс. 50000)."""
        if amount > 50000:
            print(f"Ошибка: максимальная сумма пополнения 50000. Вы ввели {amount}")
            return
        if amount <= 0:
            print("Ошибка: сумма пополнения должна быть положительной")
            return
        self.balance += amount
        print(f"Пополнение на {amount}. Баланс: {self.balance}")
    
    def withdraw(self, amount: float) -> None:
        """Снятие денег (макс. 50000, достаточно средств)."""
        if amount > 50000:
            print(f"Ошибка: максимальная сумма снятия 50000. Вы ввели {amount}")
            return
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной")
            return
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств. Доступно: {self.balance}")
            return
        self.balance -= amount
        print(f"Снятие {amount}. Баланс: {self.balance}")
    
    def get_owner_info(self) -> str:
        """Получение информации о владельце."""
        return f"Владелец: {self.owner_name}, Счёт: {self.account_number}, Баланс: {self.balance}"
    
    def transfer(self, target_account: 'BankAccount', amount: float) -> None:
        """Перевод средств на другой счёт (макс. 20000)."""
        if amount > 20000:
            print(f"Ошибка: максимальная сумма перевода 20000. Вы ввели {amount}")
            return
        if amount <= 0:
            print("Ошибка: сумма перевода должна быть положительной")
            return
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств для перевода. Доступно: {self.balance}")
            return
        self.balance -= amount
        target_account.balance += amount
        print(f"Перевод {amount} со счёта {self.account_number} на счёт {target_account.account_number}")
        print(f"Ваш баланс: {self.balance}")
    
    def get_account_info(self) -> str:
        """Получение информации о счёте."""
        return f"Счёт #{self.account_number}: {self.owner_name}, баланс: {self.balance}"
    
    @classmethod
    def get_all_accounts(cls) -> list:
        """Получить список всех счетов."""
        return cls._all_accounts
    
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
