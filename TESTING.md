# __Code Validation__

## Python Linter

No errors were returned when passing through the official CI Python Linter.

![CI Python Linter](/docs/testing/linted.png)

## User Story Testing

As a user, I want to:

- Play a solo, fun interactive game of Yahtzee and learn rules if needed.
- Input my name and be given feedback if I entered invalid data.
- Re-roll, submit score or escape home if desired.
- Easily select which dice I want to keep for re-roll and be given feedback if I entered invalid data.
- Get feedback on how my dice will score against my chosen category and allow me to change my mind.
- View my updated scoreboard as I progress through the game.
- Compete against my personal best.

## Input Validation by Function

Every user input was validated for various incorrect inputs, as shown in the next sections, broken down by function.

### home()

Input expected: 'r' or 'p'. Validation check for '', numeric, and invalid alphabetical, then prints error justification and repeats prompt.

Then, Input expected: name string. Validation checks for '' and numeric, then prints error justification and repeats input prompt.

![home validation](/docs/testing/functions/home.png)

### user_prompt()

Input expected: r, s, or e. Validation check for '', numeric, and invalid alphabetical, then prints error justification and repeats input prompt.

![user_prompt validation](/docs/testing/functions/user_prompt.png)

### keep_choice()

Input expected: numbers 1-5, separated by spaces. Validation check for '', alphabetical, and invalid numeric, then prints error justification and repeats prompt.

![keep_choice validation](/docs/testing/functions/keep_choice.png)

### submit()

Input expected: strings contained within box_options list (numbers 1-5, or box 'key'). Validation check for '', invalid numeric, and invalid alphabetical, then prints error justification and repeats prompt.

![submit validation](/docs/testing/functions/submit.png)

### points()

Input expected: 'y' string. Function uses .lower() method to convert to lowercase. Validation check for this, then calls update_category function if true, otherwise calls submit function.

![points validation](/docs/testing/functions/points.png)

### update_scoreboard()

Input expected: accepts any input, then resets roll variable and calls roll_one function.

![update_scoreboard validation](/docs/testing/functions/update_scoreboard.png)

### personal_best()

Input expected: accepts any input then resets score, which in turn calls roll_one function.

![update_scoreboard validation](/docs/testing/functions/personal_best.png)
