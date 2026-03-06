import kagglehub # pyright: ignore[reportMissingTypeStubs] Ignored as it doesn't really matter, and adding them clogs up the main folder
from rich.prompt import Confirm
from sys import exit
from lib import console

"""
Downloads the dataset from Kaggle
"""
def download_data() -> tuple[bool, str]:
    # Exception handler to catch keyboard interrupts (CTRL+C)
    try:
        # Make sure the user wants to do this, as it's wasteful if not needed
        choice = Confirm.ask("[bold]Download the dataset from Kaggle?[/]")
        if choice == False:
            # Skip if user doesn't want to
            return (False, "")
        elif choice == True:
            try:
                # Use Kaggle's library to download it
                path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata", path="tmdb_5000_movies.csv", output_dir="./data")
                console.print(f"Path to dataset files: {path}", style="bold")
            except Exception as e:
                return (False, "The following error occurred: " + str(e))
                
            return (True, "File was successfully downloaded.")
        
        # If we've got to this point, return an error because something has gone very wrong
        return (False, "Something went wrong.")
    except KeyboardInterrupt:
        console.print("\nTerminating program due to keyboard interrupt...", style="bold yellow")
        exit(-1)
