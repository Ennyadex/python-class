num = input("Enter any input: ")
r = type(int(num))
if r == float:
    print("float")
    print(type(r))
elif r == int:
    print("interger")
    print(type(r))
elif r == str:
     print("string")
     print(type(r))
