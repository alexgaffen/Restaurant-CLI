# I imported the text functions file first, since it has most of the code and all of the functions.

import text_functions

# These 2 functions run, followed by an input. 

text_functions.lobby_text()
text_functions.entrance_options()
choice_to_enter = input()

# The while loop will run while the input is not "q" as in quit the program. They are then given one more option to quit, or to select a meal. 
# If the answer isn't one of the options, and invalid answer will be printed.

while choice_to_enter != "q":
  

  if choice_to_enter == "e":
    text_functions.meal_choice()
    meal_choice = input()
    
    if meal_choice == "b":
      text_functions.breakfast_choices()
      text_functions.breakfast_inverntory_controller()
      choice_to_enter = "q"

    elif meal_choice == "l":
      text_functions.lunch_choices()
      text_functions.lunch_inverntory_controller()
      choice_to_enter = "q"

    elif meal_choice == "d":
      text_functions.dinner_choices()
      text_functions.dinner_inverntory_controller()
      choice_to_enter = "q"
      
    elif meal_choice == "q":
      choice_to_enter = "q"

    else:
      print("Invalid answer. Please Try Again.")
        

  else:
    print("Invalid answer. Please Try Again.")
    text_functions.entrance_options()
    choice_to_enter = input()
  
# Once the while loop is done running the below print statement will run.

print("\nProgram successfully exited. Goodbye.")
