import re


def check_palindrome(p):
    p = (re.sub('[!? \n-.,—]', '', p).lower())
    if p.split(sep=p[len(p)//2:])[0] == p.split(sep=p[:len(p)//2])[1].replace(p[len(p)//2], '', 1)[::-1]:
        print('Базований паліндром')
    else:
        print('Не паліндром')


check_palindrome(input())
