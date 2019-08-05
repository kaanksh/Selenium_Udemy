#Dictionary {K:V} are unordered, indexed, changeable, no duplicates

my_dict={
    "class" : "animal",
    "name"  : "giraffe",
    "age"   : 10
}
print(my_dict)
print(my_dict.values())


print(my_dict["name"])
print(my_dict.get("age"))

for x in my_dict:
    print(my_dict[x])

for x,y in my_dict.items():
    print(x,y)

my_dict["name"]="elephant" #change
print(my_dict)

my_dict["color"] = "grey" #new value
print(my_dict)

my_dict.pop("color")

print(my_dict)     #remove
my_dict.popitem()
print(my_dict)

del my_dict["class"]
print(my_dict)

my_dict.clear()
print(my_dict)
del my_dict