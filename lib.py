from colorama import Style, Back
from collections import Counter
        
"""
Return the mode of a list of numbers
"""
def mode(data: list[int | float]) -> int | float:
    # Make sure we actually have data to use
    if not data:
        raise ValueError("Cannot compute mode of empty list")
    
    cnt = Counter(data)
    return cnt.most_common(1)[0][0]

"""
Return the median value of a list of number values
"""
def median(data: list[int | float]) -> int | float:
    n: int = len(data)
    is_even: bool = (n % 2) == 0
    
    if not data or n == 0: # If there's no data
        raise ValueError("Cannot compute median of empty list")
    
    data.sort() # Needs to be sorted for median calculation
    
    # If odd, then return the middle data value
    if not is_even:
        return data[n // 2]
    else:
        return (data[(n // 2) - 1] + data[(n // 2)]) / 2

"""
Return the mean value of a list of number values
"""
def mean(data: list[int | float]) -> int | float:
    n: int = len(data)
    
    if not data or n == 0: # If there's no data
        raise ValueError("Cannot compute mean of empty list")
    
    # Calculating mean is very simple
    # Sum of values divided by number of values
    return sum(data) / (n)

# Terminal styling

def bold(message: str):
    return(Style.BRIGHT + message + Style.RESET_ALL)

def error(message: str):
    return(Style.BRIGHT + Back.RED + " " + message + " " + Style.RESET_ALL)

def success(message: str):
    return(Style.BRIGHT + Back.GREEN + " " + message + " " + Style.RESET_ALL)