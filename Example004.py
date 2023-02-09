#Вычислить число c заданной точностью d
import math

d = input('Введите степень округления ')
d = d[2:len(d)]
print(round(math.pi,len(d)))
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input("Введите число: "))
i = 2 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} : {lst}")
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")
#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)
def rnd():
    return random.randint(0, 101)
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr
k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')
with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()
with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()
print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2
with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')