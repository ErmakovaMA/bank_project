"""Тестирование банковских счетов."""
from bank_account import BankAccount

def main():
    # Создаём счета
    print("=== Создание счетов ===")
    acc1 = BankAccount("Иванов Иван Иванович", 100000)
    acc2 = BankAccount("Петрова Мария Сергеевна", 50000)
    acc3 = BankAccount("Сидоров Алексей Владимирович", 30000)
    
    # Выводим информацию о владельцах
    print("\n=== Информация о владельцах ===")
    print(acc1.get_owner_info())
    print(acc2.get_owner_info())
    print(acc3.get_owner_info())
    
    # Пополнение
    print("\n=== Пополнение ===")
    acc1.deposit(25000)
    acc2.deposit(10000)
    
    # Снятие
    print("\n=== Снятие ===")
    acc1.withdraw(15000)
    acc2.withdraw(60000)  # Должно выдать ошибку (недостаточно средств)
    acc3.withdraw(5000)
    
    # Перевод
    print("\n=== Перевод ===")
    acc1.transfer(acc2, 10000)
    acc3.transfer(acc1, 20000)
    
    # Информация о счетах
    print("\n=== Информация о счетах ===")
    print(acc1.get_account_info())
    print(acc2.get_account_info())
    print(acc3.get_account_info())
    
    # Список всех счетов
    BankAccount.print_all_accounts()

if __name__ == "__main__":
    main()
