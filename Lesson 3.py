#Завдання 1
print(sum(map(int, list(input()))))

#Завдання 2
x = input()
print(x[x.find('.')+1:])
print((x[x.find('.')+1:])[0])

#Завдання 3
list_ten = [10, 20, 30, 40, 50]
for i in list_ten[::-1]:
    print(i, end=' ')

#Завдання 4
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for i in list_of_six:
    if i % 5 == 0 and i < 150:
        print(i, end=' ')

#Завдання 5
import random
for i in range(3):
    x = int(input())
    if x == random.randint(1, 10):
        print('You won!')
        break
    else:
        print('You lose!')

#Завдання 6
horizontal = 'ABCDEFGH'

cell_1 = input('Please write down first cell:')
cell_2 = input('Please write down second cell:')

if (horizontal.find(cell_1[0]) - horizontal.find(cell_2[0]) == 1 or horizontal.find(cell_1[0]) - horizontal.find(cell_2[0]) == -1)\
        and int((cell_1[1])) - int(cell_2[1]) == 2 or int(cell_1[1]) - int(cell_2[1]) == -2:
    print(True)
else:
    print(False)


#Завдання 7
n = int(input())
to_fac = 1

for i in range(2, n + 1):
    to_fac *= i
print(to_fac)
