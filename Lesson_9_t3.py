def longest_word():
    return max(list(input().split(sep=' ')), key=len)


print(longest_word())
