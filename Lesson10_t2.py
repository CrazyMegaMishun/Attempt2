import re


def check_palindrome(p):
    p = re.sub('[!? \n-.,]', '', p)

    if len(p) > 1:
        mid = len(p)//2
        arr1 = p[:mid].lower()
        arr2 = p[mid:].lower()
        arr2 = arr2.replace(arr2[0], '', 1)

        if arr1 == arr2[::-1]:
            print('Паліндром')
        else:
            print('Не паліндром')


check_palindrome(input())
