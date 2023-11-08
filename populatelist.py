lst = []
num = 0
try:
    num = int(input("enter any number: "))
    for n in range(0,num):
        n = int(input())
        lst.append(n)
        print(lst)
        if n == "f":
            print("you have enter a flag")
            break
except  ValueError:
    print("enter integer only")