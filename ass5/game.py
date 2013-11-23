#! usr/bin/python

import sys

#get the user's answer to the riddle and convert to lowercase
answer = raw_input("Enter answer to riddle: ").lower() 

# loop through answer and find substring "map"
for i in range(len(answer)-2):
	if answer[i:i+3] == "map":
		print "Success!"
		sys.exit(0)
print "Try Again"



