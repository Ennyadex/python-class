class Person(object):
    def __init__(self,name,id): 
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
    def details(self):
        print("my name is {}". format(self.name))
        print("my id is {}". format(self.id))

class Emp(Person):
 
   def  __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,id)
    
   def details(self):
    print("my name is {}".format(self.name))
    print("id is {}".format(self.id))
    print("salary is {}".format(self.salary))
    print("post is:{}".format(self.post))

p2 = Emp("eniola","12","1000000","data analyst")
p2.details()
