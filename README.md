# __Yahtzee__

Yahtzee is a dice game which can be be played as multi-player or single player. For the purposes of this project, I have chosen to write a program for the latter.  

## __Planning__

I evaluated several other ideas for this project (Noughts and crosses, sudoku) and documented them [here](https://docs.google.com/presentation/d/1O7Istg9Qo5xgLVj28-5xCkhKq3LVPhd5kdKdjbkPYx4/edit?usp=sharing). I chose Yahtzee because it has a challenging set of scoring rules, and it lends itself well to customization. For example, it can be played solo or multi-player, single-game or multi-game and has an optional Yahtzee bonus score. It also lends itself well to a leaderboard using Google leaderboard - see [Future Enhancements](#future-enhancements).

### __Flowchart__

To help me structure the functions and visualize the user stories, I created a flowchart.

![flowchart](/docs/flowchart.png)

## __UX & Design__

### __User Stories__

As a user, I want to:

- Play a solo, fun interactive game of Yahtzee and learn rules if needed.
- Input my name and be given feedback if I entered invalid data.
- Re-roll, submit score or escape home if desired.
- Easily select which dice I want to keep for re-roll and be given feedback if I entered invalid data.
- Get feedback on how my dice will score against my chosen category and allow me to change my mind.
- View my updated scoreboard as I progress through the game.
- Compete against my personal best.

### __Colorama__

Colours have been used to help the user understand how to select the correct box in which to score points:

![colorama](/docs/colorama.png)

### __Terminal Window Size__

This app was originally designed to fit a terminal screen size of 80 columns by 24 rows. Due to this constraint, I have used a clear_display function to minimize the amount of information displayed on the screen at any one time. Even so, there were times (such as the rules screen screen) where the screen size was intentionally exceeded to enable the user to see all the information in one place, albeit with scrolling.

Some rows were repeating due to conflict between terminal size and clear_display function. This is a known bug which occurs if some rows are hidden from view when clear_display function is used.

Columns and rows were increased from 80 and 24 to 100 and 40 respectively.

![terminal size](/docs/testing/bugs/bug2_fix_terminal.png)

By increasing the terminal size, the scoreboard with rules displayed without any errors.

![terminal size](/docs/testing/bugs/bug2_fix_scoreboard_display.png)

### __Lessons learned from previous project implemented here__

- Section on validation and bug fixes included in table form.
- Validation errors caught and fixed using the [CI pep8 linter](https://pep8ci.herokuapp.com/#).
- Commit messages like "take 2" avoided. Messages kept short and frequent. Commits made per file or folder.

### __Features and Functionality__

Features and functions have been designed to meet the requirements of the User Stories. Docstrings are provided for every function explaining what they doc. Additional comments are included where helpful.

### __Imported Libraries and Packages__

- [random](https://docs.python.org/3/library/random.html) was used to generate 5 random numbers between 1-6 to represent dice face values.
- [os](https://docs.python.org/3/library/os.html) was used to create the clear_display function to enhance user experience and reduce clutter on screen.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour to some aspects of the program to help them stand out.

## Testing and Debugging

View Testing and Bug Fixing [here.](TESTING.md)

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://yahtzee-dice-6d5009f4b077.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to \`PORT\`, and the value to \`8000\` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select \`Python\` first, then \`Node.js\` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- \`pip3 install -r requirements.txt\`

If you have your own packages that have been installed, then the requirements file needs updated using:

- \`pip3 freeze --local > requirements.txt\`

The **Procfile** can be created with the following command:

- \`echo web: node index.js > Procfile\`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: \`heroku login -i\`
- Set the remote for Heroku: \`heroku git:remote -a app_name\` (replace *app_name* with your app name)
- After performing the standard Git \`add\`, \`commit\`, and \`push\` to GitHub, you can now type:
	- \`git push heroku main\`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- \`pip3 install -r requirements.txt\`.

If using any confidential credentials, such as \`CREDS.json\` or \`env.py\` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/alanjameschapman/yahtzee) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- \`git clone https://github.com/alanjameschapman/yahtzee.git\`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/alanjameschapman/yahtzee)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/alanjameschapman/yahtzee)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## __Future Enhancements__

- Interaction with Google Sheets to read/write data to/from a Leaderboard.
- Play against the computer.
- Inlcude a Yahtzee bonus.

## __Credits__

### __Code__
- Code to create clear_display function taken from [Delftstack](https://www.delftstack.com/howto/python/python-clear-console/)
- Code to generate 5 random numbers between 1-6 to represent dice face value taken from [Real Python](https://realpython.com/python-dice-roll/)
- Code to display ASCII art for YAHTZEE lettering generated by [ascii-art-generator](https://www.ascii-art-generator.org/)

### __Design__
- The Flowchart was made using Google Slides.
- Favicon was taken from [freefavicon](https://www.freefavicon.com/freefavicons/objects/iconinfo/dice-152-26713.html)

### Content

The site is intended solely for educational purposes. All images and favicons remain the property of those credited above

## __Acknowledgements__

I would like to give special thanks to my mentors, [Dave Bowers](https://www.linkedin.com/in/dnlbowers/) and [Tim Nelson](https://www.linkedin.com/in/travel-tim-nelson/) for their guidance during the development of this project. The latter provided a useful reference to an example README [here](https://github.com/adamgilroy22/python-hangman).
