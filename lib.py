from colorama import Style, Fore, Back

def mode(data: list):
    stored_values: dict[int, int] = {}

    try:
        for value in data:
            current_index = stored_values[value] if stored_values[value] else 0 # Make sure there is a value
            stored_values.update({ value: current_index })

        max_key = max(stored_values, key=stored_values.get)
        return max_key
    except Exception as e:
        print(error(str(e)))

def median(data: list):
    print("TBD")

def mean(data: list):
    print("TBD")

# Terminal styling

def bold(message: str):
    return(Style.BRIGHT + message + Style.RESET_ALL)

def error(message: str):
    return(Style.BRIGHT + Back.RED + " " + message + " " + Style.RESET_ALL)