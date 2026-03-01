from download import download_data
import sys
import csv
import os
from colorama import just_fix_windows_console, Fore, Back, Style

# Make ANSI color codes work in windows
just_fix_windows_console()

# Handle CLI arguments
filename: str = "movies"
try:
   filename: str = sys.argv[1] if sys.argv[1] else "movies" # Default to movies if custom filename not specified
except IndexError:
   filename: str = "movies"

# Welcome message
print(Style.BRIGHT +
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
+ Style.RESET_ALL)

data_download_result = download_data(filename) # Prompt user to redownload data if they wish

if data_download_result[0] == False and data_download_result[1] != "":
   print(Back.RED + Style.BRIGHT + "Exiting due to error..." + Style.RESET_ALL)
   sys.exit(0)

def main_loop(file: File) -> None:
   print(Style.BRIGHT + "Retrieving necessary data from dataset..." + Style.RESET_ALL)
   csvreader = csv.reader(file) # Read the CSV
   rows = []
   
   fields = next(csvreader)
   for row in csvreader:
      if "Action" in row[21]: # Only look at action movies
         rows.append(row)

   print(Style.BRIGHT + "\n-------------------- Retrieved Data --------------------\n" + Style.RESET_ALL)
   print(Style.BRIGHT + Back.WHITE + Fore.BLACK + "Total no. of rows:" + Style.RESET_ALL + " " + str(csvreader.line_num))
   print(Style.BRIGHT + Back.WHITE + Fore.BLACK + "Field names:" + Style.RESET_ALL + " " + ", ".join(fields))

   print(Style.BRIGHT + Back.WHITE + Fore.BLACK + '\nFirst 5 rows are:\n' + Style.RESET_ALL)

print(Style.BRIGHT + "\nReading data file..." + Style.RESET_ALL)

# Attempt to write to file, handling errors
try:
   # Encoding (UTF-8) *has* to be specified for Python to work with it
   with open(f"{filename if filename else "movies"}.csv", "r", encoding="utf-8") as file:
      main_loop(file)
except FileNotFoundError:
   print(Style.BRIGHT + Back.RED + "Dataset file could not be found. Make sure it exists in the directory" + Style.RESET_ALL)   
except IOError as e:
   print(Style.BRIGHT + Back.RED + "Fatal error while reading file:", str(e))
   print("The file could not be read.")
   print("1. Does it contain data? It may have failed to download correctly.")
   print("2. Is it being used by another program?")
   print("3. Does this program have the correct filesystem permissions to access it?" + Style.RESET_ALL)
except Exception as e:
   print(Style.BRIGHT + Back.RED + "The following error occurred:" + Style.RESET_ALL, Fore.RED + str(e) + Style.RESET_ALL)