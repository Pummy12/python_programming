n = int(input("Enter the value of n: "))
if n==1 or n==2:
    print(1)
    exit(0)
a=1
b=1
n-=2
for i in range(n+1):
    c=a+b
    n-=1
    if n==0:
        print(c)
        exit(0)
    b=a
    a=c