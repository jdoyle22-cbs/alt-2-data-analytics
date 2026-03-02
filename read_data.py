import csv
from lib import mode, median, mean
from typing import Iterable
from lib import console
from rich import rule

def read_data(file: Iterable[str]) -> None:
    console.print("Retrieving necessary data from dataset...", style="bold")
    csvreader = csv.DictReader(file, delimiter=',') # Read the CSV
    movie_count: int = 0 # How many movies are in the specified genre
    revenues: list[float] = [] # A list of all the revenues of these movies
    
    # Iterate through all the rows
    for row_num, row in enumerate(csvreader, start=1):
        if not row: # Empty rows are skipped, no point adding them
            console.print(f"Skipping empty row {row_num}", style="bold")
            continue

        # Limit to action movies
        if "Action" in row["genres"]:
            movie_count += 1
            if int(row["revenue"]) != 0: # Skip movies with zero revenue (or more likely missing data)
                try:
                    revenues.append(float(row["revenue"]))
                except ValueError: # If this fails, e.g. conversion error
                    # Skip adding the revenue and continue on with the other movies
                    continue
                
    console.print("[bold]Total no. of rows:[/]" + " " + str(csvreader.line_num if csvreader.line_num else "[bold red]Unable to determine[/]"))
    console.print("Total movies matching criteria:", movie_count, style="bold")

    console.print(rule.Rule(title="Calculated Data", end="\n"))
    console.print()
    console.print("[bold]Revenue Mode:[/]", mode(revenues))
    console.print("[bold]Median Revenue:[/]", median(revenues))
    console.print("[bold]Mean Revenue:[/]", mean(revenues))