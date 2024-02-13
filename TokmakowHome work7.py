# Задача Лесенка
# напишите программу для черепахи, чтобы она рисовала вот так  (кол-во углов произвольное)

from turtle import *
from time import sleep
shape("turtle")
colors = ['black', 'red', 'blue', 'orange']
def steps(n, size=10):
    for i in range(0, n):
        color(colors[i % 4])
        left(90)
        forward(size)
        right(90)
        forward(size)
        size = size + 10
steps(8)
sleep(2)


# Задача Спираль квадоата
# напишите программу для черепахи, чтобы она рисовала вот так  (кол-во сторон произвольное)

# from turtle import *
# from time import sleep
# shape("turtle")
# colors = ['red', 'green', 'blue']
# delta = 10
# def steps(n, size=20):
#     for i in range(0, n):
#         color(colors[i % 3])
#         forward(size)
#         left(90)
#         size += delta
# steps(24)
# sleep(2)



# задача Зигзаг
# напишите программу для черепахи, чтобы она рисовала вот так  (кол-во сторон произвольное)

# from turtle import *
# from time import sleep
# shape("turtle")
# colors = ['red', 'black', 'blue']
# def steps(n, size=30):
#     for i in range(0, n):
#         color(colors[i % 3])
#         forward(size)
#         left(90)
#         forward(size)
#         right(90)
#         forward(size)
#         right(90)
#         forward(size)
#         left(90)
# steps(9)
# sleep(2)
#



# Задача Многоуголник закрашенный
# Дано:
# n - кол-во сторон (гарантируется, что число целое)
# a - сторона многоугольника
# is_fill - нужно залить фигуру (гарантируется, что будет использован только логический тип данных)
# нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным характеристикам
# УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную, хочет ли пользователь, чтобы каждая сторона многоугольника была разного цвета)

# from turtle import *
# from time import sleep
# shape("turtle")
# n = 9
# a = 50
# colors = ['red', 'black', 'blue', 'orange', 'green', 'yellow', 'cyan']
# pensize(2)
# def poly(n, size=a):
#     begin_fill()
#     if n > 2:
#         angle = 360 / n
#         for n in range(0, n):
#             color(colors[n % 7])
#             left(angle)
#             forward(a)
# poly(n)
# end_fill()
# sleep(2)
