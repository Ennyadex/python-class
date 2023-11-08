person = {"name":"eniola","age":"15","id":"4","profession":"data analyst"}
sort_person = sorted(person.items(),key = lambda item:item[1])
person = dict(sort_person)
print(person)