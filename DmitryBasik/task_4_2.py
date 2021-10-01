### Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

def is_palindrome(in_str):
    """ check str is a palindrome """
    if isinstance(in_str, str):
        in_str = in_str.lower()
        i = 0
        k = len(in_str)-1
        flag = 'is a palindrome'
        while i <= k:
            if in_str[i] != in_str[k]:
                flag = 'is not a palindrome'
                break
            else:
                i += 1
                k -=1
    else:
        flag = 'is not a string'
    print (flag)
    return

check_str = 'Tenets'
is_palindrome(check_str)