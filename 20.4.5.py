import json
from itertools import count

with open("orders_july_2023.json","r") as f:
    orders = json.load (f)
    print(orders)

#1.Какой номер самого дорого заказа за июль?
max_price = 0
max_order = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2.Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством товаров: {max_order}, количество товаров: {max_quantity}')

#3.В какой день в июле было сделано больше всего заказов?
date_dict = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    date_dict[date] = date_dict.get(date,0) + 1

for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        date_dict[date] = max_value
print(f'Больше всего заказов в июле было сделано {date}: {date_dict[date]} заказов')

#4.Какой пользователь сделал самое большое количество заказов за июль?
user_dict = {}
for order_num, orders_data in orders.items():
    user = orders_data['user_id']
    user_dict[user] = user_dict.get(user,0) + 1

for a in sorted(user_dict):
    max_val = max(user_dict.values())
    if user_dict[user] == max_val:
        user_dict[user] = max_val
print(f'Cамое большое количество заказов за июль сделал пользователь с № {user}: {user_dict[user]} заказов')


#5.У какого пользователя самая большая суммарная стоимость заказов за июль?
user_prace_dict = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    user_prace_dict[user_id] = user_dict.get(user_id,0) + price

for user_id in sorted(user_prace_dict):
    max_value = max(user_prace_dict.values())
    if user_prace_dict[user_id] == max_value:
        user_prace_dict[user_id] = max_value
print(f'Cамая большая суммарная стоимость заказов за июль была у пользователя с № {user_id}: на сумму {user_prace_dict[user_id]} ')


#6.Какая средняя стоимость заказа была в июле?
price_sum = 0
for order_num, orders_data in orders.items():
    price_sum += orders_data['price']
    averege_sum_order = price_sum/len(orders)
print(f'Какая средняя стоимость заказа в июле: {round(averege_sum_order,2)}')

#7.Какая средняя стоимость товаров в июле?
price_sum = 0
counts = 0
for order_num, orders_data in orders.items():
    count = orders_data['quantity']
    counts += count
    price_sum += orders_data['price']
    averege_sum = price_sum/counts
print(f'Какая средняя стоимость товаров в июле: {round(averege_sum,2)}')



