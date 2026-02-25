import download_data from download
import sys

# Handle CLI arguments
filename: str = sys.argv[1] if sys.argv[1] else "movies" # Default to movies if custom filename not specified

# Welcome message
print(
"""
   _   _  _____ ___ 
  /_\ | ||_   _|_  )
 / _ \| |__| |  / / 
/_/ \_\____|_| /___|

========================================
Data Analytics
========================================

"""
)

download_data(filename) # Prompt user to redownload data if they wish

def main_loop(file: File):
   print("TBD")

print("Reading data file...")

# Attempt to write to file, handling errors
try:
   with open(f"{filename if filename else "movies"}.csv", "w") as file:
      main_loop(file)
except IOError:
   print("The file could not be read. Is it being used by another program?")
except Exception as e:
   print("The following error occurred: ", e)