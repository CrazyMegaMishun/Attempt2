#Завдання 1
name = input()
print('Hello, ' + name + '!')

#Завдання 2
number = input('Please enter an integer number: ')
print('Next number for number ' + number + ' is ' + str(int(number) + 1) + '.')
print('Previous number for number ' + number + ' is ' + str(int(number) - 1) + '.')

#Завдання 3
v = int(input())
t = int(input())
if (v > 0) and 0 <= (v * t) <= 100:
    print(v * t)

#Завдання 4
year = int(input())
if (year % 4 == 0) and (year % 100 != 0):
    print('YES')
else:
    print('NO')

#Завдання 5
x = int(input())
if x > 0:
    print('sign(x)=1')
elif x < 0:
    print('sign(x)=-1')
else:
    print('sign(x)=0')

#Завдання 6
cortege_input = int(float(input()))
a = tuple(range(10, 101, 10))
if int(cortege_input) < 0:
    cortege_input = cortege_input * -1
    if cortege_input in a:
        print('True')
    else:
        print(False)
elif int(cortege_input) > 0:
    if cortege_input in a:
        print(True)
    else:
        print(False)
else:
    print(False)

#Завдання 7
print('Input number of stars: ')
star_number = int(input('Input number of stars: '))
print('*' * star_number)
