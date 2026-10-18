# Gmail CLI
Gmail CLI is a simple text-based client for Gmail.
To use it, you **MUST** have a Google Cloud account and register your application.

## How the project is organized
The project uses [uv](https://docs.astral.sh/uv/) as its project and package manager.
The source code and the uv configuration files are located in the root directory.
The `spec` directory contains the PyInstaller specification files.

## Configuration files and how to run the project
The project use oauth2 authentication so you must download the json file with the secret key from google.
The project, to locate the secret key file, use a configuration file called `config.json` and it must be
placed where the executable is or where your main.py file is. You can run the project using an executable,
created by PyInstaller or using uv:

#### Using PyInstaller
* `gmail_cli "your gmail address"`

#### Using uv
* `uv run main.py "your gmail address"`

### Configuration file
An example of configuration file is:
```json
{
    "secret": "your secret json file.json"
}
```

## How to build an executable
#### Linux
* `uv run pyinstaller spec/gmail_cli_linux.spec`
#### Windows
* `uv run pyinstaller spec/gmail_cli_win.spec`

## Libraries
Gmail CLI uses Python >= 3.14.7 with the following libraries:

* beautifulsoup4 >= 4.15.0
* google-api-python-client >= 2.198.0
* google-auth >= 2.56.3
* google-auth-oauthlib >= 1.4.0

## Commands provided
* **listl**: List the labels in your Gmail account
* **currl**: Display the current label
* **changel**: Change the current label
* **clear**: Clear the screen
* **currp**: List the emails on the current page
* **next**: List the next page of emails in the current label
* **prev**: List the previous page of emails in the current label
* **read**: Read the selected email
* **del**: Move the selected email to Trash
* **help**: Print the help message
* **exit/quit**: Exit the terminal

## How the project works
In the main.py file there is the main function where the project start. It starts looking for your gmail address and control
if the configuration file is present. If it's present it reads use the json file with the secret key to connecto to your account.
If it's the first time you connect to the account it opens a browser page to connect. If you run the project in WSL it provides
only the web address to open with a browser.
After connected it reads the label of your gmail account and then reads the first "MAX_RES" emails of your account and start a
prompt loop to receive commands.

### files descriptions:
* config.py: in this file there are come configuration variables used in the project
* command_list.py: in this file there is the list of all the commands
* ...Command.py: theese files are the implementation of all the commands used. All the commands are class derived from the Command
  class located in Command.py. Some commands, like NextCommand are derived from ListCommand which is derived from Command.
* StateClient.py: in this file there is a class where are stored some useful informations used in all the project

