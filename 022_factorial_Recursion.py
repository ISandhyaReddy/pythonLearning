def fact(n):
    if n==0:
        return 1
    else:
        b=n*fact(n-1)
        return b
n=int(input("enter a value: "))
a=fact(n)
print(a)