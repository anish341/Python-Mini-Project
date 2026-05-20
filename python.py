# #Define the menu of restaurant 
menu = {
    'Pizza': 40,
    'Pasta':50,
    'Burger':60,
    'Solad':70,
    'Coffee':80,
    'Smosh':90,
    'Dosa':100,
}

# Greet
print("Welcome to python resturant")
print("Pizza: Rs40\nPasta: Rs50\nBurge: Rs60\nSolad:Rs70\nCoffee: Rs80");

order_total = 0
# 80 + 70 =150;
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is not available yet !")

another_order = input("Do you want to add another item?(Yes/No)")

if another_order =="Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"order item {item_2} is not avaialable!")
print(f"The total amount of item to pay is {order_total}")   
