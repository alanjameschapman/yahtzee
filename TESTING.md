# __Code Validation__

## __Python Linter__

Python coding errors were caught and fixed using [CI pep8 linter](https://pep8ci.herokuapp.com/#). The deployed site returned no errors.

![CI Python Linter](/docs/testing/linted.png)

## __User Story Testing__

| As a user, I want to... | Requirement met | Image(s) |
| :---------------------- | :------------: | :------: |
| Play a solo, fun interactive game of Yahtzee and learn rules if needed. | YES | ![story1](/docs/testing/user_stories/story1.png) |
| Input my name which will be used throughout the game | YES | ![story2a](/docs/testing/user_stories/story2a.png) ![story2b](/docs/testing/user_stories/story2b.png) |
| Re-roll, submit score or escape home if desired. | YES | ![story3](/docs/testing/user_stories/story3.png) |
| Easily select which dice I want to keep for re-roll | YES | ![story4](/docs/testing/user_stories/story4.png) |
| Get feedback on how my dice will score against my chosen category and allow me to change my mind. | YES | ![story5](/docs/testing/user_stories/story5.png) |
| View my updated scoreboard as I progress through the game. | YES | ![story6](/docs/testing/user_stories/story6.png) |
| Compete against my personal best. | YES | ![story7](/docs/testing/user_stories/story7.png) |

## __Input Validation by Function__

Every user input was validated for various incorrect inputs, as shown in the next sections, broken down by function.

| Function Tested | Inputs Validated | Validation Test | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: | :--------------: | :-------------: | :--------------- | :------------: | :-------: |
| home() | 'r' or 'p' | '', number and invalid letter | Print error, repeat input prompt | ![home validation](/docs/testing/functions/home.png) | PASS |
| home() | name string | '' and number | Print error, repeat input prompt. | ![home validation](/docs/testing/functions/home.png) | PASS |
| user_prompt() | 'r', 's', or 'e' | '', number, and invalid letter | Print error, repeat input prompt. | ![user_prompt validation](/docs/testing/functions/user_prompt.png) | PASS |
| keep_choice() | Numbers 1-5 separated by spaces | '', letter and invalid number | Print error, repeat input prompt | ![keep_choice validation](/docs/testing/functions/keep_choice.png) | PASS |
| submit() | Strings contained within box_options list (numbers 1-5, or box 'key') | '', invalid number and invalid letter | Prints error justification and repeats prompt. |![submit validation](/docs/testing/functions/submit.png) | PASS |
| points() | 'y' string. | Function uses .lower() method to convert to lowercase. | Call update_category function if true, else call submit function. | ![points validation](/docs/testing/functions/points.png) | PASS |
| update_scoreboard() | Any input | '1' | Reset roll variable call roll_one function. | ![update_scoreboard validation](/docs/testing/functions/update_scoreboard.png) | PASS |
| personal_best() | Any input | '' | Reset score, restart game, compare grand_total to 'pb' on next pass and provide user feedback | ![update_scoreboard validation](/docs/testing/functions/personal_best.png)

## __Browser Testing__

| Browser | Image(s) |
| ------- | :------: |
| Chrome | ![chrome](docs/testing/browsers/chrome.png) |
| Firefox | ![firefox](docs/testing/browsers/firefox.png) |
| Edge | ![edge](docs/testing/browsers/edge.png) |

## __Debugging__

Bugs were tracked using GitHub's Issues functionality - click [here](https://github.com/alanjameschapman/yahtzee/issues)

Code blocks isolated and refactored using [python tutor](<https://pythontutor.com/>)
