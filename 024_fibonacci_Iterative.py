num=int(input("enter a number: "))
a=0
b=1
count=0
if num==0:
    print(a)
elif num<0:
    print("negative")
else:
    while count<num:
        count=count+1
        print(a)
        a,b=b, a+b