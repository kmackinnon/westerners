#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()   # enable debugging mode

form = cgi.FieldStorage() 

coins=int(form.getvalue('coins'))

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print coins


#get the user's answer to the riddle and convert to lowercase
temp = form.getvalue("answer")
answer=temp.lower()
print answer


# loop through answer and find substring "map"
for i in range(len(answer)-2):
        if answer[i:i+3] == "map":
                coins+=10
		print '<p>You did it! You have',coins,' coins!</p>'
	else:
		coins-=10
		print '<p> You gave the wrong answer. You have',coins,' coins!</p>'
		break
	
print '</body>'
print '</html>'

