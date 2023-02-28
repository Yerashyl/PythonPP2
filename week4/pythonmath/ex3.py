from math import pi
from math import tan
def area_of_polygon(n, a):
    area = (n*a*a)/(4*tan(pi/n))
    print("The area of the polygon is:", area)
n = int(input("Input number of sides:"))
a = int(input("Input the length of a side:"))
area_of_polygon(n, a)