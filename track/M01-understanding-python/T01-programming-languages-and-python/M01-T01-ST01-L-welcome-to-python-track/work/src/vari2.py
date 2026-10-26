def add():
    a=10 #global variable 
    b=20 #local variable

    print(a+b)
add()

x=100 #global
def display():
    x=50 #local
    print("Local value of x is",x) #50
display()
print("Global value of x is",x) #100

x=10
def display():
    print(x) #10
    a=20
    print(a) #20
display()
x=30
print(x) #30