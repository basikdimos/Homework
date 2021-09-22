### Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

from datetime import time

#some_str = "Some string for test"
some_str = """Some string for test
              Some text one
              Some text two
              Some text three
           """
some_str = some_str*10000000
print('Length string with rfind; ', some_str.rfind(some_str[-1])+1)
# time execute:
# Length string with rfind;  20
# python3.9 task_1_1.py  0,01s user 0,01s system 96% cpu 0,020 total
# Length string with rfind;  118
# python3.9 task_1_1.py  0,03s user 0,01s system 97% cpu 0,045 total
# Length string with rfind;  200000000
# python3.9 task_1_1.py  0,06s user 0,08s system 99% cpu 0,134 total
# Length string with rfind;  1180000000
# python3.9 task_1_1.py  0,19s user 0,38s system 99% cpu 0,571 total

#count = 0
#for i in some_str:
#    count += 1
#print('Length string with loop: ',count)
# time execute:
# Length string with loop:  20
# python3.9 task_1_1.py  0,03s user 0,01s system 97% cpu 0,043 total
# Length string with loop:  118
# python3.9 task_1_1.py  0,03s user 0,01s system 98% cpu 0,042 total
# Length string with loop:  200000000
# python3.9 task_1_1.py  13,59s user 0,07s system 99% cpu 13,666 total
# Length string with loop:  1180000000
# python3.9 task_1_1.py  72,21s user 0,33s system 99% cpu 1:12,59 total