class Car:
    def __init__(self, name):
        self.m = name

    def move(self):
        print("car moves")
        
    def stop(self):
        print("car stops")

car = Car("hi")
car.move()
car.stop()
