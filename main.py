from download import download_data
import sys
from read_data import read_data
from lib import console
from logger import log
from config import read_config

config: dict[str, str | bool] = read_config()
genre: str = str(config["genre"]).strip().replace('"', "")

# Handle CLI arguments
filename: str = "tmdb_5000_movies"
try:
    filename: str = (
        sys.argv[1] if sys.argv[1] else "tmdb_5000_movies"
    )  # Default to 'tmdb_5000_movies' if custom filename not specified
except IndexError:
    filename: str = "tmdb_5000_movies"

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
    sys.exit(0)

console.print("Reading data file...", style="bold")

# Attempt to write to file, handling errors
try:
    # Encoding (UTF-8) *has* to be specified for Python to work with it
    with open(
        f"./data/{filename if filename else 'tmdb_5000_movies'}.csv",
        "r",
        encoding="utf-8",
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
    log.error(
        "[bold red]Fatal error while reading dataset file[/]", extra={"markup": True}
    )
    console.print("Fatal error while reading file:", str(e), style="bold white on red")
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
# Catch any other unhandled exception
except Exception:
    log.error(
        "[bold red]Fatal error due to unhandled exception[/]", extra={"markup": True}
    )
    console.print_exception(show_locals=True)
