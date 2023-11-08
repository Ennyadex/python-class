withdraw = float(input("enter amount to withdraw:"))
balance = 100000 - withdraw
if withdraw <= 100000:
    print("you have withdrawn ", withdraw," and  balance is", balance)
elif withdraw >= 100000:
    print("insufficient balance is", balance)