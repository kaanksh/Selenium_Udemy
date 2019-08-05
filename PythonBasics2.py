if 5>3 :
    print("5 is greater than 3.")

num=0
if num>0:
    print("This is a +ve number.")
elif num==0:
    print("Number is 0.")
else :
    print("This is a -ve number.")

num=[1,2,3,4,5]
sum=0
for val in num:
    print(val)
    sum=sum+val
print("Total is ",sum) # , is used instead of + for concatenating string w number

fruits=["Apple", "Oranges", "Grapes"]
for val in fruits:
    print(val)
else:
    print("No other fruits left.")

print("Enter a number:")
num=int(input())  #'int(input())' used instead of 'input()' because of typecasting issues
sum=0
i=1
while i<num:
    sum=sum+i
    i=i+1
print("Total is", sum)

