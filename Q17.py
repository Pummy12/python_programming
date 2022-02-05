#Q17. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {12: 'sun', 13: 'moon', 2: 'star', 6: 'planet', 10: 'Meteoroids'}
print("dictionary:", my_dict)
all_values = my_dict.values()
max_value = max(all_values)
print("the maximum value is:", max_value)
min_value = min(all_values)
print("the minimum value is:",min_value)
