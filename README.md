# Gmail cli

Gmail cli is a simple text client for gmail.
To use it you **MUST** have an account on Google cloud and you must register your app.
To do this you must:

* connect to [Google cloud console](https://console.cloud.google.com)
* click "Select a project" and in the new screen click "New project"
* in the "Project name" field write "Gmail cli" and click "Create"
* now in the upper left corner of your screen after the Google cloud title you must have a button "No organization".
  Click the button and select your new project. Now the button with no organization will change in your project name.
* In your project dashboard you have an "Explore and enable APIs" section. Click this section and in the new screen
  select "+ Enable APIs and services". Search for "gmail api" and click the button "Gmail API" to select it.
* After selected, in the new screen click the button "Enable".
* After enabled the API you must create credentials. In the API dashboard you have now a "Create credential" button.
  Click it.
* In the new screen select "User data" radio button and then click next. Fill the other field with your app name, e-mail,
  logo if you want and the developer e-mail address. Then click "Save and continue".
* In the next screen click "Save and continue" with no changes in the various fields.
* In the next screen select "Desktop application" in the application type field and write the name you want for your application
  in the name field.
* Then click the "Create" button to create credentials.
* Now you **MUST** download your credentials in json format. Then click "done" button.
* In the "Credentials" section you have your new credentials for Gmail API.

## How project is organized
The project use [uv]("https://docs.astral.sh/uv/") as project manager.
The sources and the configuration files for uv are in the root directory.
In the "spec" directory there are the specs for PyInstaller.

## Executables
The executable is available by now only for Linux and is compiled with PyInstaller >= 6.22.2.
* Linux version is compiled in Debian version 13 (Trixie)
* Windows version is compiled in Windows 11

To run gmail_cli with executables you must run gmail_cli_{version} "your gmail address"

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
* **help**:      Print help message
* **exit/quit**: Exit the terminal
