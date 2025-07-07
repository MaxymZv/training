grocery_list = [
    "Apples: 1.20","bananas: 0.50",
    "Oranges: 0.80", "Milk: 1.50",
    "Bread: 2.00", "Eggs: 3.00"
]


def groceries_cost(grocery_list):
    total_cost = 0
    for item in grocery_list:
        item_name, item_price = item.split(':')
        total_cost += float(item_price.strip())
    return total_cost


print("Welcome to the Grocery Store!")
print("Here is your grocery list:")
for item in grocery_list:
    print(item)

print("\nCalculating total cost...")
total_cost = groceries_cost(grocery_list)
print(f"Total cost of groceries: ${total_cost:.2f}")