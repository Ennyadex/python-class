import math
def alm(a,b,c):
   
    m = b * b - 4 * a * c
    x1 = ((-b) + math.sqrt(m)) / 2 * a
    x2 = ((-b) - math.sqrt(m)) / 2 * a
    print(f" x1 = {x1} and x2 = {x2}")

alm(4,-11,-21)