# Imports used to generate dice rolls and for clear_display()
import random
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear_display():
    '''Clears the display'''
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    os.system('cls' if os.name == 'nt' else "clear")


def home():
    '''Displays home screen and user prompt for rules game.'''
    global user_name
    clear_display()
    print('''
          __     __      _    _ _______ ____________ ______
          \\ \\   / //\\   | |  | |__   __|___  /  ____|  ____|
           \\ \\_/ //  \\  | |__| |  | |     / /| |__  | |__
            \\   // /\\ \\ |  __  |  | |    / / |  __| |  __|
             | |/ ____ \\| |  | |  | |   / /__| |____| |____
             |_/_/    \\_\\_|  |_|  |_|  /_____|______|______|
          ''')

    # Loops until valid input given
    while True:
        home_input = input(
            "Enter 'r' for rules, or 'p' to play.\n"
            "Your choice: ")
        home_input = home_input.lower()
        # Validates input and prompts until valid.
        if home_input not in ['r', 'p']:
            print(f"'{home_input}' invalid'. Enter only 'r' or 'p'.")
        else:
            if home_input == 'r':
                rules()
            else:
                while True:
                    user_name = input('Please enter your name: ')
                    if not user_name.isalpha():
                        print(f"'{user_name}' invalid. Enter only letters.")
                    else:
                        user_name = user_name.capitalize()
                        input(f"OK '{user_name}', let's play Yahtzee!\n"
                              'Hit Enter to roll dice...')
                        roll = 0
                        roll_one(roll)


def personal_best(grand_total):
    '''Checks for PB for current session'''
    global pb
    roll = 0
    if grand_total > pb:
        pb = grand_total
        input(f'Congratulations {user_name}, you have set a new PB of {grand_total}. Press Enter to roll the dice. ')  # noqa
        reset_scores(roll)
    else:
        input(f'Hard lines {user_name}, your high score remains {pb}. Press Enter to roll the dice. ')  # noqa
        reset_scores(roll)


def reset_scores(roll):
    '''Resets global scores'''
    global scores
    scores = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    roll_one(roll)


def rules():
    '''Displays rules. Clear screen method used to move to next page.'''
    clear_display()
    display_scoreboard(scores)
    print('''Single Player Yahtzee Rules:
- Objective: Score as high as possible by rolling five dice.
- Turns: You have up to 3 rolls per turn to achieve the best score.
- Scoring Categories: Upper Section (Aces, Twos, Threes, Fours, Fives, Sixes) and Lower Section (3 of a Kind, 4 of a Kind, Full House, Low Straight, High Straight, Yahtzee, Chance).'''  # noqa
'''
- Upper Section: Score the sum of matching dice (e.g., Aces = sum of 1s).
- Lower Section: Specific patterns (e.g., Full House = 3 of one number and 2 of another).'''  # noqa
'''
- Yahtzee: 5 of a kind scores 50 points.
- Chance: Sum of all dice.
- Bonus: If upper section score > 63, earn a 35-point bonus.
- Strategy: Plan your moves to maximize points in the right categories.
    ''')

    input('Scroll up for Scoreboard and press Enter to return Home...')
    home()


def roll_one(roll):
    """
    Generates a list of five random integers between 1 and 6 to represent die
    face values
    """
    # global scores
    clear_display()
    display_scoreboard(scores)
    dice = []
    for die in range(5):
        die = random.randint(1, 6)
        dice.append(die)

    user_prompt(dice, roll, scores)


def user_prompt(dice, roll, scores):
    '''Prints the current roll and prompts user to re-roll, submit or exit.'''
    roll += 1
    remain = 3-roll

    # Check if the user has taken 3 rolls.
    if roll >= 3:
        input(f'You have taken 3 rolls and your dice are: {dice}\n'
              'Time to submit your score! Press Enter')
        clear_display()
        submit(dice, scores)
    # Advises user of dice and asks for valid unput.
    print(
        f'After roll {roll} ({remain} remaining), your dice are: {dice}\n'
        f"Enter 'r' to re-roll, 's' to submit score, or 'e' to exit.")
    while True:
        game_choice = input('Your choice: ')
        game_choice = game_choice.lower()
        if game_choice not in ['r', 's', 'e']:
            print(f"'{game_choice}' invalid. Enter only 'r', 's' or 'e'.")
        elif game_choice == 'e':
            home()
        elif game_choice == 's':
            clear_display()
            submit(dice, scores)
        else:
            keep_choice(dice, roll)


def keep_choice(dice, roll):
    '''Takes dice and roll arg from previous roll and prompts the user to
    input which dice should be kept. Returns a list of integers to retain.'''

    print('''Which dice do you want to keep? Enter only numbers 1-5 separated \
 by spaces.''')
    # Prompt the user to input which dice to keep.
    while True:
        dice_to_keep = input('Your choice: ')

        # Check if the string is empty or contains letters.
        if dice_to_keep == "" or any(char.isalpha() for char in dice_to_keep):
            print(f"'{dice_to_keep}' invalid. \
Enter only numbers 1-5 separated by spaces.")
        else:
            # Split the input string into a list of integers.
            dice_to_keep = [int(i) for i in dice_to_keep.split()]

            # Check if any die values are out of range (1 to 5).
            if any(die < 1 or die > 5 for die in dice_to_keep):
                print(f"'{dice_to_keep}' invalid. \
Enter only numbers 1-5 separated by spaces.")
            else:
                keep_and_reroll(dice, roll, dice_to_keep)
                # break


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

    user_prompt(dice, roll, scores)


def submit(dice, scores):
    '''
    Evaluates score and adds to scoreboard once user selects box.
    Then resets dice and roll before calling roll_one.
    '''

    display_scoreboard(scores)
    print(f'Your dice are: {dice}')

    box_options = [
        '1', '2', '3', '4', '5', '6', 'th', 'fo', 'fh', 'ls', 'hs', 'y', 'c']
    while True:
        box = input(f"Enter box {Fore.GREEN+Style.BRIGHT}'key'\
{Fore.RESET+Style.NORMAL} "
                    f"you want to use (see Scoreboard): ").lower()

        # Check that box input is in the list of box_options and not marked 'x'
        if box not in box_options:
            print(f"'{box}' invalid. Enter a valid box \
{Fore.GREEN+Style.BRIGHT}'key'{Fore.RESET+Style.NORMAL}.")
        elif not scores[box_options.index(box)] == 'x':
            print(f"The box {Fore.GREEN+Style.BRIGHT}'{box}'\
{Fore.RESET+Style.NORMAL} already has an 'x'. Choose another box.")
        else:
            points(box, dice, scores)
            # Mark the selected box with an 'x'
            scores[box_options.index(box)] = 'x'
            break


def display_scoreboard(scores):
    '''Displays scoreboard'''

    categories = [
        f"Aces {Fore.GREEN+Style.BRIGHT}'1'{Fore.RESET+Style.NORMAL}    |",
        f"Twos {Fore.GREEN+Style.BRIGHT}'2'{Fore.RESET+Style.NORMAL}    |",
        f"Threes {Fore.GREEN+Style.BRIGHT}'3'{Fore.RESET+Style.NORMAL}  |",
        f"Fours {Fore.GREEN+Style.BRIGHT}'4'{Fore.RESET+Style.NORMAL}   |",
        f"Fives {Fore.GREEN+Style.BRIGHT}'5'{Fore.RESET+Style.NORMAL}   |",
        f"Sixes {Fore.GREEN+Style.BRIGHT}'6'{Fore.RESET+Style.NORMAL}   |",
        f"3 of a kind {Fore.GREEN+Style.BRIGHT}'th'{Fore.RESET+Style.NORMAL} = sum all dice. |",  # noqa
        f"4 of a kind {Fore.GREEN+Style.BRIGHT}'fo'{Fore.RESET+Style.NORMAL} = sum all dice. |",  # noqa
        f"Full House {Fore.GREEN+Style.BRIGHT}'fh'{Fore.RESET+Style.NORMAL} = 25............ |",  # noqa
        f"Low Straight {Fore.GREEN+Style.BRIGHT}'ls'{Fore.RESET+Style.NORMAL} = 30.......... |",  # noqa
        f"High Straight {Fore.GREEN+Style.BRIGHT}'hs'{Fore.RESET+Style.NORMAL} = 40......... |",  # noqa
        f"Yahtzee {Fore.GREEN+Style.BRIGHT}'y'{Fore.RESET+Style.NORMAL}...... = 50.......... |",  # noqa
        f"Chance {Fore.GREEN+Style.BRIGHT}'c'{Fore.RESET+Style.NORMAL}....... = sum all dice |"]  # noqa

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

    scoreboard += f'Total........................... | \
{lower_section_total}\n'\
                  f'\nGrand Total..................... | \
{grand_total}\n'

    print(scoreboard)


def points(box, dice, scores):
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
        dice = [int(d) for d in dice]
        unique_dice = list(set(dice))
        unique_dice.sort()
        unique_dice_sets = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6], [1, 2, 3, 4, 6]]  # noqa
        score = 30 if unique_dice in unique_dice_sets else 0
    if box == 'hs':
        dice = [int(d) for d in dice]
        unique_dice = list(set(dice))
        dice.sort()
        unique_dice_sets = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        score = 40 if unique_dice in unique_dice_sets else 0
    if box == 'y':
        score = 50 if len(set(dice)) == 1 else 0
    if box == 'c':
        score = sum(dice)

    points_input = input(
        f"This scores {score}. Enter 'y' to accept or anything else not to: ")

    # Validate user input to go here then update_scoreboard
    points_input.lower()
    if points_input == "y":
        update_category(box, score)
    else:
        clear_display()
        submit(dice, scores)


def update_category(box, score):
    '''Defines which box should be updated by the update_scoreboard function'''

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
    '''Updates relevant box within scoreboard'''
    clear_display()
    categories = [
        f"Aces {Fore.GREEN+Style.BRIGHT}'1'{Fore.RESET+Style.NORMAL}    |",
        f"Twos {Fore.GREEN+Style.BRIGHT}'2'{Fore.RESET+Style.NORMAL}    |",
        f"Threes {Fore.GREEN+Style.BRIGHT}'3'{Fore.RESET+Style.NORMAL}  |",
        f"Fours {Fore.GREEN+Style.BRIGHT}'4'{Fore.RESET+Style.NORMAL}   |",
        f"Fives {Fore.GREEN+Style.BRIGHT}'5'{Fore.RESET+Style.NORMAL}   |",
        f"Sixes {Fore.GREEN+Style.BRIGHT}'6'{Fore.RESET+Style.NORMAL}   |",
        f"3 of a kind {Fore.GREEN+Style.BRIGHT}'th'{Fore.RESET+Style.NORMAL} = sum all dice. |",  # noqa
        f"4 of a kind {Fore.GREEN+Style.BRIGHT}'fo'{Fore.RESET+Style.NORMAL} = sum all dice. |",  # noqa
        f"Full House {Fore.GREEN+Style.BRIGHT}'fh'{Fore.RESET+Style.NORMAL} = 25............ |",  # noqa
        f"Low Straight {Fore.GREEN+Style.BRIGHT}'ls'{Fore.RESET+Style.NORMAL} = 30.......... |",  # noqa
        f"High Straight {Fore.GREEN+Style.BRIGHT}'hs'{Fore.RESET+Style.NORMAL} = 40......... |",  # noqa
        f"Yahtzee {Fore.GREEN+Style.BRIGHT}'y'{Fore.RESET+Style.NORMAL}...... = 50.......... |",  # noqa
        f"Chance {Fore.GREEN+Style.BRIGHT}'c'{Fore.RESET+Style.NORMAL}....... = sum all dice |"]  # noqa

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

    scoreboard += f'Total........................... | \
{lower_section_total}\n' \
                  f'\nGrand Total..................... | \
{grand_total}\n'

    print(scoreboard)

    if 'x' in scores:
        input("Enter to roll again...")
        roll = 0
        roll_one(roll)
    else:
        input(f"Game over. Your final score is {grand_total}. Press Enter... ")
        personal_best(grand_total)


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
pb = 0
if __name__ == '__main__':
    ''' Python app initialised, call the first function '''
    home()
