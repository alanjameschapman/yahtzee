# 80 characters wide and 24 rows high max

import random

def roll_one():
    """
    Generates a list of five random integers between 1 and 6 to represent die face values
    """
    result = []
    for die in range(5):
        roll = random.randint(1, 6)
        result.append(roll)
    return result

result = roll_one()
print(result)