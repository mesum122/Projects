"""Account creation: Name, account number, initial deposit amount"""


def create_account(name, number, initial_balance):
    return {'account_number': number,
            "account_name": name,
            "balance": initial_balance,
            "transaction_history": []
            }


"""deposit money in account and update balance"""


def deposit(account, amount):
    account["balance"] = account["balance"] + amount
    account["transaction_history"].append(f"you deposited ${amount}")


"""Implement a method withdraw money , if sufficient funds. also update balance """


def withdrawal(account, amount):
    account["balance"] = account["balance"] - amount
    account['transaction_history'].append(f"you withdrew ${amount}")


def inquiry(account):
    for key, value in account.items():
        if key == "balance":
            print(key, value)
        else:
            pass


def transaction_history(account):
    print(account["transaction_history"])


def info(account):
    for key, value in account.items():
        if key == "transaction_history":
            pass
        else:
            print(f"{key} , {value}")


account = create_account("mesum", "123", 100)

deposit(account, 100)
withdrawal(account, 50)
inquiry(account)
transaction_history(account)
info(account)
