#Q8.Write a python program to convert a tuple to a string.
def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str
tuple = ('p', 'u', 'm', 'm', 'y')
str = convertTuple(tuple)
print(str)
