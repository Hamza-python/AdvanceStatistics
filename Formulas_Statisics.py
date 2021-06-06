import statistics
from collections import Counter


# Calculate Mean in python Function.

def Mean(lst):
    mean = sum(lst) / len(lst)
    return mean


# Calculate Mean using Statistics.
list1 = [1, 3, 5, 7, 9, 5, 5]
statistics.mean(list1)


# Calculate Median using python function.
def Median(lst):
    n = len(lst)
    index = n // 2
    # List with an odd number of Observation.
    if n % 2:
        return sorted(lst)[index]
    # List with a even number of observations.
    return sum(sorted(lst)[index - 1:index + 1]) / 2


# Calculate Median using Statistics.
statistics.median(list1)


# Calculate MOde using function.
def Mode(lst):
    c = Counter(lst)
    return [k for k, v in c.items()
            if v == c.most_common(1)[0][1]]


# Calculate Using Statistics.
statistics.mode(list1)
