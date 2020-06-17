# DukPublic
<img src="https://img.shields.io/reddit/user-karma/combined/mirandanielcz?style=flat-square" alt=""><img src="https://img.shields.io/discord/709357899633393675?style=flat-square" alt="">
<img src="https://img.shields.io/github/last-commit/MiranDaniel/dukpublic?style=flat-square" alt=""><img src="https://img.shields.io/github/release-date/MiranDaniel/dukpublic?style=flat-square" alt="">

## Features
	Ban users with more than x removed posts.
	Remove posts based on flair text.
	Discord UI for accessing the SQL easily.
	Easy to set up.

## Setup guide
[Duplicate this reposity to your own account as private](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository "Duplicate this reposity to your own account as private")

### Creating Reddit The Bot

	1. Log into Reddit, head over to the Reddit app [preferences page](https://www.reddit.com/prefs/apps/ "preferences page"), and click 'create an app'.
	2. Give it whatever name you'd like and select the script type. 
	3. Finally, Reddit apps require a redirect URI. You won’t be using it however, so just put in a dummy one, such as http://www.example.com/

### Creating Heroku Hosting
Fill out the [signup page of heroku](https://signup.heroku.com/ "signup page of heroku") and click create free account
Complete the signup
Head to [dashboard.heroku.com/new-app](https://dashboard.heroku.com/new-app "dashboard.heroku.com/new-app")
Name the app anything you want.
Select a region.
Click create app.
Click **Deploy** and pick GitHub.
Select the repository you duplicated.
Scroll down and enable Automatic Deploys, then click Deploy Branch and wait.
Once the output dissapears and the text "Your app was successfully deployed." shows up continue to the another step.

### Creating a SQL database
[Go to the add-on page of Postgres on Heroku.](https://elements.heroku.com/addons/heroku-postgresql "Go to the add-on page of Postgres on Heroku.")
Click Install Heroku Postgres
Add to provision to is the name of the app you made earlier so fill it out.
Click Provision add-on
Go to the page of your database by clicking "heroku postgres" on your Resources tab.
Go to the Settings page of your database and click View Credentials…
Use these credentials to fill out the variables in login.py under the SQL part.
