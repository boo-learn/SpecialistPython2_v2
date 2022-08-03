from IBank_part5 import Account, CreditAccount

EMPLOYEE_PASSWORD = "123"


def close_account():
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    pass


def view_accounts_list():
    """
        Отображение всех клиентов банка в виде нумерованного списка
        """


def view_account_by_passport():
    pass


def view_client_account():
    """
    Узнать состояние своего счета
    """
    pass


def put_account():
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    pass


def withdraw():
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    pass


def transfer():
    """
    Перевести на счет другого клиента по номеру телефона
    """
    pass


def create_new_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    # TODO: тут создаем новый аккаунт пользователя account = ...
    #   и добавляем его в accounts.append(account)


def client_menu(account):
    while True:
        print("***********Меню клиента <Иванов И.И.>*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account()
        elif choice == "2":
            put_account()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            close_account()
        elif choice == "3":
            view_accounts_list()
        elif choice == "4":
            view_account_by_passport()
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
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    for account in accounts:
        if passport == account.passport8:
            return account

    return False


def start_menu():
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
                employee_menu()
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
    start_menu()
