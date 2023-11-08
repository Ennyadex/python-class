import random
num = random.randint(1,100)
guess = 0
attempts = 5
while guess < attempts:
    guess = int(input("guess a number: "))
    if guess == num:
        print("good guess, the random number is ",num, " and the guessed number is ",guess)
    else:
        print("try again")
        
attempts+=0