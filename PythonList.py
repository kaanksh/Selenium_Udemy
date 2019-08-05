#LIST[] are ordered, indexed, changeable, duplicates
my_list = ["Tokyo", "London", "New York"]
print(my_list)
print(my_list[1])

my_list[2]= "New Delhi" #change elements
print(my_list)

for val in my_list:
    print(val)

print(len(my_list))

my_list.append("Berlin")    #add new ele
print(my_list)
my_list.insert(4,"Durham")
print(my_list)

my_list.remove("Tokyo")     #remove ele
print(my_list)
my_list.pop()   #removes last ele in the list
print(my_list)
my_list.pop(1)
print(my_list) #remove acc to index position
del my_list[1]
print(my_list)


fruits= ["apples", "oranges", "cherry"]
print(fruits)
fruits.reverse()
print(fruits)


my_list_2 = ["apples", 1,2,3.0] #nested lists
my_list_3 = ["apples", [1,2,3,], ['a','b','c']]
print(my_list_3)
print(my_list_3[1][1]) #list in list index
