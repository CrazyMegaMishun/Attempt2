name = input()
print('Hello, ' + name + '!')

number = input()
print('Please enter an integer number: ' + number)
print('Next number for number ' + number + ' is ' + str(int(number)+1) + '.')
print('Previous number for number ' + number + ' is ' + str(int(number)-1) + '.')

v = int(input())
t = int(input())
if (v > 0) and 0 <= (v * t) <= 100:
    print(v*t)

year = int(input())
if(year % 4 == 0) and (year % 100 != 0):
    print('YES')
else:
    print('NO')

