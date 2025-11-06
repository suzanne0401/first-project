import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Game!")

    while True:
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"You rolled a {roll}!")

        play_again = input("Roll again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play_game()
