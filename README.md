# alt-2-data-analytics
Repository for LCCS ALT 2 - Data Analytics

## Setup

**1.** **If you wish to use the automatic dataset downloader, do the following:** Create a folder called `.kaggle` in the root directory, with your Kaggle access token inside a file called `access_token`.
   
> [!Note]
> Make sure the file has no extension. *On Windows, you may have to toggle the option in File Explorer properties to see file extensions, after which you can delete the extension (including the dot) and ignore the warning. If Windows detects it as just a generic `File` type, then it is correct.*

**2.** Adjust the config to your liking in `config.ini`. Explanations of the settings are provided in the file.

**3.** Start the program and download the dataset if necessary. If you don't, the program cannot run as it has no data to work with and will not fetch it without your confirmation to do so.

**4.** The program should work normally and provide you statistics.

## Usage

[Create a virtual enviroment](https://docs.python.org/3/library/venv.html), activate it, install the packages, and run the script:

```bash
# Assuming venv is created (see link above)
$ cd .venv/Scripts
$ # Powershell
$ .\activate.ps1
$ # Command Prompt
$ activate.bat
$ # Bash
$ activate.fish

$ # If successful, you should see .venv in brackets on the left, e.g. (.venv)
$ (.venv) pip install -r requirements.txt
  ...
$ # You should see no errors if installation has worked correctly
$ # Run the script
$ (.venv) python main.py
   _   _  _____ ___ 
  /_\ | ||_   _|_  )
 / _ \| |__| |  / / 
/_/ \_\____|_| /___|

========================================
Data Analytics
========================================

Hypothesis: Action films make the most money out of any genre


Download the dataset from Kaggle? [y/n]:
```

You can edit the `config.ini` file to change the parameters. For example, you can change the genre to "Romance" instead of "Action".

```ini
[general]
genre = "Romance" # Capitals don't matter, but spelling does
```

## Development

The program can be checked by the linter by running `ruff check`.

Tests can be run by running `python tests/{name}.py`, where `{name}` is the filename of the file you wish to run, e.g. `python tests/maths.py`.
