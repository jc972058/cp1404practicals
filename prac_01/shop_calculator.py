"""
get number of items
get price for each number
calculate total price
is the price over $100
if yes * 0.1
else nothing
print number of items
print price of items
"""
number_of_items = int(input("Number of items: "))
total_cost = 0
while number_of_items < 0:
    print("Invalid number of items!!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1, 1):
    price_of_item = float(input(f"Price of item {i}: "))
    total_cost = total_cost + price_of_item
if total_cost > 100:
    total_cost = total_cost - (total_cost * 0.1)
print(f"The total price for {number_of_items} items is ${total_cost:.2f}")
