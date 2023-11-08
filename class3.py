class Fruit():
    def __init__(self,**kwargs):
        self.color = kwargs['c']
        self.size = kwargs['s']
        print(self.color)
        print(self.size)
apple = Fruit(c ="green",s ="small")
banana = Fruit(c ="yellow",s ="small")
watermelon = Fruit(c ="green",s ="big")
orange = Fruit(c = "yellow",s ="small")
mango = Fruit(c ="red",s = "big")