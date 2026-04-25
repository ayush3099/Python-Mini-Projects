from services.library_ops import *
from utils.helper import print_line


while True:

    print_line()

    print("LIBRARY MANAGEMENT SYSTEM")

    print("1. Show Available Books")

    print("2. Issue Book")

    print("3. Return Book")

    print("4. Exit")

    print_line()

    choice = input("Enter your choice: ")

    if choice == "1":

        show_books()

    elif choice == "2":

        issue_book()

    elif choice == "3":

        return_book()

    elif choice == "4":

        print("Thank you for using Library System")

        break

    else:

        print("Invalid Choice")