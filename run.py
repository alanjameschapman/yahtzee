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
    clear_display()
    print('''
          __     __      _    _ _______ ____________ ______ 
          \ \   / //\   | |  | |__   __|___  /  ____|  ____|
           \ \_/ //  \  | |__| |  | |     / /| |__  | |__   
            \   // /\ \ |  __  |  | |    / / |  __| |  __|  
             | |/ ____ \| |  | |  | |   / /__| |____| |____ 
             |_/_/    \_\_|  |_|  |_|  /_____|______|______|
          ''')

    # Loops until valid input given
    while True:
        home_input = input(
            "Type 'l' for leaderboard, 'r' for rules, or 'p' to play.\n"
            "Your choice: ")
        home_input = home_input.lower()
        # Validates input and prompts until valid.
        if home_input not in ['l', 'r', 'p']:
            print('Try again...\U0001F644')
        else:
            if home_input == 'l':
                leaderboard()
            elif home_input == 'r':
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
    input('Press Enter to return Home')
    home()


def rules():
    '''Displays rules. Clear screen method used to move to next page.'''
    clear_display()
    display_scoreboard(scores)
    print('''
Single Player Yahtzee Rules:
1. Objective: Score as high as possible by rolling five dice.
2. Turns: You have up to 3 rolls per turn to achieve the best score.
3. Scoring Categories: Upper Section (Aces, Twos, Threes, Fours, Fives, Sixes)
   and Lower Section (3 of a Kind, 4 of a Kind, Full House, Low Straight,
   High Straight, Yahtzee, Chance).
4. Upper Section: Score the sum of matching dice (e.g., Aces = sum of 1s).
5. Lower Section: Specific patterns (e.g., Full House = 3 of one number and 2
   of another).
6. Yahtzee: 5 of a kind scores 50 points; subsequent Yahtzees earn 100 points.
7. Chance: Sum of all dice.
8. Bonus: If upper section score > 63, earn a 35-point bonus.
9. Strategy: Plan your moves to maximize points in the right categories.
10. Winning: Try to beat your own high score!

    ''')

    input('Scroll up for Scoreboard and press Enter to return Home. ')
    home()


def roll_one(roll):
    """
    Generates a list of five random integers between 1 and 6 to represent die
    face values
    """
    clear_display()
    display_scoreboard(scores)
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
        input(f'You have taken 3 rolls and your dice are: {dice}\n'
              'Time to submit your score! Press Enter')
        clear_display()
        submit(dice)
    # Advises user of dice and asks for valid unput
    print(f'After roll {roll} ({remain} remaining), your dice are: {dice}\n'
          "Enter 'r' to re-roll, 's' to submit score, or 'e' to exit.")
    while True:
        game_choice = input('Your choice: ')
        game_choice = game_choice.lower()
        if game_choice not in ['r', 's', 'e']:
            print('Try again...\U0001F644')
        elif game_choice == 'e':
            home()
        elif game_choice == 's':
            clear_display()
            submit(dice)
        else:
            keep_choice(dice, roll)


def keep_choice(dice, roll):
    '''Takes dice and roll arg from previous roll and prompts the user to
    input which dice should be kept. Returns a list of integers to retain.'''

    print('Which dice do you want to keep? Enter numbers separated by spaces.')
    # Prompt the user to input which dice to keep.
    while True:
        dice_to_keep = input('Your choice:')

        # Check if the string is empty.
        if dice_to_keep == "":
            print('Try again...\U0001F644')
        # Check if the string contains letters.
        elif any(char.isalpha() for char in dice_to_keep):
            print('Try again...\U0001F644')
        else:
            # Split the input string into a list of integers.
            dice_to_keep = [int(i) for i in dice_to_keep.split()]

            # Check if any die values are out of range (1 to 5).
            if any(die < 1 or die > 5 for die in dice_to_keep):
                print('Enter numbers between 1 and 5.')
            else:
                keep_and_reroll(dice, roll, dice_to_keep)
                break


def keep_and_reroll(dice, roll, dice_to_keep):
    '''Takes dice arg from previous roll and re-rolls dice which aren't in
    keep list selected by user. Returns an updated list of dice values.'''
    # Create a copy of the dice list.
    dice = dice[:]
    # Converts user choice (1-5) to indices (0-4)
    dice_to_keep = [die-1 for die in dice_to_keep]

    # Re-roll the dice that are not being kept.
    for die in range(len(dice)):
        if die not in dice_to_keep:
            dice[die] = random.randint(1, 6)

    user_prompt(dice, roll)


def submit(dice):
    '''
    Evaluates score and adds to scoreboard once user selects box.
    Then resets dice and roll before calling roll_one.
    '''

    display_scoreboard(scores)
    print(f'Your dice are: {dice}')

    box_options = [
        '1', '2', '3', '4', '5', '6', 'th', 'fo', 'fh', 'ls', 'hs', 'y', 'c']
    while True:
        box = input("Enter box 'key' you want to use (see Scoreboard): ")
        # Check that box input is in the list of box_options
        if box not in box_options:
            print('Try again...\U0001F644')
        else:
            box = box.lower()
            points(box, dice)


def display_scoreboard(scores):
    '''Displays scoreboard'''

    # Initializes extras
    results = 0

    categories = [
        "Aces '1'    |",
        "Twos '2'    |",
        "Threes '3'  |",
        "Fours '4'   |",
        "Fives '5'   |",
        "Sixes '6'   |",
        "3 of a kind 'th'   = sum all dice |",
        "4 of a kind 'fo'   = sum all dice |",
        "Full House 'fh'.   = 25.......... |",
        "Low Straight 'ls'  = 30.......... |",
        "High Straight 'hs' = 40.......... |",
        "Yahtzee 'y'......  = 50.......... |",
        "Chance 'c'.......  = sum all dice |"]

    scoreboard = 'Upper Section\n'

    for i, category in enumerate(categories):
        if i < 6:
            scoreboard += f'Count and add only {category} {scores[i]}\n'

    results = extras(scores)

    upper_total = results['upper_total']
    upper_bonus = results['upper_bonus']
    upper_section_total = results['upper_section_total']
    lower_section_total = results['lower_section_total']
    grand_total = results['grand_total']

    scoreboard += f'Total......................... | {upper_total}\n' \
                  f'More than 63 scores a 35 Bonus | {upper_bonus}\n' \
                  f'Total of Upper Section........ | {upper_section_total}\n'

    scoreboard += '\nLower Section\n'

    for i, category in enumerate(categories):
        if i > 5:
            scoreboard += f'{category} {scores[i]}\n'

    scoreboard += f'Total............................ | \
{lower_section_total}\n'\
                  f'\nGrand Total...................... | \
{grand_total}\n'

    print(scoreboard)


def points(box, dice):
    '''Calculates points scored'''

    if box == '1':
        score = sum(die == 1 for die in dice)
    if box == '2':
        score = 2 * sum(die == 2 for die in dice)
    if box == '3':
        score = 3 * sum(die == 3 for die in dice)
    if box == '4':
        score = 4 * sum(die == 4 for die in dice)
    if box == '5':
        score = 5 * sum(die == 5 for die in dice)
    if box == '6':
        score = 6 * sum(die == 6 for die in dice)
    if box == 'th':
        for die in set(dice):
            if dice.count(die) >= 3:
                score = sum(dice)
                break
        else:
            score = 0
    if box == 'fo':
        for die in set(dice):
            if dice.count(die) >= 4:
                score = sum(dice)
                break
            else:
                score = 0
    if box == 'fh':
        if len(set(dice)) == 2 and (dice.count(die) == 3 for die in dice):
            score = 25
        else:
            score = 0
    if box == 'ls':
        dice.sort()
        unique_dice = list(set(dice))
        unique_dice_sets = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6],
                            [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        score = 30 if unique_dice in unique_dice_sets else 0
    if box == 'hs':
        dice.sort()
        unique_dice = list(set(dice))
        unique_dice_sets = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        score = 40 if unique_dice in unique_dice_sets else 0
    if box == 'y':
        score = 50 if len(set(dice)) == 1 else 0
    if box == 'c':
        score = sum(dice)

    points_input = input(
        f"This scores {score}. Enter 'y' to accept or anything else not to: ")

    # Validate user input to go here then update_scoreboard
    if points_input == "y":
        update_category(box, score)
    else:
        clear_display()
        submit(dice)


def update_category(box, score):

    if box == '1':
        scores[0] = score
        update_scoreboard(scores)
    elif box == '2':
        scores[1] = score
        update_scoreboard(scores)
    elif box == '3':
        scores[2] = score
        update_scoreboard(scores)
    elif box == '4':
        scores[3] = score
        update_scoreboard(scores)
    elif box == '5':
        scores[4] = score
        update_scoreboard(scores)
    elif box == '6':
        scores[5] = score
        update_scoreboard(scores)
    elif box == 'th':
        scores[6] = score
        update_scoreboard(scores)
    elif box == 'fo':
        scores[7] = score
        update_scoreboard(scores)
    elif box == 'fh':
        scores[8] = score
        update_scoreboard(scores)
    elif box == 'ls':
        scores[9] = score
        update_scoreboard(scores)
    elif box == 'hs':
        scores[10] = score
        update_scoreboard(scores)
    elif box == 'y':
        scores[11] = score
        update_scoreboard(scores)
    elif box == 'c':
        scores[12] = score
        update_scoreboard(scores)
    else:
        pass


def update_scoreboard(scores):
    clear_display()

    results = 0

    categories = [
        "Aces '1'    |",
        "Twos '2'    |",
        "Threes '3'  |",
        "Fours '4'   |",
        "Fives '5'   |",
        "Sixes '6'   |",
        "3 of a kind 'th'   = sum all dice |",
        "4 of a kind 'fo'   = sum all dice |",
        "Full House 'fh'.   = 25.......... |",
        "Low Straight 'ls'  = 30.......... |",
        "High Straight 'hs' = 40.......... |",
        "Yahtzee 'y'......  = 50.......... |",
        "Chance 'c'.......  = sum all dice |"]

    scoreboard = 'Upper Section\n'

    for i, category in enumerate(categories):
        if i < 6:
            scoreboard += f'Count and add only {category} {scores[i]}\n'

    results = extras(scores)

    # Used to access dictionary value returned from extras()
    upper_total = results['upper_total']
    upper_bonus = results['upper_bonus']
    upper_section_total = results['upper_section_total']
    lower_section_total = results['lower_section_total']
    grand_total = results['grand_total']

    scoreboard += f'Total......................... | {upper_total}\n' \
                  f'More than 63 scores a 35 Bonus | {upper_bonus}\n' \
                  f'Total of Upper Section........ | {upper_section_total}\n'

    scoreboard += '\nLower Section\n'

    for i, category in enumerate(categories):
        if i > 5:
            scoreboard += f'{category} {scores[i]}\n'

    scoreboard += f'Total............................ | \
{lower_section_total}\n' \
                  f'\nGrand Total...................... | \
{grand_total}\n'

    print(scoreboard)
    update_scoreboard_input = input("Enter to roll again")
    if update_scoreboard_input == "":
        roll = 0
        roll_one(roll)
    else:
        home()


def extras(scores):
    '''Calculates bonuses and totals'''

    # Initializes extras
    results = {}
    upper_total = 0
    upper_bonus = 0
    upper_section_total = 0
    lower_section_total = 0
    grand_total = 0

    # Calculates upper total from first 6 indices
    for score in scores[:6]:
        if not str(score).isalpha():
            upper_total += int(score)

    # Checks if upper bonus applies
    if not str(upper_total).isalpha():
        if upper_total >= 63:
            upper_bonus = 35

    # Calculates upper section total including bonus
    if upper_bonus == 35:
        upper_section_total = upper_total + upper_bonus
    else:
        upper_section_total = upper_total

    # Calculates lower total from lower section
    for score in scores[6:13]:
        if not str(score).isalpha():
            lower_section_total += int(score)

    # Calculates grand total from upper and lower sections
    grand_total = upper_section_total + lower_section_total

    results['upper_total'] = upper_total
    results['upper_bonus'] = upper_bonus
    results['upper_section_total'] = upper_section_total
    results['lower_section_total'] = lower_section_total
    results['grand_total'] = grand_total

    return results


# Main code block
scores = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
home()
