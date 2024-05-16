indian_cuisines = ["Butter Chicken", "Paneer Butter Masala", "Butter Naan", "Pav Bhaji", "Pulao", "Chicken Tikka", "Fish Tikka", "Dabeli"]
chinese_cuisines = ["Egg Roll","Pot Sticker", "Fried Rice"]
italian_cuisines = ["Pizza", "Pasta"]

dish_name = input("Enter a dish name: ")

if dish_name in indian_cuisines:
    print(dish_name + " is a Indian cuisine Dish")
elif dish_name in chinese_cuisines:
    print(dish_name + " is a Chinese cuisine Dish")
elif dish_name in italian_cuisines:
    print(dish_name + " is a Italian cuisine Dish")
else:
    print("Based on my limited knowledge, I don't know which cuisine is ", dish_name)
