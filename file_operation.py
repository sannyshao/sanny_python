from sys import argv
from os.path import exists

script, filename, to_file = argv

print "We are going to erase %r. " % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit return."

raw_input('?')

print "Opening the file for write"
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And we close it."
target.close()

print "copying from %s to %s" % (filename, to_file)
# we could do these two on one line, how?
in_file = open(filename)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print "Opening the out_file for read"
copy_file = open(to_file, 'r')
print copy_file.read()

