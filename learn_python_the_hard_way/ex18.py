def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "args: %r" % arg1

def print_none():
	print "I got nothing'."

print print_two("yuan", "ridan")
print print_two_again("ridan", "yuan")
print print_one("First!")
print print_none()