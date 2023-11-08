class Simpleinterest:
    def __init__(self,pr,rate,time):
        self.p = pr
        self.r = rate
        self.t = time
    

    def cal(self):
        si = (self.p * self.r * self.t) / 100
        print(f"simple interest is {si}")
p = input("interest: ")
k = input("rate: ")
b = input("Time: ")

simple = Simpleinterest(float(p),float(k),float(b))
simple.cal()