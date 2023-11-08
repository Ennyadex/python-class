def myFun(*args):
    for a in args:
        print(a)
myFun("bayo","jenifer","andy","eni","tom","sewa")

def myFun1(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
myFun1(firstname = "Bayo",lastname = "Akin")