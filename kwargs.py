def name(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key,value))
name(fn = "ayo", ln = "shade", age ="85", state = "oyo" )