def trap(a,b,h):
    area = (a + b) * h / 2
    print(f" area of trapezium is {area}")
print("hello, we program to solve area of a trapezium. please input your option")
print("enter A for area of a trapezium and E to exit")
option = input("enter your option here: ")
if option.upper() == "A":
    print("you have opted for area of a trapezium")
    m = int(input("enter value for a: "))
    j = int(input("enter value for b: "))
    k = int(input("enter value for h: "))
    trap(m,j,k)
elif option.upper() == "E":
    print("you have opted to exit")
    exit()