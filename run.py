# 80 characters wide and 24 rows high max

import random


def home():
    """
    Displays home screen and user prompt for leaderboard, rules or game.
    """
    print('ASCII art goes here')

    home_choice = input(
        "Type 'l' for leaderboard, 'r' for rules, or 'p' to play.\n"
        "Your choice: ")

    while True:
        try:
            if home_choice not in ['l', 'r', 'p']:
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')

    if home_choice == 'l':
        leaderboard()
    elif home_choice == 'r':
        rules()
    else:
        name = input('Please enter your name: ')
        print(f"{name}, let's play Yahtzee!\n")
        roll = 0
        roll_one(roll)


def leaderboard():
    """
    Generates a leaderboard from Google Sheet.
    """
    print('Leaderboard (top 10) to go here')
    leaderboard_input = input('Press Enter to return Home')

    while True:
        try:
            if leaderboard_input != "":
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')
    home()


def rules():
    """
    Displays rules. Clear screen method used to move to next page.
    """
    print('Rules to go here...')
    rules_input = input('Press Enter to return Home')
    while True:
        try:
            if rules_input != "":
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')
    home()


def roll_one(roll):
    """
    Generates a list of five random integers between 1 and 6 to represent die
    face values
    """
    dice = []
    for die in range(5):
        die = random.randint(1, 6)
        dice.append(die)

    user_prompt(dice, roll)


def user_prompt(dice, roll):
    """
    Prints the current roll and prompts user to re-roll, submit or exit.
    """
    roll += 1
    remain = 3-roll
    
    # Check if the user has taken 3 rolls.
    if roll >= 3:
        print(f'You have taken 3 rolls and your dice are: {dice}\n'
        'Time to submit your score!')
        submit(dice)
    
    while True:
        try:
            game_choice = input(
                f'After roll {roll}, you have {remain} more remaining.\n'
                f'Your dice are: {dice}\n'
                "Type 'r' to re-roll some or all dice, 's' to submit score to"
                " scoreboard, or 'e' to exit home.\n"
                "Your choice: ")
            if game_choice not in ['r', 's', 'e']:
                raise ValueError('Invalid choice')
            break
        except ValueError:
            print('Invalid input. Please try again.')

    if game_choice == 'e':
        home()
    elif game_choice == 's':
        submit(dice)
    else:
        keep_choice(dice, roll)


def keep_choice(dice, roll):
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

    keep_and_reroll(dice, roll, dice_to_keep)


def keep_and_reroll(dice, roll, dice_to_keep):
    """
    Takes dice arg from previous roll and re-rolls dice which aren't in keep
    list selected by user.
    Returns an updated list of dice values.
    """

    # Create a copy of the dice list.
    # new_dice = dice[:]
    dice = dice[:]

    # Re-roll the dice that are not being kept.
    for die in range(len(dice)):
        if die not in dice_to_keep:
            dice[die] = random.randint(1, 6)

    user_prompt(dice, roll)


def submit(dice):
    """
    Evaluates score and adds to scoreboard once user selects box.
    """
    print('User selects which field of Scoreboard to use.')
    
    # Reset dice values before reroll
    dice = 0
    roll_one()


# Main code block
home()
