from models import data

def display_balance():
    print("\nCurrent Balance:", data.balance)


def deposit_money(amount):

    data.balance += amount

    data.transactions.append(
        "Deposited ₹" + str(amount)
    )

    print("Amount Deposited Successfully")


def withdraw_money(amount):

    if amount > data.balance:

        print("Insufficient Balance")

    else:

        data.balance -= amount

        data.transactions.append(
            "Withdrawn ₹" + str(amount)
        )

        print("Amount Withdrawn Successfully")


def show_statement():

    print("\nTransaction History:")

    if len(data.transactions) == 0:

        print("No Transactions Yet")

    else:

        for t in data.transactions:

            print(t)