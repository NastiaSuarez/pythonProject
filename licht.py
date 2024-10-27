my_dict = {"Alex": 1968, "Vanya":1985, "Sasha":1986, "Andrey": 1988}
print(my_dict)
print(my_dict ['Alex'])
print(my_dict.get ('Hugh'))
my_dict.update({"Timur":1994, "Nikita": 1989 })
print(my_dict)
l = my_dict.pop("Andrey")
print(l)
print(my_dict)

my_set = {1, 1, 23.4, True, "Andre", True, "Andre", 23.4, (1,3,5)}
print(my_set)
print(my_set.add(345.67))
print(my_set.add(1234))
print(my_set.remove("Andre"))
print(my_set)