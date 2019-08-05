print("HELLO WORLD.")

x=5
y="Automation"
print(x)
print(y)
print("Hello"+y)

x=10
y=20
print(x+y)

if 10>5:
    print("10 is greater than 5")

def sum(a,b):
    print(a+b)                #ctrl+/ turns the code set into comment
x = sum(20,30)

x=5
y=2.5
z=4j
print(type(x))
print(type(y))
print(type(z))

#casting
x=int(2)        #output: 2
y=int(2.5)      #output: 2
z=float(1)      #output: 1.0
p=str(10)       #output: "10"

print(x)
print(y)
print(z)
print(p)

x="Hello Example 1"
print(x)
print(x[1])
print(x[6:13])
print(len(x))
print(x.lower())
print(x.upper())

y="    Hello Example 2...   "
print(y.strip())
print(y.replace("e","a"))
print(y.split(","))

print("Enter your name:")
x=input()
print("Hello, "+x)
