def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)

#factorial
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)
print(facto(5))

#fibbonaci series 
def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
print(fibbo(5))
