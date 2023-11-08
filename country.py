countries = ["london","america","japan","iran","isreal"]
countryname = input("enter country name:")
if countryname.lower() == countries[0]:
    print("beautiful country")
if countryname.lower() == countries[1]:
    print("developed country")
if countryname.lower() == countries[2]:
    print("developing country")
if countryname.lower() == countries[3]:
    print("war zone country")
if countryname.lower() == countries[4]:
    print("underdeveloped country")
elif countryname.lower()== "":
    print("try again later")
