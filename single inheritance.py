class Brands:
    brand_1 = "amazon"
    brand_2 = "ebay"
    brand_3 = "olx"

class Product(Brands):
    prod_1 = "online ecommerce store"
    prod_2 = "online store"
    prod_3 = "online buy sell store"

obj_1 = Product()
print(obj_1.brand_1 + " is an " + obj_1.prod_1)
print(obj_1.brand_2 + " is an " + obj_1.prod_2)
print(obj_1.brand_3 + " is an " + obj_1.prod_3)
