class Car():
    def __init__(self,**kwargs):
        self.color = kwargs['c']
        self.speed = kwargs['s']
toyota = Car(c = "red",s = "100km/hr")
honda = Car(c = "green",s = "280km/hr")
print(toyota.color)
print(toyota.speed)
print(honda.color)
print(honda.speed)