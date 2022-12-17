# I imported the time library to use the time.sleep function at the beginning of the program.

import time

# I imported all of the food classes I needed from the food classes file to make instantiations with the meal name, the food or drink name, and the price of that item. For each meal there is a food class, and a drink class

from food_classes import Breakfast_Food
from food_classes import Breakfast_Drink

from food_classes import Lunch_Food
from food_classes import Lunch_Drink

from food_classes import Dinner_Food
from food_classes import Dinner_Drink

# Breakfast food items

breakfast_food1 = Breakfast_Food("Breakfast", "1 - 🥣  Oatmeal With Apples", 7)
breakfast_food2 = Breakfast_Food("Breakfast", "2 - 🍞  Toast With Butter and a Side of Strawberries", 7)
breakfast_food3 = Breakfast_Food("Breakfast", "3 - 🍳  Omelette with Ham and Cheese", 10)
breakfast_food4 = Breakfast_Food("Breakfast", "4 - 🍒  Yogurt with Berries Inside", 7)
breakfast_food5 = Breakfast_Food("Breakfast", "5 - 🍌  Cheerios with a Banana on the Side", 7)
breakfast_food6 = Breakfast_Food("Breakfast", "6 - 🥯  Bagel with Butter and a Muffin", 8)
breakfast_food7 = Breakfast_Food("Breakfast", "7 - 🍪  Scone with Jam and Bacon on the side", 10)
breakfast_food8 = Breakfast_Food("Breakfast", "8 - 🍫  Energy bar with a Pear", 9)
breakfast_food9 = Breakfast_Food("Breakfast", "9 - 🧇  Waffles with Maple Syrup and Strawberries", 10)
breakfast_food10 = Breakfast_Food("Breakfast", "10 - 🥞  Pancakes with Maple Syrup and Peach", 10)

# Breakfast drink items

breakfast_drink1 = Breakfast_Drink("Breakfast", "1 - 💧  Water", 0)
breakfast_drink2 = Breakfast_Drink("Breakfast", "2 - ☕  Coffee", 3)
breakfast_drink3 = Breakfast_Drink("Breakfast", "3 - ☕  Espresso", 5)
breakfast_drink4 = Breakfast_Drink("Breakfast", "4 - 🥛  Milk", 4)
breakfast_drink5 = Breakfast_Drink("Breakfast", "5 - 🍫  Chocolate Milk", 4)
breakfast_drink6 = Breakfast_Drink("Breakfast", "6 - 🍊  Orange Juice", 4)
breakfast_drink7 = Breakfast_Drink("Breakfast", "7 - 🍎  Apple Juice", 4)
breakfast_drink8 = Breakfast_Drink("Breakfast", "8 - 🌊  Sparkling Water", 2)
breakfast_drink9 = Breakfast_Drink("Breakfast", "9 - 🍵  Black Tea", 3)
breakfast_drink10 = Breakfast_Drink("Breakfast", "10 - 🍵  Herbal Tea", 3)

# Lunch food items

lunch_food1 = Lunch_Food("Lunch", "1 - 🥓  Grilled Cheese with Bacon", 7)
lunch_food2 = Lunch_Food("Lunch", "2 - 🥪  Club Sandwich with Bacon, Lettuce, and Mayonaise", 8)
lunch_food3 = Lunch_Food("Lunch", "3 - 🥗  Quinoa Salad", 7)
lunch_food4 = Lunch_Food("Lunch", "4 - 🌯  Chicken Wrap", 8)
lunch_food5 = Lunch_Food("Lunch", "5 - 🍕  Lunch Sized Pizza", 7)
lunch_food6 = Lunch_Food("Lunch", "6 - 🍣  Sushi", 10)
lunch_food7 = Lunch_Food("Lunch", "7 - 🥙  Smoked Meat Sandwich", 8)
lunch_food8 = Lunch_Food("Lunch", "8 - 🍔  Veggie Burger", 8)
lunch_food9 = Lunch_Food("Lunch", "9 - 🍤  Shrimp", 9)
lunch_food10 = Lunch_Food("Lunch", "10 - 🐟  Tuna Sandwich", 7)

# Lunch drink items

lunch_drink1 = Lunch_Drink("Lunch", "1 - 💧  Water", 0)
lunch_drink2 = Lunch_Drink("Lunch", "2 - 🥛  Milk", 4)
lunch_drink3 = Lunch_Drink("Lunch", "3 - 🍫  Chocolate Milk", 4)
lunch_drink4 = Lunch_Drink("Lunch", "4 - 🥤  Coke", 3)
lunch_drink5 = Lunch_Drink("Lunch", "5 - 🧃  Pepsi", 3)
lunch_drink6 = Lunch_Drink("Lunch", "6 - ☕  Coffee", 3)
lunch_drink7 = Lunch_Drink("Lunch", "7 - ☕  Espresso", 5)
lunch_drink8 = Lunch_Drink("Lunch", "8 - 🍍  Pineapple Juice", 3)
lunch_drink9 = Lunch_Drink("Lunch", "9 - 🍵  Green Tea", 2)
lunch_drink10 = Lunch_Drink("Lunch", "10 - 🥤  Sprite", 3)

# Dinner food items

dinner_food1 = Dinner_Food("Dinner", "1 - 🍔  Cheese Burger", 7)
dinner_food2 = Dinner_Food("Dinner", "2 - 🍔  Salmon Burger", 10)
dinner_food3 = Dinner_Food("Dinner", "3 - 🥗  Pizza with Ceaser Salad", 10)
dinner_food4 = Dinner_Food("Dinner", "4 - 🥟  Tortellini with Rose Sauce", 9)
dinner_food5 = Dinner_Food("Dinner", "5 - 🍗  Chicken Wings with Barbeque Sauce", 8)
dinner_food6 = Dinner_Food("Dinner", "6 - 🍟  Poutine", 7)
dinner_food7 = Dinner_Food("Dinner", "7 - 🧀  Macaroni and Cheese", 7)
dinner_food8 = Dinner_Food("Dinner", "8 - 🍖  Meat Loaf", 9)
dinner_food9 = Dinner_Food("Dinner", "9 - 🍜  Chicken Potpie", 10)
dinner_food10 = Dinner_Food("Dinner", "10 - 🍝  Spaghetti and Meatballs", 7)

# Dinner drink items

dinner_drink1 = Dinner_Drink("Dinner", "1 - 💧  Water", 0)
dinner_drink2 = Dinner_Drink("Dinner", "2 - 🌊  Sparkling Water", 2)
dinner_drink3 = Dinner_Drink("Dinner", "3 - 🥤  Coke", 3)
dinner_drink4 = Dinner_Drink("Dinner", "4 - 🥤  Diet Coke", 3)
dinner_drink5 = Dinner_Drink("Dinner", "5 - 🧃  Pepsi", 3)
dinner_drink6 = Dinner_Drink("Dinner", "6 - 🥛  Milk", 4)
dinner_drink7 = Dinner_Drink("Dinner", "7 - 🍺  Beer", 5)
dinner_drink8 = Dinner_Drink("Dinner", "8 - 🍷  Wine", 7)
dinner_drink9 = Dinner_Drink("Dinner", "9 - 🍋  Lemonade", 3)
dinner_drink10 = Dinner_Drink("Dinner", "10 - ☕  Hot Chocolate", 4)

# This is the function that controlls the inventory of the user. It has the ability to add, remove, view the cart, or checkout. 
# It takes the list of whichever meal was chosen and an empty dictionary which will be the inventory, with the item as the key, and the quantity of that item as the value. It also takes the add-remove-viewcart-checkout (arvc) parameter from the beginning which will we set to "a" as in add when the function starts.

def inventory_controller(meal_list, inventory_dict, arvc):

# This while loop, which runs only when the user has not chosen to checkout, it can add items, remove items, view cart, or checkout.

  while arvc != "c":

    # Adding Items

# **This may be easier it understand if you refer to any of the meal lists about 200 lines down**

# First I check is their choice was to add an item. If so, they will be able to choose an item based on the instructions given on how to choose items. There is a nested while loop that runs until the choice is valid (in the list). 

    if arvc == "a":
      inventory_choice = input("Enter the food or drink: ")
      while inventory_choice not in meal_list:
        print("\ninvalid menu choice. Try again")
        inventory_choice = input("Enter the food or drink: ")

# There is then a range which goes through the indexes of the list, and if the choice matches an item in the list, that means that the users selection is one index before, and the quantity is two indexes after, and that item's quantity gets assigned as the key after being added to by 1. 

      for i in range(len(meal_list)):
        if inventory_choice == meal_list[i]:
          meal_list[i + 2] += 1
          inventory_dict.update({meal_list[i - 1] : meal_list[i + 2]})
          print("\nItem successfully added")

    # Removing Items

# If the user's choice was r, then they will get the same chance to input the code of the item they wish to remove. The same code is used here to evaluate if the choice was valid before going any further.

    elif arvc == "r":
      inventory_choice = input("Enter the food or drink: ")
      while inventory_choice not in meal_list:
        print("\ninvalid menu choice. Try again")
        inventory_choice = input("Enter the food or drink: ")

# Once the user has made a valid choice, there is a for loop going through the indexes of the list, and once it finds the string that matches the user's input, it will first evaluate if the quantity of that item, which is 2 indexes later, is greater or equal to 1. If it is, then 1 will be subtracted from the quantity, and the inventory will be updated accordingly. Then if that quantity is equal to 0, the entire index (both key and value) will be deleted from the dictionary. If the quantity is not >= 1 in the first place, then a statement will pe printed, which says that their cart already doesn't contain whatever item they tried to delete. It is sliced because the names of the items when the objects were instantiated had for example "1 - 💧" before them.

      for i in range(len(meal_list)):
        if inventory_choice == meal_list[i]:
          if meal_list[i + 2] >= 1:
            meal_list[i + 2] -= 1
            inventory_dict.update({meal_list[i - 1] : meal_list[i + 2]})
            if meal_list[i + 2] == 0:
              del inventory_dict [meal_list[i - 1]]
            print("\nItem successfully removed")
          else:
            print(f"\nYour cart already does not contain any: {meal_list[i - 1][4::]}")

    # Viewing Cart

# If the user chooses to view the cart, "items and quantities" will be printed, and then the keys, followed by the values will be printed from the inventory dictionary's items.
        
    elif arvc == "v":
      print("\nItems and Quantities\n--------------------")
      for k, v in inventory_dict.items():
        print(k[4::],  v)

# After the user either adds, removes or views their cart, they will be asked to choose any of the 4 choices again. The arvc text function can be looked at below, it only has print statements in it. 

    arvc_text()
    arvc = input("Enter: ")
  
# If the user did not enter any of the 4 options, they will be asked until they do so.

    while arvc != "a" and arvc != "r" and arvc != "v" and arvc != "c":
      print("\ninvalid answer. try again")
      arvc_text()
      arvc = input("Enter: ")

# If their choice is c, a subtotal variable will be made, which will be added to by the quantity of any found item multiplied by its price. Once all of prices have been added, if the price is anything other than 0, a receipt will be printed. The loop will then stop and so will the function becuase arvc will be set to "c". However if subtotal remains to be 0, arvc will be set to "a", and the user will be prompted to add an item to their cart before checking out.
    if arvc == "c":
      subtotal = 0
      for i in range(len(meal_list)):
        for d in inventory_dict.keys():
          if meal_list[i] == d:
            subtotal += meal_list[i + 2] * meal_list[i + 3]
      if subtotal == 0:
        arvc = "a"
        print("\nYou are unable to checkout without having your order cost anything\nPlease select an item from the menu")
      else:
        print("\nORDER DETAILS\n-------------\n\nItems and Quantities\n--------------------")
        for k, v in inventory_dict.items():
          print(k[4::],  v)
        print(f"\nRECEIPT\n-------\nSubtotal: {subtotal}$\nTax owed: {round(subtotal * 0.13, 2)}$\nTotal: {round(subtotal * 1.13, 2)}$")


# When the program first runs, the strings in the list will be printed will delay from the time.sleep function.

def lobby_text():
  lobby_text_list = ["Welcome to Alex's 5 star e-restaurant", "You are in the lobby", "--------------------", ]
  lobby_text_list_slogan = ["* WE", " * SERVE", "  * BREAKFAST", "   * LUNCH", "    * DINNER", "-------------"]
  for i in lobby_text_list:
    print(i)
  for i in lobby_text_list_slogan:
    print(i)
    time.sleep(0.3)

# The following functions are just for text on the screen. The meal choices functions use the attributes of the classes.

def entrance_options():
  print("[e] enter the menu\n[q] quit the program")

def meal_choice():
  print("\nWhat kind of meal would you like today?\n[b] breakfast\n[l] lunch\n[d] dinner\n[q] quit the program")

def arvc_text():
  print("\n[a] add item\n[r] remove item\n[v] view cart\n[c] checkout\n")

def breakfast_choices():
  print(f"\nBreakfast Food\n--------------\n{breakfast_food1.food_or_drink} ${breakfast_food1.price}\n{breakfast_food2.food_or_drink} ${breakfast_food2.price}\n{breakfast_food3.food_or_drink} ${breakfast_food3.price}\n{breakfast_food4.food_or_drink} ${breakfast_food4.price}\n{breakfast_food5.food_or_drink} ${breakfast_food5.price}\n{breakfast_food6.food_or_drink} ${breakfast_food6.price}\n{breakfast_food7.food_or_drink} ${breakfast_food7.price}\n{breakfast_food8.food_or_drink} ${breakfast_food8.price}\n{breakfast_food9.food_or_drink} ${breakfast_food9.price}\n{breakfast_food10.food_or_drink} ${breakfast_food10.price}\n\nBreakfast Drinks\n----------------\n{breakfast_drink1.food_or_drink} ${breakfast_drink1.price}\n{breakfast_drink2.food_or_drink} ${breakfast_drink2.price}\n{breakfast_drink3.food_or_drink} ${breakfast_drink3.price}\n{breakfast_drink4.food_or_drink} ${breakfast_drink4.price}\n{breakfast_drink5.food_or_drink} ${breakfast_drink5.price}\n{breakfast_drink6.food_or_drink} ${breakfast_drink6.price}\n{breakfast_drink7.food_or_drink} ${breakfast_drink7.price}\n{breakfast_drink8.food_or_drink} ${breakfast_drink8.price}\n{breakfast_drink9.food_or_drink} ${breakfast_drink9.price}\n{breakfast_drink10.food_or_drink} ${breakfast_drink10.price}")

def lunch_choices():
  print(f"\nLunch Food\n--------------\n{lunch_food1.food_or_drink} ${lunch_food1.price}\n{lunch_food2.food_or_drink} ${lunch_food2.price}\n{lunch_food3.food_or_drink} ${lunch_food3.price}\n{lunch_food4.food_or_drink} ${lunch_food4.price}\n{lunch_food5.food_or_drink} ${lunch_food5.price}\n{lunch_food6.food_or_drink} ${lunch_food6.price}\n{lunch_food7.food_or_drink} ${lunch_food7.price}\n{lunch_food8.food_or_drink} ${lunch_food8.price}\n{lunch_food9.food_or_drink} ${lunch_food9.price}\n{lunch_food10.food_or_drink} ${lunch_food10.price}\n\nLunch Drinks\n----------------\n{lunch_drink1.food_or_drink} ${lunch_drink1.price}\n{lunch_drink2.food_or_drink} ${lunch_drink2.price}\n{lunch_drink3.food_or_drink} ${lunch_drink3.price}\n{lunch_drink4.food_or_drink} ${lunch_drink4.price}\n{lunch_drink5.food_or_drink} ${lunch_drink5.price}\n{lunch_drink6.food_or_drink} ${lunch_drink6.price}\n{lunch_drink6.food_or_drink} ${lunch_drink6.price}\n{lunch_drink7.food_or_drink} ${lunch_drink7.price}\n{lunch_drink8.food_or_drink} ${lunch_drink8.price}\n{lunch_drink9.food_or_drink} ${lunch_drink9.price}\n{lunch_drink10.food_or_drink} ${lunch_drink10.price}")

def dinner_choices():
  print(f"\nDinner Food\n--------------\n{dinner_food1.food_or_drink} ${dinner_food1.price}\n{dinner_food2.food_or_drink} ${dinner_food2.price}\n{dinner_food3.food_or_drink} ${dinner_food3.price}\n{dinner_food4.food_or_drink} ${dinner_food4.price}\n{dinner_food5.food_or_drink} ${dinner_food5.price}\n{dinner_food6.food_or_drink} ${dinner_food6.price}\n{dinner_food7.food_or_drink} ${dinner_food7.price}\n{dinner_food8.food_or_drink} ${dinner_food8.price}\n{dinner_food9.food_or_drink} ${dinner_food9.price}\n{dinner_food10.food_or_drink} ${dinner_food10.price}\n\nDinner Drinks\n----------------\n{dinner_drink1.food_or_drink} ${dinner_drink1.price}\n{dinner_drink2.food_or_drink} ${dinner_drink2.price}\n{dinner_drink3.food_or_drink} ${dinner_drink3.price}\n{dinner_drink4.food_or_drink} ${dinner_drink4.price}\n{dinner_drink5.food_or_drink} ${dinner_drink5.price}\n{dinner_drink6.food_or_drink} ${dinner_drink6.price}\n{dinner_drink6.food_or_drink} ${dinner_drink6.price}\n{dinner_drink7.food_or_drink} ${dinner_drink7.price}\n{dinner_drink8.food_or_drink} ${dinner_drink8.price}\n{dinner_drink9.food_or_drink} ${dinner_drink9.price}\n{dinner_drink10.food_or_drink} ${dinner_drink10.price}")

########## Breakfast inventory controller

# This function runs once breakfast is chosen and creates a dictionary for the inventory and sets arvc to "a". It also creates a list and runs the inventory controller function inside of the function. The breakfast items list is a parameter, as well as the dictionary and the arvc variable.

def breakfast_inverntory_controller():
  inventory_dict ={}
  arvc = "a"
  print("\nTo add items to your cart:\nEnter the letter f for \"food\" or d for \"drinks\" followed by number left of the item.\n(e.g d3 or f8)")
  breakfast_food1_quantity = 0
  breakfast_food2_quantity = 0
  breakfast_food3_quantity = 0
  breakfast_food4_quantity = 0
  breakfast_food5_quantity = 0
  breakfast_food6_quantity = 0
  breakfast_food7_quantity = 0
  breakfast_food8_quantity = 0
  breakfast_food9_quantity = 0
  breakfast_food10_quantity = 0
  breakfast_drink1_quantity = 0
  breakfast_drink2_quantity = 0
  breakfast_drink3_quantity = 0
  breakfast_drink4_quantity = 0
  breakfast_drink5_quantity = 0
  breakfast_drink6_quantity = 0
  breakfast_drink7_quantity = 0
  breakfast_drink8_quantity = 0
  breakfast_drink9_quantity = 0
  breakfast_drink10_quantity = 0

  breakfast_items_list = [breakfast_food1.food_or_drink, "f1", breakfast_food1.price, breakfast_food1_quantity, breakfast_food2.food_or_drink, "f2", breakfast_food2.price, breakfast_food2_quantity, breakfast_food3.food_or_drink, "f3", breakfast_food3.price, breakfast_food3_quantity, breakfast_food4.food_or_drink, "f4", breakfast_food4.price, breakfast_food4_quantity, breakfast_food5.food_or_drink, "f5", breakfast_food5.price, breakfast_food5_quantity, breakfast_food6.food_or_drink, "f6", breakfast_food6.price, breakfast_food6_quantity, breakfast_food7.food_or_drink, "f7", breakfast_food7.price, breakfast_food7_quantity, breakfast_food8.food_or_drink, "f8", breakfast_food8.price, breakfast_food8_quantity, breakfast_food9.food_or_drink, "f9", breakfast_food9.price, breakfast_food9_quantity, breakfast_food10.food_or_drink, "f10", breakfast_food10.price, breakfast_food10_quantity, breakfast_drink1.food_or_drink, "d1", breakfast_drink1.price, breakfast_drink1_quantity, breakfast_drink2.food_or_drink, "d2", breakfast_drink2.price, breakfast_drink2_quantity, breakfast_drink3.food_or_drink, "d3", breakfast_drink3.price, breakfast_drink3_quantity, breakfast_drink4.food_or_drink, "d4", breakfast_drink4.price, breakfast_drink4_quantity, breakfast_drink5.food_or_drink, "d5", breakfast_drink5.price, breakfast_drink5_quantity, breakfast_drink6.food_or_drink, "d6", breakfast_drink6.price, breakfast_drink6_quantity, breakfast_drink7.food_or_drink, "d7", breakfast_drink7.price, breakfast_drink7_quantity, breakfast_drink8.food_or_drink, "d8", breakfast_drink8.price, breakfast_drink8_quantity, breakfast_drink9.food_or_drink, "d9", breakfast_drink9.price, breakfast_drink9_quantity, breakfast_drink10.food_or_drink, "d10", breakfast_drink10.price, breakfast_drink10_quantity]

  inventory_controller(breakfast_items_list, inventory_dict, arvc)

########## Lunch inventory controller

# This function runs once lunch is chosen and creates a dictionary for the inventory and sets arvc to "a". It also creates a list and runs the inventory controller function inside of the function. The lunch items list is a parameter, as well as the dictionary and the arvc variable.

def lunch_inverntory_controller():
  inventory_dict ={}
  arvc = "a"
  print("\nTo add items to your cart:\nEnter the letter f for \"food\" or d for \"drinks\" followed by number left of the item.\n(e.g d3 or f8)")
  lunch_food1_quantity = 0
  lunch_food2_quantity = 0
  lunch_food3_quantity = 0
  lunch_food4_quantity = 0
  lunch_food5_quantity = 0
  lunch_food6_quantity = 0
  lunch_food7_quantity = 0
  lunch_food8_quantity = 0
  lunch_food9_quantity = 0
  lunch_food10_quantity = 0
  lunch_drink1_quantity = 0
  lunch_drink2_quantity = 0
  lunch_drink3_quantity = 0
  lunch_drink4_quantity = 0
  lunch_drink5_quantity = 0
  lunch_drink6_quantity = 0
  lunch_drink7_quantity = 0
  lunch_drink8_quantity = 0
  lunch_drink9_quantity = 0
  lunch_drink10_quantity = 0

  lunch_items_list = [lunch_food1.food_or_drink, "f1", lunch_food1.price, lunch_food1_quantity, lunch_food2.food_or_drink, "f2", lunch_food2.price, lunch_food2_quantity, lunch_food3.food_or_drink, "f3", lunch_food3.price, lunch_food3_quantity, lunch_food4.food_or_drink, "f4", lunch_food4.price, lunch_food4_quantity, lunch_food5.food_or_drink, "f5", lunch_food5.price, lunch_food5_quantity, lunch_food6.food_or_drink, "f6", lunch_food6.price, lunch_food6_quantity, lunch_food7.food_or_drink, "f7", lunch_food7.price, lunch_food7_quantity, lunch_food8.food_or_drink, "f8", lunch_food8.price, lunch_food8_quantity, lunch_food9.food_or_drink, "f9", lunch_food9.price, lunch_food9_quantity, lunch_food10.food_or_drink, "f10", lunch_food10.price, lunch_food10_quantity, lunch_drink1.food_or_drink, "d1", lunch_drink1.price, lunch_drink1_quantity, lunch_drink2.food_or_drink, "d2", lunch_drink2.price, lunch_drink2_quantity, lunch_drink3.food_or_drink, "d3", lunch_drink3.price, lunch_drink3_quantity, lunch_drink4.food_or_drink, "d4", lunch_drink4.price, lunch_drink4_quantity, lunch_drink5.food_or_drink, "d5", lunch_drink5.price, lunch_drink5_quantity, lunch_drink6.food_or_drink, "d6", lunch_drink6.price, lunch_drink6_quantity, lunch_drink7.food_or_drink, "d7", lunch_drink7.price, lunch_drink7_quantity, lunch_drink8.food_or_drink, "d8", lunch_drink8.price, lunch_drink8_quantity, lunch_drink9.food_or_drink, "d9", lunch_drink9.price, lunch_drink9_quantity, lunch_drink10.food_or_drink, "d10", lunch_drink10.price, lunch_drink10_quantity]

  inventory_controller(lunch_items_list, inventory_dict, arvc)

########## Dinner inventory controller

# This function runs once dinner is chosen and creates a dictionary for the inventory and sets arvc to "a". It also creates a list and runs the inventory controller function inside of the function. The dinner items list is a parameter, as well as the dictionary and the arvc variable.

def dinner_inverntory_controller():
  inventory_dict ={}
  arvc = "a"
  print("\nTo add items to your cart:\nEnter the letter f for \"food\" or d for \"drinks\" followed by number left of the item.\n(e.g d3 or f8)")
  dinner_food1_quantity = 0
  dinner_food2_quantity = 0
  dinner_food3_quantity = 0
  dinner_food4_quantity = 0
  dinner_food5_quantity = 0
  dinner_food6_quantity = 0
  dinner_food7_quantity = 0
  dinner_food8_quantity = 0
  dinner_food9_quantity = 0
  dinner_food10_quantity = 0
  dinner_drink1_quantity = 0
  dinner_drink2_quantity = 0
  dinner_drink3_quantity = 0
  dinner_drink4_quantity = 0
  dinner_drink5_quantity = 0
  dinner_drink6_quantity = 0
  dinner_drink7_quantity = 0
  dinner_drink8_quantity = 0
  dinner_drink9_quantity = 0
  dinner_drink10_quantity = 0

  dinner_items_list = [dinner_food1.food_or_drink, "f1", dinner_food1.price, dinner_food1_quantity, dinner_food2.food_or_drink, "f2", dinner_food2.price, dinner_food2_quantity, dinner_food3.food_or_drink, "f3", dinner_food3.price, dinner_food3_quantity, dinner_food4.food_or_drink, "f4", dinner_food4.price, dinner_food4_quantity, dinner_food5.food_or_drink, "f5", dinner_food5.price, dinner_food5_quantity, dinner_food6.food_or_drink, "f6", dinner_food6.price, dinner_food6_quantity, dinner_food7.food_or_drink, "f7", dinner_food7.price, dinner_food7_quantity, dinner_food8.food_or_drink, "f8", dinner_food8.price, dinner_food8_quantity, dinner_food9.food_or_drink, "f9", dinner_food9.price, dinner_food9_quantity, dinner_food10.food_or_drink, "f10", dinner_food10.price, dinner_food10_quantity, dinner_drink1.food_or_drink, "d1", dinner_drink1.price, dinner_drink1_quantity, dinner_drink2.food_or_drink, "d2", dinner_drink2.price, dinner_drink2_quantity, dinner_drink3.food_or_drink, "d3", dinner_drink3.price, dinner_drink3_quantity, dinner_drink4.food_or_drink, "d4", dinner_drink4.price, dinner_drink4_quantity, dinner_drink5.food_or_drink, "d5", dinner_drink5.price, dinner_drink5_quantity, dinner_drink6.food_or_drink, "d6", dinner_drink6.price, dinner_drink6_quantity, dinner_drink7.food_or_drink, "d7", dinner_drink7.price, dinner_drink7_quantity, dinner_drink8.food_or_drink, "d8", dinner_drink8.price, dinner_drink8_quantity, dinner_drink9.food_or_drink, "d9", dinner_drink9.price, dinner_drink9_quantity, dinner_drink10.food_or_drink, "d10", dinner_drink10.price, dinner_drink10_quantity]

  inventory_controller(dinner_items_list, inventory_dict, arvc)