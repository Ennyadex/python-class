class Data:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
x = Data("john","femi")
x.printname()

class Information(Data):
    pass