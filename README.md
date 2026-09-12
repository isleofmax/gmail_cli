# Gmail cli

Gmail cli is a simple text client for gmail.
To use it you **MUST** have an account on Google cloud and you must register your app.
To do this you must:

* connect to [Google cloud console](https://console.cloud.google.com)
* click the "Open project picker" or press Ctrl + O and in the new screen click "New project"
* in the "Project name" field write "Gmail cli" or whatever you want and click "Create"
* click again in the "Open project picker" and select your new project and the project picker button will change with your project name.
* In your project dashboard, in the "Quick access" section, you have the button "API API's & Services" (you can find it in the hamburger menu
  on the top left corner). Click the button and in the new screen select **"+ Enable APIs and services"**.
  Search for "gmail api" and click the button "Gmail API" to select it.
* After selected, in the new screen click the button **Enable**.
* After you clicked **Enable** you'll be redirected to "Enabled APIs & services" menu in the section "APIs & services".
* At the top right you can see **Create credentials** button. Click it.
* In the new screen select "User data" radio button and then click next. Fill the other field with your app name, e-mail,
  logo if you want and the developer e-mail address. Then click "Save and continue".
* In the next screen click "Save and continue" with no changes in the various fields.
* In the next screen select "Desktop application" in the application type field and write the name you want for your application
  in the name field.
* Then click the "Create" button to create credentials.
* Now you **MUST** download your credentials in json format. Then click "done" button.
* In the "Credentials" section you have your new credentials for Gmail API.
* After created the credentials you must add your email to try the services. To do this click **OAuth consent screen** in the API & Service
  menu on the left. You'll be redirect to the **Google Auth Platform** and in this section click **Audience** in the menu on the left and then
  **Make external**. Choose the testing publishing status and confirm. At the bottom of the page add your user for testing (you must provide
  your Gmail Account) and you have done.
* **Warning**, if you lose the credentials or you want add new credentials you can go, from google cloud console dashborad, in the Credentials section
  of the API & Service menu found in the Hamburger menu on top left of the dashboard.

## How project is organized
The project use [uv]("https://docs.astral.sh/uv/") as project manager.
The sources and the configuration files for uv are in the root directory.
In the "spec" directory there are the specs for PyInstaller.

## Configuration file
Configuration file must be named config.json and inside you must provide the directory where the secret file is:
```
{
    "secret": "your secret json file.json"
}
```

## How to run the project
To run the project you must provide configuration file in the same directory of the main script (main.py).
Then you can run gmail_cli using:
* uv run main.py "your gmail address"

Otherwise you can use the executables which are available in the dist directory.
Again you must provide the configuration file in the same directory of the executable.
Excutables are, by now, only for Linux and Windows and are compiled with PyInstaller >= 6.22.2.
* Linux version is compiled in Ubuntu 22.04.5 LTS (jammy)
* Windows version is compiled in Windows 11

To run gmail_cli with executables you must run gmail_cli_{os} "your gmail address"

### How to build executables
#### Linux
* uv run pyinstaller spec/gmail_cli_linux.spec
#### Windows
* uv run pyinstaller spec/gmail_cli_win.spec


## Libraries
Gmail cli uses python >= 3.14.7 with theese libraries:
* beautifulsoup4 >= 4.15.0
* google-api-python-client >= 2.198.0
* google-auth >= 2.56.3
* google-auth-oauthlib >= 1.4.0

## Run gmail_cli without build executabe
* uv run main.py "your gmail address"

## Commands provided
* **listl**:     List labels of your gmail account
* **currl**:     Display the label of your gmail account where you are in
* **changel**:   Change the label of your gmail account where you are in
* **clear**:     Clear the screen
* **currp**:     List emails in the current page
* **next**:      List next page of e-mails in the current label
* **prev**:      List previous page of e-mails in the current label
* **read**:      Read the selected e-mail
* **del**:       Move the selected e-mail to Trash
* **help**:      Print help message
* **exit/quit**: Exit the terminal
