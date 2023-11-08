def fun(p1,p2,p3):
    print(p1,p2,p3)
all = ("python","php","java")
fun(*all)

def good(** lang):
    for x,y in lang.items():
        print("%s == %s" %(x,y))
good(l1 = "python", l2 = "php",l3 ="java")