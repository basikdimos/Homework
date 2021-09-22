### Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']
# ```

some_str = 'red,white,black,rеd,green,black'
some_list = some_str.split(',')
print(some_list)
unique_list = []
for rec in some_list:
    if rec not in unique_list:
        unique_list.append(rec)
print(sorted(unique_list))