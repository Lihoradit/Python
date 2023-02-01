'''#1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
b = input("Введите число: ")

def result(b):                           
    if float(b) < 0:                            
        b = b%10
    number = 0

    for i in str(b):
        if i != '.':
            number += int(i)
    return number

   
print(f"Сумма чисел равна {result(b)}")
#2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
a = int(input("Введите число: "))
def sum(a):
    result=1
    for i in range(a):
        i+=1
        result*=i
        print(f"{result},")
sum(a)'''
#На столе лежат n монеток. Некоторые из них лежат вверх
#решкой, а некоторые – гербом. Определите минимальное число
#монеток, которые нужно перевернуть, чтобы все монетки были
#повернуты вверх одной и той же стороной. Выведите минимальное
#количество монет, которые нужно перевернуть.
import random
coin= int(input("Введите количество монет: "))
rand_list=[]
n=coin
for i in range(n):
    rand_list.append(random.randint(0,1))
print(rand_list) 
heads=int()
tails=int()
for i in range(len(rand_list)):
    if rand_list[i]==1:
        heads= heads+1
    elif rand_list[i]==0:
        tails= tails+1
if heads<tails:
    print(f"Переверните Орел {heads} раз")
elif tails<heads:
    print(f"Переверните Решку {tails} раз ")
elif tails==heads:
    print(f"Монеты выпали поровну на орел и решка, вы счастливчик :)")
