def add(x,y):
    add = x + y
    print(f"addition of two numbers is {add}")

def mult(x,y):
    m = x * y
    print(f"Multiplication of two numbers is {m}")

print("hello, we have program that can add and multiply, please choose your options")
print("A for addition, B for Multipliction, E to exit")
opt = input("Enter your option here: ")

if opt.upper() == "A":
    p = float(input("Enter first number: "))
    l = float(input("Enter second number: "))
    add(p,l)
elif opt.upper() == "B":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    mult(a,b)
elif opt.upper() == "E":
    print("bye bye")
    exit()
elif opt.upper() != "A" or opt.upper()!=  "B" or opt.upper() != "E":
    print("ooops, i dont understand your input")
    exit()
