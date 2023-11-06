# Yahtzee

Yahtzee is a dice game which can be be played as multi-player or single player. For the purposes of this project, I have chosen to write a program for the latter.  

## Planning

This app was designed to fit a terminal screen size of 80 columns by 24 rows. Due to this constraint, I used a clear_display function to minimize the amount of information displayed on the screen. Where the screen size is exceeded, such as the rules screen, this has been intentionally done to enable the user to see all the information in one place, albeit with scrolling.

### User Experience

- Users who want to play a solo, fun interactive game.
- Users who want to improve their previous scores.
- Ability to learn rules, restart game and compete against themselves.

### Colorama

Colours have been used to help the user understand how to select the correct box in which to score points.

### Lessons learned from previous project implemented here

- Section on bug fixes included.
- Validation errors caught and fixed using CI pep8 linter: https://pep8ci.herokuapp.com/#.
- Commit messages like "take 2" avoided. Messages kept short and frequent.

## Functionality

For a description of each function, docstrings are provided within.

### Instructions Area

Instructions provided to user, along with a link to help them understand how to answer the questions.

## Testing and User Input Validation per Function

No errors were returned when passing through the official CI Python Linter.

Every user input was validated 

### home

Input expected: l, r or p. Validation check for '', numeric, and invalid alphabetical, then prints error justification and repeats prompt.

Then, Input expected: name string. Validation checks for '' and numeric, then prints error justification and repeats input prompt.

![home validation](/docs/testing/home.png)

### user_prompt

Input expected: r, s, or e. Validation check for '', numeric, and invalid alphabetical, then prints error justification and repeats input prompt.

![user_prompt validation](/docs/testing/user_prompt.png)

### keep_choice

Input expected: numbers 1-5, separated by spaces. Validation check for '', alphabetical, and invalid numeric, then prints error justification and repeats prompt.

![keep_choice validation](/docs/testing/keep_choice.png)

### submit

Input expected: strings contained within box_options list (numbers 1-5, or box 'key'). Validation check for '', invalid numeric, and invalid alphabetical, then prints error justification and repeats prompt.

![submit validation](/docs/testing/submit.png)

### points

Input expected: 'y' string. Function uses .lower() method to convert to lowercase. Validation check for this, then calls update_category function if true, otherwise calls submit function.

![points validation](/docs/testing/points.png)

### update_scoreboard

Input expected: accepts any input, then resets roll variable and calls roll_one function.

![update_scoreboard validation](/docs/testing/update_scoreboard.png)


### Debugging Code

I used python tutor to isolate and refactor code blocks: <https://pythontutor.com/>

## Deployment

The site was deployed to Heroku pages. The steps to deploy were as follows:

- In the Heroku home screen I selected Create New app from the 'New' drop-down menu.
- I created a unique game and selected 'Europe' under region, then 'Create app'.
- Under the 'Deploy' heading and within 'Deployment Method' section I connected to the relevant repository in GitHub.
- Under the 'Settings' heading and within 'Reveal Config Vars' section I added PORT = 8000. Within 'Buildpacks' I added python and nodejs in that order.
- Under the 'Deploy' heading and within 'Manual Deploy' section I deployed main branch.
- The live link can be found here - <https etc. >

## Future Enhancements

Interaction with Google Sheet to read/write data to/from a Leaderboard.

## Credits

### Peer Review

Following on from #peer-code-review on Slack (TBC) and mentor feedback from Tim Nelson and David Bowers I implemented a few improvements:

- Escape characters used to correct Yahtzee ASCII art for home screen.
- Colorama used to clarify to the user how to allocate their points.

### Content

Code blocks isolated and refactored used python tutor: <https://pythontutor.com/>

Validation errors caught and fixed using CI pep8 linter: https://pep8ci.herokuapp.com/#.

The site is intended solely for educational purposes. All images and favicons remain the property of those credited above