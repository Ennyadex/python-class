jobs= ["teaching","police","soldier","lecturer","doctor","nurse","accountant","lawyer","judge","pharmacist","retiring"]
age = int(input("enter your age: "))
if age >= 18 and age <= 20:
    for age in jobs:
        print(jobs[0])
        print(jobs[1])
        print(jobs[2])
        break
elif age >= 30 and age <= 35:
    for age in jobs:
        print(jobs[3])
        print(jobs[4])
        print(jobs[5])
        print(jobs[6])
        break
elif age >= 50 and age <= 55:
    for age in jobs:
        print(jobs[7])
        print(jobs[8])
        print(jobs[9])
        break
elif age >= 70 and age <= 75:
    for age in jobs:
        print(jobs[10])
        break
