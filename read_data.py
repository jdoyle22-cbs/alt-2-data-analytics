from colorama import Fore, Back, Style
import csv
from lib import bold, mode

def read_data(file: File) -> None:
    print(Style.BRIGHT + "Retrieving necessary data from dataset..." + Style.RESET_ALL)
    csvreader = csv.reader(file, delimiter=',') # Read the CSV
    rows = []
    movie_count: int = 0
    revenues: list = []
    
    for row_num, row in enumerate(csvreader, start=1):
        if not row:
            print(f"Skipping empty row {row_num}")
            continue
        if 21 < len(row):
            print(f"Row {row_num}, Column {21}: {row[21]}")
            if "Action" in row[21]: # Only look at action movies
                movie_count += 1
                rows.append(row)
                revenues.append(row[7])
        else:
            print(f"Row {row_num} has only {len(row)} columns, skipping.")
            break
    print("Total movies matching criteria:", movie_count)

    print(bold("\n-------------------- Retrieved Data --------------------\n"))
    print(bold("Total no. of rows:") + " " + str(csvreader.line_num if csvreader.line_num else "Unable to determine"))
    print(mode(revenues))