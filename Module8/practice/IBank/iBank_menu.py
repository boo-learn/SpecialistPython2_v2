import pickle
import iBank_template as iBank

EMPLOYEE_PASSWORD = "123"


def close_account():
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    print("Укажите паспорт")
    passport = int(input(':'))
    acc = 0
    is_found = False
    for account in accounts:
        if account.passport8 == passport:
            acc = account
            is_found = True
            break
    if not is_found:
        raise ValueError('Аккаунта с данным паспортом не существует')
    if type(acc) is iBank.Account:
        iBank.Account.account_close(acc)
    if type(acc) is iBank.CreditAccount:
        iBank.CreditAccount.account_close(acc)


def view_accounts_list():
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    if len(accounts) == 0:
        raise ValueError('Список клиентов пуст')
    for i, account in enumerate(accounts, 1):
        if type(account) is iBank.Account:
            try:
                info = iBank.Account.full_info(account)
            except ValueError as e:
                info = e
        if type(account) is iBank.CreditAccount:
            try:
                info = iBank.CreditAccount.full_info(account)
            except ValueError as e:
                info = e
        print(f'{i}. {info}')


def view_account_by_passport():
    print("Укажите паспорт")
    passport = int(input(':'))
    for account in accounts:
        if account.passport8 == passport:
            if account.is_archived:
                raise ValueError('Аккаунт закрыт')
            view_client_account(account)
            print('**** История операций клиента ****')
            view_history(account)
            return
    raise ValueError('Аккаунта с данным паспортом не существует')


def view_client_account(account):
    """
    Узнать состояние своего счета
    """
    if type(account) is iBank.Account:
        print(iBank.Account.full_info(account))
    if type(account) is iBank.CreditAccount:
        print(iBank.CreditAccount.full_info(account))


def put_account(account):
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    print("Укажите сумму")
    amount = int(input(':'))
    if amount <= 0:
        raise ValueError('Сумма должна быть больше 0')
    if type(account) is iBank.Account:
        iBank.Account.deposit(account, amount)
    if type(account) is iBank.CreditAccount:
        iBank.CreditAccount.deposit(account, amount)


def withdraw(account):
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    print("Укажите сумму")
    amount = int(input(':'))
    if amount <= 0:
        raise ValueError('Сумма должна быть больше 0')
    if type(account) is iBank.Account:
        iBank.Account.withdraw(account, amount)
    if type(account) is iBank.CreditAccount:
        iBank.CreditAccount.withdraw(account, amount)


def transfer(account):
    """
    Перевести на счет другого клиента по номеру телефона
    """
    print("Укажите телефон другого клиента")
    phone = input(':')
    for acc in accounts:
        if acc.phone_number == phone:
            if acc.is_archived:
                raise ValueError('Аккаунт, на который вы пытаетесь перевести деньги, закрыт')
            print("Укажите сумму")
            amount = int(input(':'))
            if amount <= 0:
                raise ValueError('Сумма должна быть больше 0')
            if type(account) is iBank.Account:
                iBank.Account.transfer(account, acc, amount)
            if type(account) is iBank.CreditAccount:
                iBank.CreditAccount.transfer(account, acc, amount)
            return
    raise ValueError('Аккаунта с данным телефоном не существует')


def create_new_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    new_acc = iBank.Account(name, passport, phone_number)
    for account in accounts:
        if account.passport8 == new_acc.passport8 or account.phone_number == new_acc.phone_number:
            raise ValueError('Аккаунт с данным паспортом либо телефоном уже существует')
    accounts.append(new_acc)


def create_new_credit_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    negative_limit = int(input("Лимит (сумма со знаком '-'): "))
    new_acc = iBank.CreditAccount(name, passport, phone_number, negative_limit=negative_limit)
    for account in accounts:
        if account.passport8 == new_acc.passport8 or account.phone_number == new_acc.phone_number:
            raise ValueError('Аккаунт с данным паспортом либо телефоном уже существует')
    accounts.append(new_acc)


def view_history(account):
    res_str = ''
    if type(account) is iBank.Account:
        res_str = iBank.Account.show_history(account)
    if type(account) is iBank.CreditAccount:
        res_str = iBank.CreditAccount.show_history(account)
    if res_str:
        print(res_str)
    else:
        print('История пуста')


def reopen_account():
    print("Укажите паспорт")
    passport = int(input(':'))
    acc = 0
    is_found = False
    for account in accounts:
        if account.passport8 == passport:
            acc = account
            is_found = True
            break
    if not is_found:
        raise ValueError('Аккаунта с данным паспортом не существует')
    if type(acc) is iBank.Account:
        iBank.Account.account_reopen(acc)
    if type(acc) is iBank.CreditAccount:
        iBank.CreditAccount.account_reopen(acc)


def client_menu(account):
    while True:
        print(f"***********Меню клиента {account.name} *************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Посмотреть историю операций")
        print("6. Exit")
        choice = input(":")
        if choice == "1":
            try:
                view_client_account(account)
            except ValueError as e:
                print(e)
        elif choice == "2":
            try:
                put_account(account)
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                withdraw(account)
            except ValueError as e:
                print(e)
        elif choice == "4":
            try:
                transfer(account)
            except ValueError as e:
                print(e)
        elif choice == "5":
            try:
                view_history(account)
            except ValueError as e:
                print(e)
        elif choice == "6":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Создать новый кредитный счет")
        print("3. Закрыть счет")
        print("4. Переоткрыть счет")
        print("5. Посмотреть список счетов")
        print("6. Посмотреть счет по номеру паспорта")
        print("7. Exit")
        choice = input(":")
        if choice == "1":
            try:
                create_new_account()
            except ValueError as e:
                print(e)
        if choice == "2":
            try:
                create_new_credit_account()
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                close_account()
            except ValueError as e:
                print(e)
        elif choice == "4":
            try:
                reopen_account()
            except ValueError as e:
                print(e)
        elif choice == "5":
            try:
                view_accounts_list()
            except ValueError as e:
                print(e)
        elif choice == "6":
            try:
                view_account_by_passport()
            except ValueError as e:
                print(e)
        elif choice == "7":
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
            if account.is_archived:
                raise ValueError('Аккаунт закрыт')
            return account

    return False


def start_menu():
    try:
        with open('clients.pickle', 'rb') as f_in:
            global accounts
            accounts = pickle.load(f_in)
    except FileNotFoundError as e:
        pass
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            with open('clients.pickle', 'wb') as f_out:
                pickle.dump(accounts, f_out)
            break
        elif choice == "1":
            if employee_access():
                employee_menu()
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = None
            try:
                account = client_access(accounts)
            except ValueError as e:
                print(e)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий паспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


if __name__ == "__main__":
    accounts = []
    start_menu()
