# Задача 1:
# Вам дана строка текста. Напишите программу, которая проверяет, содержится ли в ней заданная подстрока.
# Если подстрока найдена, программа должна вывести индекс её первого вхождения в строку,
# иначе - сообщение о том, что подстрока не найдена.

# test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam et turpis magna."
# und_str = "dolor"
# if und_str in test_string:
#     print(f'Выбранная подстрока находится в строке и ее индекс вхождения = {test_string.find(und_str)}')
# else:
#     print('Выбранная подстрока не встречается в данной строке')


# Задача 4:
# Напишите программу, которая принимает строку и меняет регистр каждой буквы:
# если буква была в верхнем регистре, то она становится строчной, и наоборот.

# test_string = input("Введите текст    ")
# print("Меняем регистр всех букв и получаем  -  "+test_string.swapcase())


# Задача 5:
# Напишите программу, которая переворачивает строку задом наперёд.
# Например, из строки "Hello" должно получиться "olleH".

# test_string = "Lorem ipsum dolor sit amet"
# revers_str = "".join(reversed(test_string))
# print(revers_str)


# Задача 3:
# Напишите программу, которая определяет, является ли заданная строка палиндромом
# (читается одинаково слева направо и справа налево).
# Программа должна игнорировать пробелы, регистр букв и пунктуацию.
# test_string = "ABBA"
# revers_str = "".join(reversed(test_string))
# if revers_str == test_string:
#     print("Палиндром")
# else:
#     print("Не Палиндром")


# Задача 7:
# Напишите программу, которая принимает строку и выводит на экран частоту встречаемости каждого символа в ней.
# test_string = "Lorem ipsum lorem"
# for i in test_string:
#     print(f'Символ', i, "Встречается раз :", {test_string.count(i)})
