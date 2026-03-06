import csv
from typing import Iterable
from lib import console
from rich import rule
from config import read_config
from display_data import display_data

def read_data(file: Iterable[str]) -> None:
    console.print("Retrieving necessary data from dataset...", style="bold")
    
    config: dict[str, str | bool] = read_config()
    csvreader = csv.DictReader(file) # Read the CSV
    genre_movie_count: int = 0 # How many movies are in the specified genre
    other_movie_count: int = 0 # How many movies are *not* in the specified genre, for use with our hypothesis
    genre_revenues: list[float] = [] # A list of all the revenues of these movies
    other_revenues: list[float] = []
    
    # Iterate through all the rows
    for row_num, row in enumerate(csvreader, start=1):
        if not row: # Empty rows are skipped, no point adding them
            console.print(f"Skipping empty row {row_num}", style="bold")
            continue

        # Debug
        if config["debug"]:
            print(row.get("genres"))

        # Limit to action movies
        if isinstance(config["genre"], str) and config["genre"].lower() in row["genres"].lower():
            genre_movie_count += 1
            if int(row["revenue"]) != 0: # Skip movies with zero revenue (or more likely missing data)
                try:
                    genre_revenues.append(float(row["revenue"]))
                except ValueError: # If this fails, e.g. conversion error
                    # Skip adding the revenue and continue on with the other movies
                    continue
        # If it's not action, we still use it for our hypothesis
        else:
            other_movie_count += 1
            if int(row["revenue"]) != 0:
                try:
                    other_revenues.append(float(row["revenue"]))
                except ValueError:
                    continue
              
    # Handle data with missing revenue by exiting, as we need this data to continue
    if not genre_revenues or not other_revenues:
        console.print(" No revenue figures were found in the data source ", style="white on red")
        exit(1)
                
    # Generic csv figures
    console.print("[bold]Total no. of rows:[/]" + " " + str(csvreader.line_num if csvreader.line_num else "[bold red]Unable to determine[/]"))
    console.print("Total movies matching criteria:", genre_movie_count, style="bold")
    console.print("Total movies not matching criteria:", other_movie_count, style="bold")

    console.print(rule.Rule(title=f"Calculated Data of {config["genre"]} Movies", end="\n"))
    console.print() # Padding

    # Function split in two for cleanliness
    display_data(genre_revenues, other_revenues)