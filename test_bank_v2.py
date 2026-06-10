"""Тестирование расширенного банковского приложения."""
from bank_account_v2 import BankAccount, Bank


def main():
    print("=" * 60)
    print("СОЗДАНИЕ СЧЕТОВ")
    print("=" * 60)
    
    # Создаём счета
    acc1 = BankAccount("Иванов Иван Иванович", 100000)
    acc2 = BankAccount("Петрова Мария Сергеевна", 50000)
    acc3 = BankAccount("Сидоров Алексей Владимирович", 30000)
    
    # Выводим информацию о владельцах
    print("\n=== Информация о владельцах ===")
    print(acc1.get_owner_info())
    print(acc2.get_owner_info())
    print(acc3.get_owner_info())
    
    # Пополнение
    print("\n" + "=" * 60)
    print("ОПЕРАЦИИ ПОПОЛНЕНИЯ")
    print("=" * 60)
    acc1.deposit(25000)
    acc2.deposit(10000)
    
    # Снятие
    print("\n" + "=" * 60)
    print("ОПЕРАЦИИ СНЯТИЯ")
    print("=" * 60)
    acc1.withdraw(15000)
    acc2.withdraw(60000)  # Должно выдать ошибку
    acc3.withdraw(5000)
    
    # Перевод между счетами
    print("\n" + "=" * 60)
    print("ПЕРЕВОД МЕЖДУ СЧЕТАМИ")
    print("=" * 60)
    acc1.transfer_to(acc2, 10000)
    acc3.transfer_to(acc1, 20000)
    
    # Вывод информации о счетах
    print("\n" + "=" * 60)
    print("ТЕКУЩЕЕ СОСТОЯНИЕ СЧЕТОВ")
    print("=" * 60)
    Bank.print_all_accounts_info()
    
    # Поиск счёта по номеру
    print("\n" + "=" * 60)
    print("ПОИСК СЧЁТА ПО НОМЕРУ")
    print("=" * 60)
    found = BankAccount.find_account(2)
    if found:
        print(f"Найден: {found.get_account_info()}")
    
    # Перевод через банк
    print("\n" + "=" * 60)
    print("ПЕРЕВОД ЧЕРЕЗ БАНК")
    print("=" * 60)
    Bank.transfer(1, 3, 5000)
    
    # Финальное состояние счетов
    print("\n" + "=" * 60)
    print("ФИНАЛЬНОЕ СОСТОЯНИЕ СЧЕТОВ")
    print("=" * 60)
    Bank.print_all_accounts_info()
    
    # История операций
    print("\n" + "=" * 60)
    print("ИСТОРИЯ ОПЕРАЦИЙ")
    print("=" * 60)
    acc1.print_history()
    acc2.print_history()
    acc3.print_history()


if __name__ == "__main__":
    main()
