import random

def play_game():

    options = ["stone", "paper", "scissors"]

    user_choice = input(
        "\nEnter stone / paper / scissors: "
    ).lower()

    if user_choice not in options:

        print("Invalid choice")

        return

    computer_choice = random.choice(options)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:

        print("Result: It's a Draw!")

    elif (
        (user_choice == "stone" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "stone") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):

        print("Result: You Win!")

    else:

        print("Result: Computer Wins!")