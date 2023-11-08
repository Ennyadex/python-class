class Brands:
    brand_1 = "amazon"
    brand_2 = "ebay"
    brand_3 = "olx"

class Products(Brands):
    prod_1 = "online ecommerce store"
    prod_2 = "online store"
    prod_3 = "online buy sell store"

class Popularity(Brands):
    pop_1 = "100"
    pop_2 = "70"
    pop_3 = "60"

class Value(Brands):
    val_1 = "excellent value"
    val_2 = "better value"
    val_3 = "good value"
obj_1 = Products()
obj_2 = Popularity()
obj_3 = Value()
print(obj_1.brand_1 + " is an " + obj_1.prod_1+" has popularity of "+obj_2.pop_1+" with an "+obj_3.val_1)
print(obj_1.brand_2 + " is an " + obj_1.prod_2)
print(obj_1.brand_3 + " is an " + obj_1.prod_3)