import random
num = random.randint(1,100)
guess = 0
attempts = 5
while guess < attempts:
    n = int(input("guess a number: "))
    guess+=1
    if n == num:
        print("won")
    else:
        print("failed")