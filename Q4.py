#Write a python program to split the given list into 3 sub-lists as per your requirement.
import numpy as np

ints = [1,2,3,4,5,6]

splits = np.array_split(ints, 3)

for array in splits:
    print((array))
