### Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).

def str_split(in_str, separate=' '):
    """ function which works the same as `str.split` method """
    split_list = []
    if isinstance(in_str, str):
        s = ''
        for rec in in_str:
            if rec != separate:
                s += rec
            else:
                split_list.append(s)
                s = ''
        split_list.append(s)
    else:
        print('is not a string')
    return split_list

#some_str = 'Tenet'
some_str = '"Hi Amy! Your mum sent me a text. You forgot your inhaler. Why don’t you turn your phone on?" Amy didn’t like technology'
print(some_str)
print(str_split(some_str))