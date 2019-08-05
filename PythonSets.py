#sets {} are unordered, unindexed, no duplicates

my_set={"Chalk", "Duster", "Board"}
print(my_set)
# print(my_set[1]) won't work
for x in my_set:
    print(x)
print("Chalk" in my_set)   #true

my_set.add("Pen") #add ele
print(my_set) #can be added anywhere randomly because unordered set
my_set.update(["Pencil", "Eraser"])
print(my_set)

len(my_set)

my_set.remove("Pencil")   #remove ele
my_set.discard("Pen")     #discard
print(my_set)
# when unsure of that ele to be removed is present in the set or not, use discard instead of remove for error free code
my_set.pop()
my_set.clear()
print(my_set)
del my_set


my_set_2 = {"Apples", 1,2, (3,4,5)}
print(my_set_2)
my_list = [1,2,3]
print(my_list)
my_set_3 = set(my_list) #convert list to a set
print(my_set_3)


# UNION|INTERSECTION|DIFF.|SYMMETRIC DIFF.

A={'A','B',1,2,3}
B={'B','C',3,4,5}

print(A.union(B))
#or
print(A|B)


print(A.intersection(B))
print(A&B)


print(A.difference(B))
print(A-B)


print(A.symmetric_difference(B))
print(A^B)