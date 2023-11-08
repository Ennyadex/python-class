mytuple = ("ola","sewa","jenny","femi","kenny","ojo","betty","lizzy","dammy","lola")
mylist = list(mytuple)
mylist.sort()
mytuple = tuple(mylist)
for x in mytuple:
    print(x, end = ", ")