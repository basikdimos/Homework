### Task 1.4
# Write a Python program to sort a dictionary by key.
some_dict = {
    'Aulonocara': 1,
    'Melanochromis': 1,
    'Labeotropheus': 3,
    'Pseudotropheus': 4,
    'Apistogramma': 2,
}
print(some_dict)
sorted_dict = {}
for key in sorted(some_dict):
    sorted_dict[key] = some_dict[key]
print(sorted_dict)