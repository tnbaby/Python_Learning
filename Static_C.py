class Kls(object):
	def __init__(kls, data):
		kls.data = data
	def printd(kls):
		print kls.data
	@staticmethod
	def smethod(*arg):
		print 'Static:', arg
	@classmethod
	def cmethod(*arg):
		print "Class:", arg
ik = Kls(23)
ik.printd()
ik.smethod()
ik.cmethod()
