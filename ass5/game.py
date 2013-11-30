
#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()   # enable debugging mode

form = cgi.FieldStorage() 

coins=int(form.getvalue('coins'))

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Westerner's Room Page </title>"
print """<link rel="stylesheet" type="text/css" href="roomstyle.css">"""
print '</head>'
print '<body>'


def printPage(coins):
	#this will regenerate the page
	print """<div id = "header">"""
	print '<h1> The Room </h1>'
	print '</div>'
	print '<!--Display the room -->'
	print """<div id="main">"""
	print """<a href="http://www.cs.mcgill.ca/~eraso/Grid.html" class="top">North</a></br>"""
	print """<a href="http://cs.mcgill.ca/~cmacdo40/room.html" class="left">West</a></br>"""
	print """<a href="http://www.cs.mcgill.ca/~aturne15/room.html" class="right">East</a></br>"""
	print """<a href="http://cgi.cs.mcgill.ca/~phende/comp206/room.html" class="bottom">South</a></br>"""
	print "</div>"

	print """<form name="game" action="game.py" method="post">"""
	print "<!-- Hidden tags for inventory -->"
	print """<input type="hidden" name="Inventory1" value="">"""
	print """<input type="hidden" name="Inventory2" value="">"""
	print """<input type="hidden" name="Inventory3" value="">"""
	print """<input type="hidden" name="Inventory4" value="">"""
	print """<input type="hidden" name="Inventory5" value="">"""

	print "<!-- CGI that which implements game activity and submit button -->"
	print "I have roads but no cars.</br>"
	print "I have lakes but no fish.</br>"
	print "What am I? </br></br>"
	print """Answer: <input type="text" name="answer" method="post" maxlength="10">"""
	#this is what will use the updated coins value to update the page
	print """<input type="hidden" name="coins" value=" """,coins,""" "> """
	print """<input type="submit" value="Submit">"""
	print "</form>"

	print """<form name="goNorth" action="http://www.cs.mcgill.ca/~eraso/Grid.html" method="post">"""
	print """<input type="hidden" name="points" value="0">"""
	print """<input type="hidden" name="Inventory1" value="">"""
	print """<input type="hidden" name="Inventory2" value="">"""
	print """<input type="hidden" name="Inventory3" value="">"""
	print """<input type="hidden" name="Inventory4" value="">"""
	print """<input type="hidden" name="Inventory5" value="">"""

	print "<!-- and the top button -->"
	print "</form>"

	print """<form name="goWest" action="http://cs.mcgill.ca/~cmacdo40/room.html" method="post">"""
	print """<input type="hidden" name="points" value="0">"""
	print """<input type="hidden" name="Inventory1" value="">"""
	print """<input type="hidden" name="Inventory2" value="">"""
	print """<input type="hidden" name="Inventory3" value="">"""
	print """<input type="hidden" name="Inventory4" value="">"""
	print """<input type="hidden" name="Inventory5" value="">"""

	print "<!-- and the left button -->"
	print "</form>"

	print """<form name="goEast" action="http://www.cs.mcgill.ca/~aturne15/room.html" method="post">"""
	print """<input type="hidden" name="points" value="0">"""
	print """<input type="hidden" name="Inventory1" value="">"""
	print """<input type="hidden" name="Inventory2" value="">"""
	print """<input type="hidden" name="Inventory3" value="">"""
	print """<input type="hidden" name="Inventory4" value="">"""
	print """<input type="hidden" name="Inventory5" value="">"""

	print """<!-- and the right button -->"""
	print "</form>"

	print"""<form name="goSouth" action="http://cgi.cs.mcgill.ca/~phende/comp206/room.html" method="post">"""
	print """<input type="hidden" name="points" value="0">"""
	print """<input type="hidden" name="Inventory1" value="">"""
	print """<input type="hidden" name="Inventory2" value="">"""
	print """<input type="hidden" name="Inventory3" value="">"""
	print """<input type="hidden" name="Inventory4" value="">"""
	print """<input type="hidden" name="Inventory5" value="">"""

	print"<!-- and the bottom button -->"
	print"</form>"
	
	print"</br>"


#Now I have to handle the two forms

#This will handle if a user puts in an answer
select=form.getvalue("select")
if select=="riddle":

	#get the user's answer to the riddle and convert to lowercase
	temp = form.getvalue("answer")
	answer=temp.lower()

	#If a user has coins, they can interact.
	if coins!=0:
		# loop through answer and find substring "map"
		for i in range(len(answer)-2):
			if answer[i:i+3] == "map":
				coins+=10
				printPage(coins)
				print '<font color="green"><p>That is corrent! You have earned 10 more coins. You have',coins,' coins!</p></font>'
			else:
				coins-=10
				printPage(coins)
				print '<font color="red"><p> You gave the wrong answer. You have lost 10 coins. You have',coins,' coins!</p></font>'
				break

	#if a user has no coins, they cannot interact.
	else:
		printPage(coins)

#this handles if a user puts in a command.	
elif select=="command":

	command = form.getvalue("command").lower()

	if command == "look":
		print command
		# display inventory in csv by index

	elif command[:6] == "pickup":
		num = int(command[7:])
		# remove n items from inventory and add it to first hidden inventory slot
		# if there are no slots available, error message and item should not be removed from csv.
		# room redisplayed

	elif command[:4] == "drop":
		num = int(command[5:])
		# item in Inventorynum would be removed ""
		# item added to Inventory.csv

	elif command == "inventory":
		print "blah"
		# displays the items the user has to the screen
		# room redisplayed

print '</body>'
print '</html>'
		
	
