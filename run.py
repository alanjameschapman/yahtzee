# 80 characters wide and 24 rows high max

import random


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


def user_choice(dice):
    """Takes dice arg from previous roll and prompts the user to input which
    dice should be kept. Returns a list of integers to retain.
    """

    # Print the current roll.
    print(f'Your current roll is: {dice}')

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


dice = roll_one()
keep = user_choice(dice)
new_dice = keep_and_reroll(dice, keep)
print(f'Your updated roll is {new_dice}. You have one roll remaining.')
