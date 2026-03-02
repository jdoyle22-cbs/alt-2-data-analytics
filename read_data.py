from colorama import Style
import csv
from lib import bold, mode
from typing import Iterable

def read_data(file: Iterable[str]) -> None:
    print(Style.BRIGHT + "Retrieving necessary data from dataset..." + Style.RESET_ALL)
    csvreader = csv.DictReader(file, delimiter=',') # Read the CSV
    movie_count: int = 0 # How many movies are in the specified genre
    revenues: list[float] = [] # A list of all the revenues of these movies
    
    for row_num, row in enumerate(csvreader, start=1):
        if not row:
            print(f"Skipping empty row {row_num}")
            continue

        if "Action" in row["genres"]: # Only look at action movies
            movie_count += 1
            revenues.append(float(row["revenue"]))
    print("Total movies matching criteria:", movie_count)

    print(bold("\n-------------------- Retrieved Data --------------------\n"))
    print(bold("Total no. of rows:") + " " + str(csvreader.line_num if csvreader.line_num else "Unable to determine"))
    print(mode(revenues))