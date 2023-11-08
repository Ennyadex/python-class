class Areaofcircle:
    def __init__(self,pi,rad):
        self.p = pi
        self.r = rad
    def cal(self):
        area = self.p * self.r * self.r
        print(f"area is {area}")
myarea = Areaofcircle(3.142,21)
myarea.cal()