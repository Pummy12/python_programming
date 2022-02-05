#Q15. Write a Python program to map two lists into a dictionary.
keys=['red','yellow','green']
values=[1,2,3]
print("first list:",keys)
print("second list:",values)
dictionary=dict(zip(keys,values))
print("dictionary formed:",dictionary)
