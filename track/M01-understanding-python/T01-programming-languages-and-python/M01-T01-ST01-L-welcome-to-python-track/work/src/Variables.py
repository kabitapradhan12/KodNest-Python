name="Kabita"
age=23
print(name)
print(id(name))
print(type(name))

print("Hello Python",end=" -")
print("Thank you python")

print("Hello Python \nThank you python")

print("My name is" + name + "my age "+str(age))
#string formatting
print(f"My nameis {name} and my age is {age}")


a=10
b=20
c=30
print(a+b+c)

a=b=c=10
print(a+b+c)

a, b, c="Abhi","Ram","Sita"
print(a+b+c)

x,y,z=30,4,8
print(x+y) # 38
print(a+str(x)) # Abhi38
print(b+c) # RamSita
print(a , x) #Abhi 30

a=10
print(type(a),a)