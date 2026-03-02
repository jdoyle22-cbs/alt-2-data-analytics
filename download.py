import requests
from colorama import Style, Back

"""
Downloads the dataset from Kaggle and writes to the specified file
"""
def download_data(filename: str = "movies") -> list[bool | str]:
    # Make sure the user wants to do this, as it's wasteful if not needed
    if input(Style.BRIGHT + "Download the dataset from Kaggle? [Y/N]: " + Style.RESET_ALL).lower() == "n":
        return [False, ""]

    # Taken from inspecting Kaggle's network calls
    url = "https://storage.googleapis.com/kagglesdsdata/datasets/9514028/14871842/movies.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260224%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260224T124743Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6dfe05499d30dec6d1d298be974b52647bc73bf9f151abb3ff5a352f03d49452d520810460c58cd02d2645009d63fdb1837ecb919a4aa42c69ae1567f287494e7c446d92db1419d9fd25928f72452e3831cb6153ac4b42b1d3f071eeb3123421e7238deb1f3543a5a160bce8ead9d26cb8fdf0fa01b1faae25ac0bdb19cb2356a0ea63db3b2af265ab41a642c7f681f91358dc3180dc1dba725ba7eadb7d366fd183e2516f5260e169b92edb8770f48ad89dea3f10501a6e389b63da995094f4c8311db771dc67ebdf47c51d1166e0748706046714ca1838985d30a6a25529fe36c16a6bd1d832c299c026da64041b17947b316db0598cb8edbf052cde909914"

    response = requests.get(url)
    if response.status_code != 200:
        print(Style.BRIGHT + Back.RED + "HTTP Status code: " + str(response.status_code) + Style.RESET_ALL)
        return [False, Style.BRIGHT + Back.RED + "Error while attempting to retrieve dataset from URL, cancelling..." + Style.RESET_ALL]

    # Attempt to write to file, handling errors
    try:
        with open(f"{filename if filename else "movies"}.csv", "w") as file:
            file.write(str(response.content))
        return [True, Style.BRIGHT + Back.RED + "Data successfully downloaded." + Style.RESET_ALL]
    except IOError:
        return [False, Style.BRIGHT + Back.RED + "The file could not be written to. Is it being used by another program?" + Style.RESET_ALL]
    except Exception as e:
        return [False, Style.BRIGHT + Back.RED + "The following error occurred: " + str(e) + Style.RESET_ALL]
