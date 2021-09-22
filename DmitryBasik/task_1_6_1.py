### Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```
some_tuple = (1, 2, 3, 4)
s = ''
for rec in some_tuple:
    s += str(rec)
some_int = int(s)
print(some_int)