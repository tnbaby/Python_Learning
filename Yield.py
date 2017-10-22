import time

CONSTENT = 1000000

def fab(max):
	a, b = 0, 1 
	for i in xrange(max):
		yield b
		a, b = b, a + b
def fab1(max):
	a, b = 0, 1
	for i in xrange(max):
		pass
		a, b = b, a + b

start = time.time()
for n in fab(CONSTENT):
	pass
end = time.time()
print "iterable: ", (end - start)
start = time.time()
fab1(CONSTENT)
end = time.time()
print "common way: ", (end - start)
