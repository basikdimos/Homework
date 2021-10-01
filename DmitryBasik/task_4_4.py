### Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("no luck", [42])
# ["no luck"]
# ```

def split_by_index(in_str, indexes=[]):
    """ split string by indexes """
    split_list = []
    count = 0
    if isinstance(in_str, str):
        for rec in indexes:
            if rec >= len(in_str):
                break
            elif rec < len(in_str):
                split_list.append(in_str[count:rec])
                count = rec
        if count < len(in_str):
            split_list.append(in_str[count:])
    else:
        print('is not a string')
    return split_list

#some_str = '"Hi Amy! Your mum sent me a text. You forgot your inhaler. Why don’t you turn your phone on?" Amy didn’t like technology'
some_str = "pythoniscool,isn'tit?"
some_indexes = [6, 8, 12, 13, 18, 42]
print(some_str)
print(split_by_index(some_str, some_indexes))
some_str = "no luck"
some_indexes = [42]
print(some_str)
print(split_by_index(some_str, some_indexes))