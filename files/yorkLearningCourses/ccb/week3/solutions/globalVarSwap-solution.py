x = 10
y = 20

print ("x = ", x, " y = ", y)

def swap():
	"""swap x and y as global variables """

	#Need this for it to work
	global x, y
	temp = x
	x = y
	y = temp
	

swap()
print ("x = ", x, " y = ", y)


x = 10
y = 20
print ("x = ", x, " y = ", y)

def swap2(a, b):
	""" swap two parameters and return them """
	temp = a
	a = b
	b = temp
	
	return a, b

x, y = swap2(x, y)

print ("x = ", x, " y = ", y)
