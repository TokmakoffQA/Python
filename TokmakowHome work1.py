#Задача
#Выведите столбец чисел от start (определяется пользователем) до end.
#Найти произведение чисел

#start = int(input('Введите начально число диапазона:   ')) 
#end =  int(input('Введите конечное число диапазона:   ')) 
#prod = 1
#for num in range(start, end+1, step):
    #print(num)
    #prod *= num
#print(f"Произведение столбца чисел = {prod}")


#Задача
# распечатайте все числа, которые делятся на 3 от start до end(включительно) 
#(start, end - могут быть перепутаны), start , end- гарантируется, что целые числа 

#start = int(input('Введите начально число диапазона:   ')) 
#end =  int(input('Введите конечное число диапазона:   ')) 
#if start > end:
    #end, start = start, end
#for num in range(start, end):
    #if num % 3 == 0:
        #print ('Числа которые делятся на 3 без остатка:  ', num)


#Задача
#Дан список элементов 1, 3, 22, 7, 12, 8, 2 (могут быть какие-то другие значения, ввод данных делать не нужно)  
#1. показать каждый элемент, последняя цифра которого 2
#2. показать произведение чисел, последняя цифра которого 2

# print('Заданы числа 2,33,12,125,2,15,82,132','Числа с последней цифрой 2 -  ', sep='\n')
# for num in 2, 33, 12, 125, 2, 15, 82, 132:
#     if num % 10 == 2:
#             print(num)
# res = 1
# for num in 2, 33, 12, 125, 2, 15, 82, 132:
#     if num % 10 == 2:
#        res *= num
# print('Произведение этих чисел =    ',res)


#Задача
#Игра угадай число от 1 до 100
#реализовать подсказки (число введенное больше или меньше)
#сделать проверку на ввод числа для пользователя (может быть абсолютно любой символ)
# from random import randint
# number = randint(1 ,100)
# x = int(input('Попробуй ввести число которое я загадал...     '))
# while x != number:
#     if x < number:
#         print('Ваше число меньше')
#     elif x > number:
#         print('Ваше число больше')
#     x = int(input('Повторите попытку...   '))
# print('Вы угадали')


