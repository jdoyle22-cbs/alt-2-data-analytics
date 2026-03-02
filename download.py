from lib import error, success, bold
import kagglehub # pyright: ignore[reportMissingTypeStubs] Ignored as it doesn't really matter, and adding them clogs up the main folder

"""
Downloads the dataset from Kaggle
"""
def download_data() -> list[bool | str]:
    # Make sure the user wants to do this, as it's wasteful if not needed
    while choice := input(bold("Download the dataset from Kaggle? [Y/N]: ")).lower():
        if choice == "n":
            # Skip if user doesn't want to
            return [False, ""]
        elif choice == "y":
            try:
                path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata", output_dir="./data")
                print(bold("Path to dataset files:"), path)
            except Exception as e:
                return [False, error("The following error occurred: " + str(e))]
            
            return [True, success("File was successfully downloaded.")]
        else:
            # If it's an invalid choice, ask again
            continue
    
    # If we've got to this point, return an error because something has gone very wrong
    return [False, error("Something went wrong.")]
