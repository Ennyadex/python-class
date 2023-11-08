class Addition:
    def __init__(self,firstnumber,secondnumber):
        self.fn = firstnumber
        self.sn = secondnumber
    def solve(self):
        add = self.fn + self.sn
        print(f"Addition of number is {add}")

class Subtraction:
    def __init__(self,firstnumber,secondnumber):
        self.fn = firstnumber
        self.sn = secondnumber
    def solve(self):
        subtract = self.fn - self.sn
        print(f" Subtraction of number is {subtract}")

class Multiplication:
    def __init__(self,firstnumber,secondnumber):
        self.fn = firstnumber
        self.sn = secondnumber
    def solve(self):
        multiply = self.fn * self.sn
        print(f" Multiplication of number is {multiply}")

class Division:
    def __init__(self,firstnumber,secondnumber):
        self.fn = firstnumber
        self.sn = secondnumber
    def solve(self):
        divide = self.fn / self.sn
        print(f" Division of number is {divide}")

print("welcome, we have program that can solve for Addition,Subtraction,Multiplication and Division")
print("A for additon,B for subtractin,C for multiplication,D for division and E to exit")
option = input(" enter your option here: ") 
if option.upper() == "A":
    print("you have opted for additon program")
    a = float(input("enter first number: "))
    b = float (input("enter second number: "))
    addition = Addition(a,b) 
    addition.solve()
elif option.upper() == "B":
    print("you have opted for subtraction program")
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    subtraction = Subtraction(a,b)
    subtraction.solve()
elif option.upper() == "C":
    print("you have opted for multiplicatin program")
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    multiplication = Multiplication(a,b)
    multiplication.solve()
elif option.upper() == "D":
    print("you have opted for division program")
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    division = Division(a,b)
    division.solve()
elif option.upper() == "E":
    print("you have opted to exit")
    exit()
elif option.upper() != "A" or option.upper() != "B" or option.upper() != "C" or option.upper() != "D" or option.upper() != "D" or option.upper() != "E":
    print("ooooops, you have opted wrong option")
    exit()