x = input("input a number: ")
i=0
j=len(x)-1

while i<j:
    if x[i]!=x[j]:
        print("not palindrome")
        exit(0)
    i+=1
    j-=1
print("palindrome")