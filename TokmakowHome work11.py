# Задача
# Дано: Информация о заказах (название блюда, количество, цена).
# Найти: Общую стоимость заказа, список уникальных блюд в меню.
# Пример:
# Входные данные:
# {“Заказ 1”: ("Пицца", 2, 250),
# “Заказ 2”: ("Салат", 1, 150),
# “Заказ 3”: ("Пицца", 1, 250)}
# Выходные данные:
# Общая стоимость заказа: 900
# Уникальные блюда в меню: {"Пицца", "Салат"}

orders = {"Заказ 1": ("Пицца", 2, 250),
          "Заказ 2": ("Сок", 1, 0), # добавил для наглядности
          "Заказ 3": ("Салат", 1, 0), # оставил только наименование бдюда
          "Заказ 4": ("Салат", 1, 150),
          "Заказ 5": ("Пицца", 1, 250)}
uniq = {key: value[0] for key, value in orders.items()} # оставил только наименование бдюда
uniq = set(uniq.values()) # получил уникальные
for value in uniq:  
    print("Уникальное блюдо :   ", value)  
orders_money = {key: value[1] * value[2] for key, value in orders.items()} # общая по кажд. заказу
print("Общая стоимость по каждому заказу - ", orders_money)
total_money = sum(orders_money.values()) # общая
print("Общая стоимость всех заказов - ", total_money) 



# Задача
# Дано: Множество уникальных заказов и список выполненных заказов.
# Найти: Невыполненные заказы.
# Пример:
# Входные данные:
# Уникальные заказы: {1, 2, 3, 4, 5}
# Выполненные заказы: [2, 4]

# Выходные данные:
# Невыполненные заказы: {1, 3, 5}
print()
print("Новая задача ")
orders = {1 ,2 ,3 ,4 ,5}
done_orders = [2,4]

orders = list(orders)
not_done_orders = []
for el in orders:
    if el not in done_orders:
        not_done_orders.append(el)
print("Не выполненые заказы",not_done_orders)

# Задача
# Создайте словарь всех покупателей и стоимости покупок (для каждого покупателя: стоимость покупки). найти для такого словаря:
# ●	максимальную стоимость покупки и кто совершил эту покупку
# ●	кол-во сделанных продаж

print()
print("Новая задача ")
buy_dict = {"Николай": 10, "Кирилл": 100, "Кирилл": 800, "Елена": 30}
print(buy_dict) 
max_price = max(buy_dict.values())
max_price_key = max(buy_dict, key=buy_dict.get)
print("Максимальная стоимость :",max_price)
print("Больше всех потратил : ", max_price_key)


