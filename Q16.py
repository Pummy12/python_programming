#Q16. Write a Python program to sort a given dictionary by key.
my_dict={12:'sun',13:'moon',2:'star',6:'planet',10:'Meteoroids'}
print("dictionary:",my_dict)
print("Sorting with respect to key elements:")
for key in sorted(my_dict):
    print(key,":",my_dict[key])
