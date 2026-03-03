import csv
from lib import mode, median, mean
from typing import Iterable
from lib import console
from rich import rule
from rich.prompt import Confirm
import matplotlib.pyplot as plt # pyright: ignore[reportMissingTypeStubs]
from config import read_config

config = read_config()

def read_data(file: Iterable[str]) -> None:
    console.print("Retrieving necessary data from dataset...", style="bold")
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

        # Limit to action movies
        if config["genre"] in row["genres"].lower():
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
                
    console.print("[bold]Total no. of rows:[/]" + " " + str(csvreader.line_num if csvreader.line_num else "[bold red]Unable to determine[/]"))
    console.print("Total movies matching criteria:", genre_movie_count, style="bold")
    console.print("Total movies not matching criteria:", other_movie_count, style="bold")

    console.print(rule.Rule(title=f"Calculated Data of {config["genre"]} Movies", end="\n"))
    console.print()

    # Genre Variables
    genre_mode_result = mode(genre_revenues)
    genre_median_result = median(genre_revenues)
    genre_mean_result = mean(genre_revenues)

    console.print(f"[bold]{config["genre"]} Movies - Revenue Mode:[/]", genre_mode_result)
    console.print(f"[bold]{config["genre"]} Movies - Median Revenue:[/]", genre_median_result)
    console.print(f"[bold]{config["genre"]} Movies - Mean Revenue:[/]", genre_mean_result)
    console.print()
    show_genre_graph = Confirm.ask("[bold]Show a graph of this data?[/]")
    if show_genre_graph == True:
        print() # Padding
        # Create bar chart
        plt.bar(["Mode", "Median", "Mean"], [genre_mode_result, genre_median_result, genre_mean_result])
        plt.ylim(100000, 200000000)
        plt.xlabel('Categories')
        plt.ylabel('Revenue (hundred millions) (US Dollars)')
        plt.title(f'{config["genre"]} Movies - Revenue Statistics')
        plt.show()

    # Other Movie Variables
    other_mode_result = mode(other_revenues)
    other_median_result = median(other_revenues)
    other_mean_result = mean(other_revenues)

    console.print(f"[bold]Non-{config["genre"]} Movies - Revenue Mode:[/]", other_mode_result)
    console.print(f"[bold]Non-{config["genre"]} Movies - Median Revenue:[/]", other_median_result)
    console.print(f"[bold]Non-{config["genre"]} Movies - Mean Revenue:[/]", other_mean_result)
    console.print()
    show_genre_graph = Confirm.ask("[bold]Show a graph of this data?[/]")
    if show_genre_graph == True:
        print() # Padding
        # Create bar chart
        plt.bar(["Mode", "Median", "Mean"], [other_mode_result, other_median_result, other_mean_result])
        plt.ylim(100000, 200000000)
        plt.xlabel('Categories')
        plt.ylabel('Revenue (hundred millions) (US Dollars)')
        plt.title(f'Non-{config["genre"]} Movies - Revenue Statistics')
        plt.show()

    show_combined_graph = Confirm.ask("[bold]Show a combined graph of all data?[/]")
    if show_combined_graph == True:
        plt.bar(
            [
                f"{config["genre"]} Mode", f"Non{config["genre"]} Mode", 
                f"{config["genre"]} Median", f"Non{config["genre"]} Median",
                f"{config["genre"]} Mean", f"Non{config["genre"]} Mean",
            ], 
            [
                genre_mode_result, other_mode_result, 
                genre_median_result, other_median_result,
                genre_mean_result, other_mean_result
            ]
        )