# -*- coding: utf-8 -*- 
#更多的变量和打印
#格式化字符串（format String）

my_name = "yrd"
my_age = 22 # not a lie
my_height = 173
my_weight = 160
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s delending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)