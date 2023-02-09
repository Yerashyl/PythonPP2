x = lambda a : a + 10
print(x(6))

x = lambda a, b : a * b
print(x(35, 8))

x = lambda a, b, c : a + b + c
print(x(9, 4, 78))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(41))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(42))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))