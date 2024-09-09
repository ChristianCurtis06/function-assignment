# Task 1: Write a function that lets the user add items to a list
shopping_list = []

def add_item():
    add_input = input("\nWhat would you like to add to your shopping list? ").lower()
    if len(add_input) > 0:
        print(f"{add_input} was added to your shopping list.")
        shopping_list.append(add_input)
    else:
        print("Invalid input. Please try again.")

# Task 2: Include a function to remove items from the list
def remove_item():
    remove_input = input("\nWhat would you like to remove from your shopping list? ").lower()
    if remove_input in shopping_list:
        print(f"{remove_input} was removed from your shopping list.")
        shopping_list.remove(remove_input)
    else:
        print(f"{remove_input} was not found in your shopping list.")

# Task 3: Add a function that prints out the entire list in a formatted way
def view_list():
    if len(shopping_list) == 0:
        print("Your shopping list is empty.")
    elif len(shopping_list) == 1:
        print(f"Your shopping list: {shopping_list[0]}")
    else:
        print(f"Your shopping list: {", ".join(shopping_list[:-1])} and {shopping_list[-1]}")

print("Shopping List Program:")

while True:
    choice = input("\nWould you like to [A]dd items, [R]emove items, [V]iew your shopping list, or [Q]uit the program? ").upper()
    if choice == "A":
        add_item()
    elif choice == "R":
        remove_item()
    elif choice == "V":
        view_list()
    elif choice == "Q":
        print("Quitting the program.")
        break
    else:
        print("Invalid input. Please try again.")