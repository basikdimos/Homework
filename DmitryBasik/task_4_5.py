### Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
# Example:
# ```python
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```

def split_by_index(num: int):
    """ Function which get in int and return tuple of digits"""
    num_str = str(num)
    num_list = []
    for rec in num_str:
        num_list.append(int(rec))
    return tuple(num_list)

print(split_by_index(87178291199))