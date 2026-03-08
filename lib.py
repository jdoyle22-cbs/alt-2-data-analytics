from collections import Counter
from rich.console import Console
import chardet

# Rich Console
console = Console()

"""
Return the mode of a list of numbers
"""


def mode(data: list[int | float], check_data_validity: bool = False) -> int | float:
    # Make sure we actually have data to use
    if not data:
        raise ValueError("Cannot compute mode of empty list")

    # Make sure all data values are numbers
    if check_data_validity:
        for i in data:
            try:
                float(i)
            except Exception:
                raise ValueError("Encountered value that is not a number in the list")

    cnt = Counter(data)
    return cnt.most_common(1)[0][0]


"""
Return the median value of a list of number values
"""


def median(data: list[int | float]) -> int | float:
    n: int = len(data)
    is_even: bool = (n % 2) == 0

    if not data or n == 0:  # If there's no data
        raise ValueError("Cannot compute median of empty list")

    data.sort()  # Needs to be sorted for median calculation

    # If odd, then return the middle data value
    if not is_even:
        return data[n // 2]
    else:
        return (data[(n // 2) - 1] + data[(n // 2)]) / 2


"""
Return the mean value of a list of number values
"""


def mean(data: list[int | float], check_data_validity: bool = False) -> int | float:
    n: int = len(data)

    if not data or n == 0:  # If there's no data
        raise ValueError("Cannot compute mean of empty list")

    if check_data_validity:
        for i in data:
            try:
                float(i)
            except Exception:
                raise ValueError("Encountered value that is not a number in the list")

    # Calculating mean is very simple
    # Sum of values divided by number of values
    return sum(data) / (n)


# Custom Error
class UserTerminationError(KeyboardInterrupt):
    def __init__(self, value):
        self.value = value
        message = "User terminated program execution."
        super().__init__(message)


# Check CSV encoding
def detect_encoding(filepath: str):
    with open(filepath, "rb") as f:
        result = chardet.detect(f.read())
        return result
