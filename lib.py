from colorama import Style, Back
from sys import exit

def mode(data: list[int | float]) -> int | float:
    stored_values: dict[int | float, int] = {}

    try:
        for value in data:
            current_index = stored_values[value] if stored_values[value] else 0 # Make sure there is a value
            stored_values.update({ value: current_index })
            
        # Quick wrapper to satisfy the typing system that a value is always present
        def get_from_dict(key: int | float) -> int:
            v: int = stored_values.get(key)
            assert v is not None
            return v

        max_key: int | float = max(stored_values, key=get_from_dict)
        return max_key
    except Exception as e:
        print(error(str(e)))
        exit(-1)

def median(data: list[int | float]) -> int | float:
    print("TBD")
    return -1

def mean(data: list[int | float]) -> int | float:
    print("TBD")
    return -1

# Terminal styling

def bold(message: str):
    return(Style.BRIGHT + message + Style.RESET_ALL)

def error(message: str):
    return(Style.BRIGHT + Back.RED + " " + message + " " + Style.RESET_ALL)