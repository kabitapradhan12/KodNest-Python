c=30
def add():
    global a
    a=10
    b=20
    print(a+b)
    print(c) #global variable
add()


x=100 #global variable
def display():
    x=50 #local
    print("Local varibale",x) # 50
display()
print("Global variable x:",x) #100





