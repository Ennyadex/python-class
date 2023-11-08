import random
x = input("enter any number: ")
r = random.randint(1,10)
if x == r:
    print("correct number is", r)
    print("you are correct")
else:
    print("correct option is", r)
    print("oooops you are wrong")