
# задача
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.
print('Новая задача')
class Book:
        def __init__(self, title, name, style):
            self.title = title
            self.name = name
            self.style = style
my_book = Book(title='Мастер и Маргарита', name='Михаил Булгаков', style='Фантастический роман')
print(f'My book: title of book - {my_book.title}, name of autor - {my_book.name}, style of book - {my_book.style}.')
print()
print('Новая задача')
# задача
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе
class Bank_bill:
    def __init__(self, owner, balance ):
        self.owner = owner
        self.balance = balance
bill_1 = Bank_bill(owner='Булгаков', balance=1000000,)
bill_2 = Bank_bill(owner='Булгаков', balance=1000000,)
bill_3 = Bank_bill(owner='Булгаков', balance=1000000,)
bill_4 = Bank_bill(owner='Булгаков', balance=1000000,)
print(f'Владелец - {bill_1.owner}, balance - {bill_1.balance}')

#
# Не доделана!!! Эту задачу буду еще допиливать)))

print()
print('Новая задача')
# Реализуйте класс для управления системой бронирования отелей. Класс Бронь должен содержать информацию о госте, дате заезда и выезда, типе номера.
# Методы должны позволять бронировать, отменять бронь и проверять доступность номеров на определенные даты.
# free_date = ["12.05.23", "12.05.23", "12.05.23", "12.05.23", "12.05.23"]
# class Reserv:
#     def __init__(self, guest, date_in, date_out, room,):
#         self.guest = guest
#         self.date_in = date_in
#         self.date_out = date_out
#         self.room = room
#
# room_info = Reserv(guest=input("Введите имя гостя:  "), date_in=input(str("Введите дату заезда на май в формате 12.05.23:  ")),
#                    date_out=input("Введите дату выезда: "), room=input("Введите класс номера (стандарт или люкс):    "))
#
# print(f'Информация по бронированию: Имя гостя - {room_info.guest}, Дата Заезда - {room_info.date_in},'
#             f' Дата Выезда - {room_info.date_out}, Класс номера - {room_info.room}')
