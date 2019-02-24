def variable_function(*args, **kwargs):
	print 'args:', args
	print 'kwargs:', kwargs

variable_function('simple')
args: ('simple')
kwargs: {}

variable_function(type='Complex')
args: ()
kwargs: {'type': 'Complex')

def mixed_function(a, b, c=None, *args, **kwargs):
	print '(a, b, c):', (a, b, c)
	print 'args:', args
	print 'kwargs:', kwargs

mixed_function(1,2,3,4,5, d=10, e=20)
(a, b, c): (1,2,3)
args: (4,5)
kwargs: {'e':20, 'd':10}




