from .iBank import Account, CreditAccount


EMPLOYEE_PASSWORD = "123"

def close_account(accounts):
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    account = access_by_passport(accounts)
    if account:
        account.to_archive()


def view_accounts_list(accounts):
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    idx = 1
    for acc in accounts:
        if not acc.in_archive:
            print(idx, acc)
            idx += 1


def view_account_by_passport(accounts):
    account = access_by_passport(accounts)
    if account:
        archived = ('Нет', 'Да')[account.in_archive]
        print(account, 'Аккаунт в архиве:', archived)


def view_client_account(account):
    """
    Узнать состояние своего счета
    """
    print(account)


def put_account(account):
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    amount = int(input('Введите сумму: '))
    account.deposit(amount)


def withdraw(account):
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    amount = int(input('Введите сумму: '))
    try:
        account.withdraw(amount)
    except ValueError as e:
        print(e)


def transfer(account):
    """
    Перевести на счет другого клиента по номеру телефона
    """
    phone = input('Введите номер телефона клиента: ')
    target = None
    for acc in accounts:
        if phone == acc.phone_number:
            target = acc
    if not target:
        print('Введен несуществующий номер, повторите попытку')
    else:
        amount = int(input('Введите сумму: '))
        account.transfer(target, amount)


def create_new_account(accounts):
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    credit = input('Создать кредитный аккаунт (y/n)? ')
    if credit == 'y':
        limit = int(input('Введите доступный лимит: '))
        account = CreditAccount(name, passport, phone_number, negative_limit=abs(limit) * (-1))
    else:
        account = Account(name, passport, phone_number)
    accounts.append(account)


def client_menu(account):
    while True:
        print(f"***********Меню клиента {account.name}*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(": ")
        if choice == "1":
            view_client_account(account)
        elif choice == "2":
            put_account(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            transfer(account)
        elif choice == "5":
            return
    # input("Press Enter")


def employee_menu(accounts):
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account(accounts)
        elif choice == "2":
            close_account(accounts)
        elif choice == "3":
            view_accounts_list(accounts)
        elif choice == "4":
            view_account_by_passport(accounts)
        elif choice == "5":
            return


def employee_access():
    """
    Проверяет доступ сотрудника банка, запрашивая пароль
    """
    password = input("Пароль: ")
    if password == EMPLOYEE_PASSWORD:
        return True
    return False


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = input("Номер паспорта: ")
        int(passport)
    except ValueError:
        return False
    for account in accounts:
        if passport == account.passport8:
            return account

    return False


def access_by_passport(accounts):
    account = client_access(accounts)
    if account is False:
        print('Неверные паспортные данные, повторите попыту')
        return
    else:
        return account
        


def start_menu(accounts):
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            break
        elif choice == "1":
            if employee_access():
                employee_menu(accounts)
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = client_access(accounts)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий пасспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


if __name__ == "__main__":
    accounts = []
    start_menu(accounts)
