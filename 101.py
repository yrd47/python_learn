print 'Hello World'

name = 'shell'
print('my name is {0} and the length of name is {1}'.format(name, len(name)))
print('my name is %s and the length of name is %d' % (name, len(name)))

print '------------'

a = 1
if a == 1:
	print 'ok'
print 'done'

print '------------'

try:
	input = raw_input
	pass
except NameError:
	pass

number = 23

running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
print('Done')

print '------------'

for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')