def circle(x,r):
    a = x * r * r
    print(f" area of a circle is {a}")
    
def rec(l,b):
    m = 2 * (l + b)
    print(f" perimeter of a rectangle is {m}")

def si(p,r,t):
    si = (p * r * t) / 100
    print(f" simple interest is {si}")

import math
def af(a,b,c):
    f = (b * b) - (4 * a * c)
    x1 = ((-b) + math.sqrt(f)) / 2 * a
    x2 = ((-b) - math.sqrt(f)) / 2 * a
    print(f" x1 = {x1} and x2 = {x2}")

print("hello, we have program that can solve area of a circle, perimeter of a rectangle, simple interest and almighty formular.please choose your option")
print("A for area of circle,B for perimeter of a rectangle,C for simple interest,D for almighty formular and E for exit ")
option = input("enter your option here: ")

if option.upper() == "A":
    print("you have opted for area of a circle program")
    v = float(input("enter value for pi: "))
    r = float(input("enter value for radius: "))
    circle(v,r)    
elif option.upper() == "B":
    print("you have opted for perimeter of a rectangle program")
    l = float(input("enter value for length: "))
    b = float(input("enter value for breadth: "))
    rec(l,b)
elif option.upper() == "C":
    print("you have opted for simple interest program")
    p = float(input("enter value for principal: "))
    r = float(input("enter value for rate: "))
    t = float(input("enter value for time: "))
    si(p,r,t)
elif option.upper() == "D":
    print("you have opted for almighty formular program")
    a = float(input("enter value for a: "))
    b = float(input("enter value for b: "))
    c = float(input("enter value for c: "))
    af(a,b,c)
elif option.upper() == "E":
    print("you have opted to exit")
    exit()
elif option.upper() != "A" or option.upper() != "B" or option.upper() != "C" or option.upper() != "D" or option.upper() != "E":
    print("oooops,i don't understand your input")
    exit()