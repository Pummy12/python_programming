a,b=map(int,input("Enter two numbers: ").split())
power = 1
for i in range(1,b+1):
    power*=a
print("The value of a^b is: ",power)