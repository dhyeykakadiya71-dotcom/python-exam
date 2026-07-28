print(" ===================================== ")
print("|                                     |")
print("| Welcome to inventory list Analyzer! |")
print("|                                     |")
print(" ===================================== ")
item = []
item_catogery = set()
item_quantity = []

while True:
    ITEM = input("\nEnter the item Name:")
    catogery = input("Enter the item catogery:")
    quantity = int(input("Enter the item quantity:"))

    item.append(ITEM)
    item_catogery.add(catogery)
    item_quantity.append(quantity)


    user_input = input("\nDo you want to enter more item(yes/no):")
    user_input.lower()
    if user_input == "yes":
        pass
    elif user_input == "no":
        break
    else:
        print("\nInvalide option")
        while True:
            user_input = input("\nDo you want to enter more item(yes/no):")
            user_input.lower()
            if user_input == "yes":
                break
            elif user_input == "no":
                break
            else:
                pass
    if user_input == "no":
        break

print(" ===================================== ")
print("|                                     |")
print("|          inventory summary          |")
print("|                                     |")
print(" ===================================== ")

print(f"\nTotal Items : {len(item)}")
print(f"Total Quantity : {sum(item_quantity)}")
print(f"Average Quantity : {sum(item_quantity)/len(item_quantity)}")
print(f"Highest Quantity : {max(item_quantity)}")
print(f"Lowest Quantity : {min(item_quantity)}")

print("*" * 40)

print(f"Unique catogerys are shown here: {item_catogery}")

print("*" * 40)

print(" ========================================== ")
print("|                                          |")
print("|          Item stored by quantity         |")
print("|                                          |")
print(" ========================================== ")

sorted_items = list(item)
sorted_quantities = list(item_quantity)

for i in range(len(sorted_quantities)):
    for j in range(0, len(sorted_quantities) - i - 1):
        if sorted_quantities[j] < sorted_quantities[j + 1]:
            sorted_quantities[j], sorted_quantities[j + 1] = sorted_quantities[j + 1], sorted_quantities[j]
            sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]

for idx in range(len(sorted_items)):
    print(f"{idx + 1}. {sorted_items[idx]} - {sorted_quantities[idx]} units")

print(" ========================================== ")
print("|                                          |")
print("|     Categories in Alphabetical Order     |")
print("|                                          |")
print(" ========================================== ")

sorted_categories = sorted(list(item_catogery))
for idx, cat in enumerate(sorted_categories, 1):
    print(f"{idx}. {cat}")
