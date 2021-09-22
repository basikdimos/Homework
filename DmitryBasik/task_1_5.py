### Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:
# ```
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# ```
list_dicts = [
    {"V":"S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII":"S005"},
    {"V":"S009"},
    {"VIII":"S007"},
]
print(list_dicts)
some_set = set()
for records in list_dicts:
    for key in records:
        some_set.add(records[key])
print(some_set)