def element_mover(s, num):
    s += s[0:num]
    s = s.replace(s[0:num], '', 1)
    print(s)


element_mover(input(), int(input()))
