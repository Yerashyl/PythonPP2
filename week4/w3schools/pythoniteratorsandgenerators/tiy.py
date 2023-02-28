tuple_a = ("apple", "banana", "cherry")
myit = iter(tuple_a)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "melons"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

tuple_l = ("apple", "banana", "cherry")

for x in tuple_l:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 2
      return x
    else:
      raise StopIteration

firstcl = Numbers()
oper = iter(firstcl)

for x in oper:
  print(x)