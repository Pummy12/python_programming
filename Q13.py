#Q13. WAP to Creating Python Dictionary, Accessing Elements from Dictionary,Changing and Adding Dictionary elements, Removing elements from Dictionary
my_dict={1:'Apple',2:'Mango',3:'Banana',4:'Grapes',5:'Cherry'}
print("Accessing key values from the dictionary:")
print(my_dict.keys())
print(my_dict.values())
print("Changing 1st element:")
my_dict[1]='Guava'
print(my_dict)
print("Adding new elements:")
my_dict[6]='Strawberry'
my_dict[7]='Lichi'
print(my_dict)
print("Removing 3rd element:")
my_dict.pop(3)
print(my_dict)
