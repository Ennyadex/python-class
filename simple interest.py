print("program for solving simple interest")
p = input("enter principal value: ")
r = input("enter rate value: ")
t = input("enter time value: ")
si = (float(p) * float(r) * float(t))/100

print("simple interest with principal of ",p, " at rate of ",r," and time of ",t, "is ",  si)