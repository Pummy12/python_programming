x = input("input a number: ")
a=int(x)
b=0
for i in range(len(x)):
    b+=(int(x[i])**len(x))
if a==b:
    print("Given number is Narcissistic number")
else:
    print("given number is not Narcissistic number")