from services.game_logic import play_game
from utils.helper import print_line


while True:

    print_line()

    print("STONE PAPER SCISSORS GAME")

    print("1. Play Game")

    print("2. Exit")

    print_line()

    choice = input("Enter your choice: ")

    if choice == "1":

        play_game()

    elif choice == "2":

        print("Thank you for playing")

        break

    else:

        print("Invalid choice")