def sum_numbers(numbers=None):
    """
    Learned:
    (1) The limits of list comprehensions
    (2) correct usage of range() function
    (3) How if-else works
    (4) sum() function
    (5) basic use of pytest

    """
    result = 0
    if numbers is None:
        result = sum(range(1, 101))
    else:
        result = sum(numbers)
    return result


