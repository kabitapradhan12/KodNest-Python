#no input and no output
def square():
    n=5*5
    print(n)
square()
print("\n")
#no ip and with op
def square():
    n=5*5
    return n
print(square())
print("\n")
#with in and no op
def square(n):
    res=n*n
    print(res)
square(5)
print("\n")

#with in and with op
def square(n):
    res=n*n
    return res
print(square(5))
print("\n")
