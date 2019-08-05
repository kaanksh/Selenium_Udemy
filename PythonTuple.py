#tuple () are ordered, indexed, unchangeable, duplicates
my_tuple=("Apples", "Oranges", "Grapes")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1]) #- index strats from last ele
print(my_tuple[0:2])

for val in my_tuple:
    print(val)
# my_tuple[1]="Cherry" won't work because unchangeable
del my_tuple
# del my_tuple[2] wont work


my_tuple_2= ("Banana", (1,2,3), ["Tokyo", "New Delhi"])
print(my_tuple_2) # nested tuple+list combo
print(my_tuple_2[2][1])
my_tuple_2[2][1]= "New York"
print(my_tuple_2) #change new delhi to new york
print("Banana" in my_tuple_2) #true
print("Cherry"in my_tuple_2)  #false



