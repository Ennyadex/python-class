class Brands:
    brand_1 = "amazon"
    brand_2 = "ebay"
    brand_3 = "olx"

class Products:
    prod_1 = "online ecommerce store"
    prod_2 = "online store"
    prod_3 = "online buy sell store"

class Popularity(Brands, Products):
    pop_1 = "100"
    pop_2 = "70"
    pop_3 = "60"
obj_1 = Popularity()
print(obj_1.brand_1 + " is an " + obj_1.prod_1 + " popularity of " + obj_1.pop_1)
print(obj_1.brand_2 + " is an " + obj_1.prod_2 + " popularity of " + obj_1.pop_2)
print(obj_1.brand_3 + " is an " + obj_1.prod_3 + " popularity of " +obj_1.pop_3)