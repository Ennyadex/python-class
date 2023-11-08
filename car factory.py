cars = ("toyota","jeep","volkswagen","cammry","trailer") 
toyota = 200
jeep = 300
volkswagen = 400
cammry = 150
trailer = 500
car = input("enter car name: ")
dist = input("Enter distance for the car: ")

if car.lower() == "toyota":
   dist_lit = 10
   total = 10 * 200 * float(dist)
   print("hi, you entered ",car.upper())
   print("this car has a fuel capacity of ", toyota)
   print("the amount of fuel consumption for ", car.upper()," is ", total,"litres")
if car.lower() == "jeep":
    dist_lit = 20
    total = 20 * 300 * float(dist)
    print("hi, you entered",car.upper())
    print("this car has a fuel capacity of ", jeep)
    print("the amount of fuel consumption for ", car.upper()," is ", total,"litres")
if car.lower() == "volkswagen":
    dist_lit = 30
    total = 30 * 400 * float(dist)
    print("hi, you entered ",car.upper())
    print("this car has a fuel capacity of ", volkswagen)
    print("the amount of fuel comption for ", car.upper()," is ", total,"litres")
if car.lower() == "cammry":
    dist_lit = 40
    total =40 * 150 * float(dist)
    print("hi, you entered ",car.upper())
    print("this car has afuel capacity of ", cammry)
    print("the amount of fuel consumption for " , car.upper()," is ", total,"litres")
if car.lower() == "trailer":
    dist_lit = 50
    total = 50 * 500 * float(dist)
    print("hi, you entered",car.upper())
    print("this car has a fuel capacity of ", trailer)
    print("this amount of fuel comsumption for ", car.upper()," is ",total,"litres")  
else:
    print("the car you picked is not in our car list")
