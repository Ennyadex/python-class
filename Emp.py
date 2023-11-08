import Person

class Emp(Person):
 
   def  __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,id)
    
   def details(self):
        print("name is {}".format(self.name))
        print("id is {}".format(self.id))
        print("post is:{}".format(self.post))
