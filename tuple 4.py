food_items = [
    ("Burger", 5.99),
    ("Pizza", 8.99),
    ("Salad", 4.50),
    ("Pasta", 7.25),
    ("Soda", 1.50)
]

sorted_food_items = sorted(food_items, key=lambda item: item[1], reverse=True)

print(sorted_food_items)
