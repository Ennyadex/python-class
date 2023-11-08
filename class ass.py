class Areaofacircle:
    def __init__(self,pi,radius):
        self.p = pi
        self.r = radius
    def solve(self):
        aoc = self.p * self.r * self.r
        print(f"area of a circle is {aoc}")

class Perimeterofarectangle:
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth
    def solve(self):
        por = 2 * (self.l + self.b)
        print(f"perimeter of a rectangle is {por}")

class Simpleinterest:
    def __init__(self,principal,rate,time):
        self.p = principal
        self.r = rate
        self.t = time
    def solve(self):
        si = (self.p * self.r * self.t) / 100
        print(f"simple interest is {si}")

class Almightyformular:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
     import math
     f = (self.b * self.b) - (4 * self.a * self.c)
     x1 = ((- self.b) + math.sqrt(f)) / 2 * self.a
     x2 = ((- self.b) - math.sqrt(f)) / 2 * self.a
     print(f"x1 = {x1} and x2 = {x2}")

print("hello,we have program that can solve area of circle,perimeter of a rectangle,simple interest and almighty formular.please input your option")
print("A for area of circle,B for perimeter of a rectangle,C for simple interest,D for almighty formular and E to exit")
option = input("enter your option here: ")

if option.upper() == "A":
    print("you have opted for area of a circle program")
    p = float(input("enter value for pi: "))
    r = float (input("enter value for radius: "))
    area = Areaofacircle(p,r)
    area.solve()

elif option.upper() == "B":
    print("you have opted for perimeter of a rectangle program")
    l = float(input("enter value for length: "))
    b = float(input("enter value for breadth: "))
    perimeter = Perimeterofarectangle(l,b)
    perimeter.solve()

elif option.upper() == "C":
    print("you have opted for simple interest program")
    p = float(input("enter value for principal: "))
    r = float(input("enter value for rate: "))
    t = float(input("enter value for time: "))
    simple = Simpleinterest(p,r,t)
    simple.solve()

elif option.upper() == "D":
    print("you have opted for almighty formular program")
    a = float(input("enter value for a: "))
    b = float(input("enter value for b: "))
    c = float(input("enter value for c: "))
    al = Almightyformular(a,b,c)
    al.solve()

elif option.upper() == "E":
    print("you have opted to exit")
    exit()

elif option.upper() != "A" or option.upper() != "B" or option.upper() != "C" or option.upper() != "D" or option.upper() != "E":
    print("ooooops,you've opted wrong option")
    exit()