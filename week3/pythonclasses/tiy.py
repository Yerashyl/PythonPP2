class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number

p1 = Person("Bale", 11)

print(p1.name)
print(p1.number)

class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number

p1 = Person("Bale", 11)

print(p1)

class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def __str__(self):
    return f"{self.name}({self.number})"

p1 = Person("Bale", 11)

print(p1)

class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def myfunc(self):
    print("I'm " + self.name + " and my number was " + self.number)

p1 = Person("Bale", "11")
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, number):
    mysillyobject.name = name
    mysillyobject.number = number

  def myfunc(abc):
    print("I'm " + abc.name + " and my number is " + abc.number)

p1 = Person("Bale", "11")
p1.myfunc()