class Food:
  '''
  This food class is the parent food class and only has a meal type attribute
  '''
  def __init__(self, meal_type):
    self.meal_type = meal_type

#Breakfast class

class Breakfast(Food):
  '''
  This breakfast class inherits from the food class and has the food_or_drink attribute
  '''
  def __init__(self, meal_type, food_or_drink):
    Food.__init__(self, meal_type)
    self.food_or_drink = food_or_drink


#Breakfast foods and drinks classes

class Breakfast_Food(Breakfast):
  '''
  This breakfast food class inherits from the breakfast class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price
  
class Breakfast_Drink(Breakfast):
  '''
  This breakfast drink class inherits from the breakfast class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price

#Lunch class
  
class Lunch(Food):
  '''
  This lunch class inherits from the food class and has the food_or_drink attribute
  '''
  def __init__(self, meal_type, food_or_drink):
    Food.__init__(self, meal_type)
    self.food_or_drink = food_or_drink

#Lunch foods and drinks classes

class Lunch_Food(Lunch):
  '''
  This lunch food class inherits from the lunch class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price
  
class Lunch_Drink(Lunch):
  '''
  This lunch drink class inherits from the lunch class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price

#Dinner class

class Dinner(Food):
  '''
  This dinner class inherits from the food class and has the food_or_drink attribute
  '''
  def __init__(self, meal_type, food_or_drink):
    Food.__init__(self, meal_type)
    self.food_or_drink = food_or_drink

#Dinner foods and drinks classes

class Dinner_Food(Dinner):
  '''
  This dinner food class inherits from the dinner class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price
  
class Dinner_Drink(Dinner):
  '''
  This dinner food class inherits from the dinner class and adds the price attribute
  '''
  def __init__(self, meal_type, food_or_drink, price):
    Dinner.__init__(self, meal_type, food_or_drink)
    self.price = price