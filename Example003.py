#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
user_num= list(map(float, input("Введите числа через пробел: ").split()))
def SumOddPos(num):
    result=int()
    for i in range(0, len(user_num), 2):
        result+= user_num[i]
    return result
print(SumOddPos(user_num))
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
def SumFirstNLastPos(num):
    temp =int(0)
    for i in range(len(num)):
        print(num[i]+ num[(len(num)-1)-temp])
        temp=temp+1
        if temp > (len(num)-1)/2: break
SumFirstNLastPos(user_num)
#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
size= int(input("Введите размер списка: "))
rand_list=[]
for i in range(size):
    rand_list.append(round(random.random(),2))
print(rand_list)
def MinMaxDifference(list):
    max=float(0)
    min=float(1)
    for i in range(len(list)):
        if rand_list[i]> max:
            max =rand_list[i]
        elif rand_list[i]< min:
            min= rand_list[i]
    dif= max-min
    return dif
print(MinMaxDifference(rand_list))
#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input("Введите число: "))
def BinaryConvert(n):
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n //= 2
    print(s)
BinaryConvert(n)
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input("Введите число: "))

def Fib(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = Fib(n)
print(Fib(n))
print(fibo_nums.index(0))