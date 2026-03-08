from chardet import DetectionDict

from download import download_data
from sys import exit
from read_data import read_data
from lib import console, UserTerminationError, detect_encoding
from config import read_config
from os.path import isfile

config: dict[str, str | bool] = read_config()
genre: str = str(config["genre"])

# Welcome message
console.print(
    f"""
   _   _  _____ ___ 
  /_\\ | ||_   _|_  )
 / _ \\| |__| |  / / 
/_/ \\_\\____|_| /___|

========================================
Data Analytics
========================================

Hypothesis: {genre} movies make the most money out of any genre

""",
    style="bold",
)

data_download_result = download_data()  # Prompt user to redownload data if they wish

if not data_download_result[0] and data_download_result[1] != "":
    console.print("Exiting due to error...", style="bold white on red")
    exit(0)

console.print("Reading data file...", style="bold")

# Attempt to write to file, handling errors
try:
    file_path: str = f"./data/{config['data_filename'] or 'tmdb_5000_movies'}.csv"

    # Make sure that FileNotFound always occurs when the file doesn't exist
    if not isfile(file_path):
        raise FileNotFoundError

    encoding: DetectionDict = detect_encoding(file_path)
    # From Chardet documentation:
    #   chardet returns None when the data appears to be binary rather than text.
    #   This happens when the data contains null bytes or a high proportion of control characters that don’t match any known text encoding.
    # i.e., check if the file is actually valid
    if encoding["encoding"] is None:
        console.print(
            "[bold white on red]Dataset file appears to be invalid - cannot determine encoding, likely due to data corruption.[/]"
        )
        exit(1)

    with open(
        file_path,
        "r",  # No writing to the file
        encoding=encoding["encoding"],
    ) as file:
        read_data(file)
# If the file doesn't exist
except FileNotFoundError:
    console.print(
        "Dataset file could not be found. Make sure it exists in the directory",
        style="bold white on red",
    )
# If the file has failed to be read, e.g. incorrect filesystem permissions, another program is using it etc.
except IOError as e:
    # Show more detailed error messages if debug variable is set
    # No need to confuse the end user
    if config["debug"]:
        console.print(
            "Fatal error while reading file:", str(e), style="bold white on red"
        )

    # More user-friendly information
    console.print("The file could not be read.", style="bold yellow")
    console.print(
        "1. Does it contain data? It may have failed to download correctly.",
        style="bold yellow",
    )
    console.print("2. Is it being used by another program?", style="bold yellow")
    console.print(
        "3. Does this program have the correct filesystem permissions to access it?",
        style="bold yellow",
    )
except UserTerminationError:
    exit(0)  # Not actually an error, so code 0
# Catch any other unhandled exception
except Exception:
    console.print_exception(show_locals=True)
    exit(1)
