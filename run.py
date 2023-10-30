# 80 characters wide and 24 rows high max

import random


def home():
    """
    Displays home screen and user prompt for leaderboard, rules or game.
    """
    print('ASCII art goes here')

    while True:
        try:
            home_choice = input(
                "Type 'l' for leaderboard, 'r' for rules, or 'p' to play.\n"
                "Your choice: ")
            if home_choice not in ['l', 'r', 'p']:
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')
    return home_choice


def leaderboard():
    """
    Generates a leaderboard from Google Sheet.
    """
    print('Leaderboard (top 10) to go here')


def rules():
    """
    Displays rules. Clear screen method used to move to next page.
    """
    print('Rules to go here...')


def roll_one():
    """
    Generates a list of five random integers between 1 and 6 to represent die
    face values
    """
    result_one = []
    for die in range(5):
        die = random.randint(1, 6)
        result_one.append(die)
    return result_one


def user_prompt(dice):
    """
    Prints the current roll and prompts user to re-roll, submit or exit.
    """
    while True:
        try:
            game_choice = input(
                f'After your first roll, your dice are: {dice}\n'
                "Type 'r' to re-roll some or all dice, 's' to submit score to"
                " scoreboard, or 'e' to exit home.\n"
                "Your choice: ")
            if game_choice not in ['r', 's', 'e']:
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')
    return game_choice


def keep_choice(dice):
    """Takes dice arg from previous roll and prompts the user to input which
    dice should be kept. Returns a list of integers to retain.
    """
    # Prompt the user to input which dice to keep.
    while True:
        try:
            dice_to_keep = input(
                'Which dice do you want to keep? (Enter the '
                'indices, separated by spaces): ')

            # Split the input string into a list of integers.
            dice_to_keep = [int(i) for i in dice_to_keep.split()]

            # Validate the input.
            for i in dice_to_keep:
                if i < 0 or i >= len(dice):
                    raise ValueError('Invalid index.')

            # Break out of the loop if the input is valid.
            break
        except ValueError:
            print('Invalid input. Please try again.')

    return dice_to_keep


def keep_and_reroll(dice, keep):
    """
    Takes dice arg from previous roll and re-rolls dice which aren't in keep
    list selected by user.
    Returns an updated list of dice values.
    """

    # Create a copy of the dice list.
    new_dice = dice[:]

    # Re-roll the dice that are not being kept.
    for die in range(len(dice)):
        if die not in keep:
            new_dice[die] = random.randint(1, 6)

    return new_dice


def submit(dice):
    """
    Evaluates score and adds to scoreboard once user selects box.
    """
    print('Scoreboard updates...')


# Main code block
home_choice = home()
if home_choice == 'l':
    leaderboard()
elif home_choice == 'r':
    rules()
else:
    name = input('Please enter your name: ')
    print(f"{name}, let's play Yahtzee!\n")

dice = roll_one()
game_choice = user_prompt(dice)

if game_choice == 'e':
    home()
elif game_choice == 's':
    submit(dice)
else:
    keep = keep_choice(dice)
    new_dice = keep_and_reroll(dice, keep)
    print(f'Your updated roll is {new_dice}. You have one roll remaining.')