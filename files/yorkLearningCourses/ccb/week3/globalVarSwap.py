x = 10
y = 20

print ("x = ", x, " y = ", y)

def swap():
	"""swap x and y as global variables """

	pass
	

swap()
print ("x = ", x, " y = ", y)


x = 10
y = 20
print ("x = ", x, " y = ", y)

def swap2(a, b):
	""" swap two parameters and return them """
	
	return a, b

x, y = swap2(x, y)

print ("x = ", x, " y = ", y)
