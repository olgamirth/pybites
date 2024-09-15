def sum_numbers(numbers=None):
    result = 0
    if numbers is None:
        result = sum(range(1, 100))
    else:
        result = sum(numbers)
    return result


