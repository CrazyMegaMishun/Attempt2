def writer():
    with open('text.txt', 'w') as f:
        while True:
            s = input()
            if s != '':
                f.write(s + '\n')
            else:
                break


writer()
