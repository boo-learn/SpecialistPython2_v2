import random

number_items = int(input("Enter amount of items sold "))
item_price_list = []

for i in range(number_items):
    item_price_list.append(random.randint(1, 100))

print(f"Items at price  {item_price_list}")

item_price_list.sort()
item_price_list.reverse()

print(f"Items sorted by price  {item_price_list}")

middle_index = round(len(item_price_list) / 2)

print(
    f"List of most expensive items sold {item_price_list[:middle_index]}\nSum of most expensive items: {sum(item_price_list[:middle_index])}")

