mcdonaldsMenu = {
    "Burger": 2.99,
    "Fries": 1.99,
    "Drink": .99,
    "Nuggets": 2.59
    }
wendysMenu = {
    "Burger": 2.89,
    "Fries": 1.79,
    "Frosty": 1.99,
    "Nuggets": 1.99
    }
chickfilaMenu = {
    "Sandwich": 3.99,
    "Fries": 1.79,
    "Drink": 1.49,
    "Nuggets": 3.19
    }   
cookoutMenu = {
    "Tray": 5.99,
    "Fries": 1.99,
    "Milkshake": 2.99,
    "Quesadilla": 1.49
    }
timeMultiplier = {
    12: 1.5,
    13: 1.5,
    14: 1.3,
    18: 1.6,
    19: 1.6
}
is_quitting = False
print('Welcome to the Food Price Surge Calculator! Press enter to continue')
input()
while is_quitting == False:
    print("Select a restaurant to view prices: \n1. Mcdonalds\n2. Wendys\n3. Chick-Fil-A\n4. Cookout\n5. Quit")
    selection = input("Select a number from the list provided: ")