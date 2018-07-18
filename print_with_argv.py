from sys import argv 
script,first, second, third = argv

print " Your information is as follows: "
a = raw_input("Please enter your %s " % first)
b = raw_input("Please enter your %s " % second)
c = raw_input("Please enter your %s " % third)

print "So, your %s is %s, your %s is %s, your %s is %s." % (first, a, second, b, third, c)
 

