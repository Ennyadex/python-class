class Fruit(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def display(self):
        print(self.name)
        print(self.color)
    def details(self): 
        print("fruit name is {}" .format(self.name))
        print("fruit color is {}" .format(self.color))

class Orange(Fruit):
    
    def __init__(self,name,color,taste,edible,size):
        self.taste = taste
        self.edible = edible
        self.size = size
        Fruit.__init__(self,name,color)
    
    def details(self):
        print("fruit name is {}".format(self.name))
        print("fruit color is {}".format(self.color))
        print("fruit taste is {}".format(self.taste))
        print("fruit is edible {}".format(self.edible))
        print("fruit size is {}".format(self.size))

f1 = Orange("orange","yellow","sweet","yes","small")
f1.details()