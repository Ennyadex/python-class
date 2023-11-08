fruits = ["apple","mango","orange","guava","banana","watermelon"]
for x in fruits:
    print("fruit", x)
    if x == "orange":
        print("i have reached", x)
        break
    

fruits = ["apple","mango","orange","guava","banana","watermelon"]
for x in fruits:
    if x == "mango":
        continue
    print(x)