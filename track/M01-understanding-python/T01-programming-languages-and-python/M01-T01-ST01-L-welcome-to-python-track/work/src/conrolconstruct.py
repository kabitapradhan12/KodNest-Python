#check positive number
a=10
if a>0:
    print("Positive Number")

#eligible for blood donation
age=20
if(age>=18):
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")

#temp above 10c print "Hot day"age
temp=45
if(temp>=30):
    print("Hot Day")

#student attendent at least 75% of classes
attend=68
if(attend>=75):
    print("Student has attended 75% of classes")
else:
    print("Student has not attended 75% of classes")
#even or odd
a=13
if(a%2==0):
    print("Even Number")
else:
    print("Odd Number")
#a person is eligible for driveing licenses
age=45
if(age>=18 and age<=60):
    print("Eligible for Driveing Licenses")
else:
    print("Not Eligible for Driveing Licenses")
#given year is leap year or not
year=2005
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
#compare 2 number and print largest one
a=20
b=30
if(a>b):
    print("a is greater")
else:
    print("b is greater")
#Assing grades based on marks
mark=65
if(mark>=90 and mark<=100):
    print("Grade is A")
elif(mark>=80 and mark<90):
    print("Grade is B")
elif(mark>=70 and mark<80):
    print("Grade is C")
elif(mark>=60 and mark<70):
    print("Grade is D")
else:
    print("Grade is Fail")
#catagorize electricity usage
usage=78
if(usage>=500):
    print("High")
elif(usage>=301 and usage<500):
    print("Medium")
elif(usage>=101 and usage<300):
    print("Low")
else:
    print("Very Low")
#Scholarship eligibility
mark=87
family_income=200000
if(mark>=85 and family_income<=300000):
    print("Eligible for scholarship")
else:
    print("Not Eligible for scholarship")

#user login



#display dayusing numbers(1-7)
n = 6

match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")
#display season based on month
month = "nov"

match month:
    case "dec" | "jan" | "feb":
        print("Winter")
    case "mar" | "apr" | "may":
        print("Summer")
    case "jun" | "jul" | "aug" | "sep":
        print("Rainy")
    case "oct" | "nov":
        print("Autumn")
    case _:
        print("Invalid month")

#print umber from 1 to 20
for i in range(21):
    print(i)

#multiplication tablr for a number
num=4
for i in range(11):
    print(i*num)

#print number from 10 to 1
i=10
while i>0:
    print(i)
    i-=1

#find factorial of a number

while i > 0:
    a = a * i
    i -= 1
print(a)
#print number 1 to 20 but stop at 15
for i in range(1, 21):
    if i == 15:
        break
    print(i)

#search for a number in a list using break
list=[1,2,3,4,5,6,7,8,9,10]
search=8
for i in list:
    if i==search:
        print("Found")
        break
    print(i)

#print number from 1 to 20 ,skippig multiple of 3 using continue
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)    
#print odd numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)   

#find the cube of a number using for loop using function call and 
def cube(n):
    return n*n*n
for i in range(1, 11):
    print(cube(i))   
#find the maximum of two numbers using function and 
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(10,20))  

#create an empty function named display() using pass statement
def display():
    pass
display()

    

    