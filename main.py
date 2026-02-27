from download import download_data
import sys
import csv

# Handle CLI arguments
filename: str = "movies"
try:
   filename: str = sys.argv[1] if sys.argv[1] else "movies" # Default to movies if custom filename not specified
except IndexError:
   filename: str = "movies"

# Welcome message
print(
"""
   _   _  _____ ___ 
  /_\\ | ||_   _|_  )
 / _ \\| |__| |  / / 
/_/ \\_\\____|_| /___|

========================================
Data Analytics
========================================

Hypothesis: Action films make the most money out of any genre

"""
)

download_data(filename) # Prompt user to redownload data if they wish

def main_loop(file: File) -> None:
   print("Retrieving necessary data from dataset...")
   csvreader = csv.reader(file)
   
   fields = next(csvreader)
   for row in csvreader:
      rows.append(row)

   print("Total no. of rows: %d" % csvreader.line_num)

print("\nReading data file...")

# Attempt to write to file, handling errors
try:
   with open(f"{filename if filename else "movies"}.csv", "r") as file:
      if len(file) == 0: # Handle errors where the file is empty, e.g. HTTP based errors
         raise IOError
      main_loop(file)
except IOError:
   print("The file could not be read.")
   print("1. Does it exist? Make sure it has been downloaded at least once.")
   print("2. Does it contain data? It may have failed to download correctly.")
   print("2. Is it being used by another program?")
   print("3. Does this program have the correct filesystem permissions to access it?")
except Exception as e:
   print("The following error occurred: ", str(e))