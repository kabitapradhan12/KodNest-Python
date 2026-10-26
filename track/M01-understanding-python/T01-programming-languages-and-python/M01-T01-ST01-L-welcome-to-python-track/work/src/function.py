#addition
def add():
    a=10
    b=20
    print(a+b)
add()
#check square
def square():
    a=10
    print(a*a)
square()

#largest number
def largest():
    a=10
    b=20
    c=30
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print(largest())

print("\n")
#check even or odd
def even():
    num=int(input("Enter a number to check: "))
    if num%2==0:
        print("even")
    else:
        print("odd")

even()



