## Code Validation

No errors were returned when passing through the official CI Python Linter.

![CI Python Linter](/docs/testing/linted.png)

Every user input was validated for various incorrect inputs, as shown in the next sections.

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
