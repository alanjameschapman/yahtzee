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
print(dice)

# Keeps the first two dice and re-roll the rest.
keep = [0, 1, 2]
new_dice = keep_and_reroll(dice, keep)
print(new_dice)
