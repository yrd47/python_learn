the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

for x in xrange(0,6):
	print "Adding %d to the list." % x
	elements.append(x)

for x in elements:
	print "Element was: %d" % x