from colorama import Style, Back
from collections import Counter

#def mode(data: list[int | float]) -> int | float:
#    # Make sure we actually have data to use
#    if not data:
#        raise ValueError("Cannot compute mode of empty list")
#    
#    stored_values: dict[int | float, int] = {}
#
#    try:
#        for value in data:
#            stored_values[value] = stored_values.get(value, 0) + 1
#            
#        return max(stored_values, key=stored_values.get)
#    except Exception as e:
#        print(error(str(e)))
#        exit(-1)
        
def mode(data: list[int | float]) -> int | float:
    # Make sure we actually have data to use
    if not data:
        raise ValueError("Cannot compute mode of empty list")
    
    cnt = Counter(data)
    return cnt.most_common(1)[0][0]

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

def success(message: str):
    return(Style.BRIGHT + Back.GREEN + " " + message + " " + Style.RESET_ALL)