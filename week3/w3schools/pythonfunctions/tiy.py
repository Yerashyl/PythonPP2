def address(street, home_number):
  print(street + " " + home_number)

address("Navoi", "467")

def team_2(*kids):
  print("The tallest child is " + kids[1])

team_2("Emil", "Tobias", "Linus")

def team_2(child3, child2, child1):
  print("The tallest child is " + child2)

team_2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def myfunction():
  pass

def product_calculate(x, y):
  return y * x

print(product_calculate(3, 5))
print(product_calculate(5, 10))
print(product_calculate(9, 63))

def my_function(food):
  for x in food:
    print(x)
    
places = ["Koktobe", "Medeu", "Mega", "Esentai"]

my_function(places)