#Q6.Write a python program to create two lists and join the second list with the first, then display the resultant list.
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using + operator to concat
list1 = list1 + list2
# Printing concatenated list
print("Concatenated  : "
      + str(list1))
