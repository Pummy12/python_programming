#Python Program to find the largest number using max() function
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
# We can also take the input in one line
# n1, n2, n3 = input("Enter three numbers: ").split()
print(max(n1, n2, n3), "is the largest among all the three numbers")