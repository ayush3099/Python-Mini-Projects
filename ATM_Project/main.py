from services.operations import *
from utils.helper import print_line

while True:

    print_line()

    print("ATM MENU")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    print_line()

    choice = input("Enter choice: ")

    if choice == "1":

        display_balance()

    elif choice == "2":

        amt = int(input("Enter amount: "))

        deposit_money(amt)

    elif choice == "3":

        amt = int(input("Enter amount: "))

        withdraw_money(amt)

    elif choice == "4":

        show_statement()

    elif choice == "5":

        print("Thank you for using ATM")

        break

    else:

        print("Invalid Choice")