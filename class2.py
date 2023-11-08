class Person:
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def __str__(self):
        return f"{self.n} and {self.a}"
p1 = Person("ayo","100")
print(p1)