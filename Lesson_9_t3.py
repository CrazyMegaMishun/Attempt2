def longest_word() -> str:
    return max(list(input().split(sep=' ')), key=len)


print(longest_word())
