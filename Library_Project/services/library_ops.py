from datetime import datetime
from models import data


def show_books():

    print("\nAvailable Books:")

    for book_id, book in data.library_books.items():

        if book_id not in data.issued_books:

            print(book_id, "-", book)


def issue_book():

    show_books()

    book_id = int(input("\nEnter Book ID to Issue: "))

    if book_id in data.library_books:

        if book_id in data.issued_books:

            print("Book already issued")

            return

        student_name = input("Enter Student Name: ")

        days = int(input("Enter number of days to issue: "))

        issue_date = datetime.now()

        data.issued_books[book_id] = {

            "student": student_name,
            "issue_date": issue_date,
            "days": days
        }

        print("\nBook Issued Successfully")

        print("Return within", days, "days")

    else:

        print("Invalid Book ID")


def calculate_fine(extra_days):

    fine = 0

    # Weekly increasing fine logic

    for day in range(1, extra_days + 1):

        week = (day - 1) // 7 + 1

        fine += 10 * week

    return fine


def return_book():

    book_id = int(input("\nEnter Book ID to Return: "))

    if book_id in data.issued_books:

        issue_data = data.issued_books[book_id]

        issue_date = issue_data["issue_date"]

        allowed_days = issue_data["days"]

        today = datetime.now()

        used_days = (today - issue_date).days

        print("\nBook used for:", used_days, "days")

        if used_days > allowed_days:

            extra_days = used_days - allowed_days

            fine = calculate_fine(extra_days)

            print("Late Return!")

            print("Fine to Pay: ₹", fine)

        else:

            print("Returned on time")

        del data.issued_books[book_id]

        print("Book Returned Successfully")

    else:

        print("Book was not issued")