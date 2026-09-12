# Gmail CLI

Gmail CLI is a simple text-based client for Gmail.

To use it, you **MUST** have a Google Cloud account and register your application.

To do this, follow these steps:

* Go to the [Google Cloud Console](https://console.cloud.google.com).
* Click **"Open project picker"** or press `Ctrl + O`. In the new screen, click **"New project"**.
* In the **"Project name"** field, enter **"Gmail CLI"** or whatever name you want, and click **"Create"**.
* Click **"Open project picker"** again and select your new project. The project picker button will now display your project name.
* In your project dashboard, in the **"Quick access"** section, you will find the **"APIs & Services"** button. You can also find it in the hamburger menu in the top-left corner. Click it, and on the new screen select **"+ Enable APIs and services"**.
  Search for **"Gmail API"** and click **"Gmail API"** to select it.
* On the next screen, click **"Enable"**.
* After clicking **"Enable"**, you will be redirected to the **"Enabled APIs & services"** page in the **"APIs & Services"** section.
* At the top right, you will see the **"Create credentials"** button. Click it.
* On the new screen, select the **"User data"** radio button and click **"Next"**. Fill in the remaining fields with your application name, email address, logo (if you want), and developer email address. Then click **"Save and continue"**.
* On the next screen, click **"Save and continue"** without making any changes to the fields.
* On the next screen, select **"Desktop application"** in the **"Application type"** field and enter the name you want for your application in the **"Name"** field.
* Click **"Create"** to create the credentials.
* You **MUST** download your credentials in JSON format. Then click the **"Done"** button.
* In the **"Credentials"** section, you will find your new Gmail API credentials.
* After creating the credentials, you must add your email address as a test user before you can use the application. To do this, click **"OAuth consent screen"** in the **"APIs & Services"** menu on the left. You will be redirected to the **Google Auth Platform**. In this section, click **"Audience"** in the menu on the left and then click **"Make external"**. Select the testing publishing status and confirm. At the bottom of the page, add your user for testing by entering your Gmail account address. You are now done.
* **Warning:** If you lose your credentials or want to create new ones, you can go to the **"Credentials"** section from the **"APIs & Services"** menu, which can be found in the hamburger menu in the top-left corner of the Google Cloud Console dashboard.

## How the project is organized

The project uses [uv](https://docs.astral.sh/uv/) as its project and package manager.

The source code and the uv configuration files are located in the root directory.

The `spec` directory contains the PyInstaller specification files.

## Configuration file

The configuration file must be named `config.json` and must contain the path to your credentials JSON file:

```json
{
    "secret": "your secret json file.json"
}
```

## How to run the project

To run the project, you must place the configuration file in the same directory as the main script (`main.py`).

Then you can run Gmail CLI using:

* `uv run main.py "your gmail address"`

Alternatively, you can use the executables available in the `dist` directory.

Again, you must place the configuration file in the same directory as the executable.

The executables are currently available only for Linux and Windows and are built with PyInstaller >= 6.22.2.

* The Linux version is built on Ubuntu 22.04.5 LTS (Jammy).
* The Windows version is built on Windows 11.

To run Gmail CLI using the executables, run:

* `gmail_cli_{os} "your gmail address"`

### How to build the executables

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
