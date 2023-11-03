# 80 characters wide and 24 rows high max
# Imports used to generate dice rolls and for clear_display()
import random
import os


def clear_display():
    '''Clears the display'''
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def home():
    '''Displays home screen and user prompt for leaderboard, rules or game.'''
    print('ASCII art goes here')
    # Loops until valid input given
    while True:
        home_choice = input(
            "Type 'l' for leaderboard, 'r' for rules, or 'p' to play.\n"
            "Your choice: ")
        home_choice = home_choice.lower()
        # Validates input and prompts until valid.
        if home_choice not in ['l', 'r', 'p']:
            print('Try again...\U0001F644')
        else:
            if home_choice == 'l':
                leaderboard()
            elif home_choice == 'r':
                rules()
            else:
                while True:
                    name = input('Please enter your name: ')
                    if name == "":
                        print('Try again...\U0001F644')
                    else:
                        name = name.capitalize()
                        input(f"OK {name}, let's play Yahtzee!\n"
                        'Hit Enter to roll dice...')
                        roll = 0
                        roll_one(roll)


def leaderboard():
    '''Generates a leaderboard from Google Sheet.'''
    print('Leaderboard (top 10) to go here')
    leaderboard_input = input('Press Enter to return Home')
    home()


def rules():
    '''Displays rules. Clear screen method used to move to next page.'''
    print('Rules to go here...')
    rules_input = input('Press Enter to return Home')
    home()


def roll_one(roll):
    """
    Generates a list of five random integers between 1 and 6 to represent die
    face values
    """
    clear_display()
    dice = []
    for die in range(5):
        die = random.randint(1, 6)
        dice.append(die)

    user_prompt(dice, roll)


def user_prompt(dice, roll):
    '''Prints the current roll and prompts user to re-roll, submit or exit.'''
    roll += 1
    remain = 3-roll

    # Check if the user has taken 3 rolls.
    if roll >= 3:
        print(f'You have taken 3 rolls and your dice are: {dice}\n'
              'Time to submit your score!')
        submit(dice, roll)
    # Advises user of dice and asks for valid unput
    print(f'After roll {roll}, you have {remain} more remaining.\n'
          f'Your dice are: {dice}\n'
            "Type 'r' to re-roll some or all dice, 's' to submit score to"
            " scoreboard, or 'e' to exit home.")
    while True:
        game_choice = input('Your choice:')
        game_choice = game_choice.lower()
        if game_choice not in ['r', 's', 'e']:
            print('Try again...\U0001F644')
        elif game_choice == 'e':
            home()
        elif game_choice == 's':
            submit(dice, roll)
        else:
            keep_choice(dice, roll)


def keep_choice(dice, roll):
    '''Takes dice and roll arg from previous roll and prompts the user to
    input which dice should be kept. Returns a list of integers to retain.'''

    print('Which dice do you want to keep? Enter numbers separated by spaces')
    # Prompt the user to input which dice to keep.
    while True:
        dice_to_keep = input('Your choice:')

        # Validate the input.
        try:
            dice_to_keep = [int(i) for i in dice_to_keep.split()]

            if not dice_to_keep:
                print('Try again...\U0001F644')
            elif any(die < 1 or die > 5 for die in dice_to_keep):
                print('Try again...\U0001F644')
            else:
                keep_and_reroll(dice, roll, dice_to_keep)
                break
        except ValueError:
            print('Try again...\U0001F644')


def keep_and_reroll(dice, roll, dice_to_keep):
    '''Takes dice arg from previous roll and re-rolls dice which aren't in
    keep list selected by user. Returns an updated list of dice values.'''
    clear_display()
    # Create a copy of the dice list.
    # new_dice = dice[:]
    dice = dice[:]

    # Re-roll the dice that are not being kept.
    for die in range(len(dice)):
        if die not in dice_to_keep:
            dice[die] = random.randint(1, 6)

    user_prompt(dice, roll)


def submit(dice, roll):
    '''
    Evaluates score and adds to scoreboard once user selects box.
    Then resets dice and roll before calling roll_one.
    '''
    box = input('Select which Scoreboard box you want to use.')
    scoreboard()

    points(box, dice)

    # Reset dice values before reroll
    dice = 0
    roll = 0
    roll_one(roll)


def points(box, dice):
    '''Calculates points scored'''
    if box == '1':
        score = sum(die == 1 for die in dice)
        return score
    if box == '2':
        score = sum(die == 2 for die in dice)
        return score
    if box == '3':
        score = sum(die == 3 for die in dice)
        return score
    if box == '4':
        score = sum(die == 4 for die in dice)
        return score
    if box == '5':
        score = sum(die == 5 for die in dice)
        return score
    if box == '6':
        score = sum(die == 6 for die in dice)
        return score
    if box == 'th':
        if len(set(dice)) <= 3:
            score = sum(dice)
            return score
        else:
            return 0
    if box == 'fo':
        if len(set(dice)) <= 4:
            score = sum(dice)
            return score
        else:
            return 0


def scoreboard():
    '''Holds the scores'''
    scoreboard = []
    print(scoreboard)


# Main code block
home()
