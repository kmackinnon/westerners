#!/usr/bin/python
import cgi
import cgitb; cgitb.enable() # enable debugging mode
import csv

form = cgi.FieldStorage()

coins=int(form.getvalue('coins'))

Inventory1=form.getvalue("Inventory1")
Inventory2=form.getvalue("Inventory2")
Inventory3=form.getvalue("Inventory3")
Inventory4=form.getvalue("Inventory4")
Inventory5=form.getvalue("Inventory5")

InventoryList=[Inventory1,Inventory2,Inventory3,Inventory4,Inventory5]

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Westerner's Room Page </title>"
print """<link rel="stylesheet" type="text/css" href="roomstyle.css">"""
print '</head>'
print '<body>'

#TO DO:
	#Change the parameter here to a List, no a "Listing" as it is here. That will resolve logic issues hopefully
def printPage(coins, Inventory1, Inventory2, Inventory3, Inventory4, Inventory5):
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
        print """<input type="hidden" name="Inventory1" value=" """,Inventory1,""" ">"""
        print """<input type="hidden" name="Inventory2" value=" """,Inventory2,""" ">"""
        print """<input type="hidden" name="Inventory3" value=" """,Inventory3,""" ">"""
        print """<input type="hidden" name="Inventory4" value=" """,Inventory4,""" ">"""
        print """<input type="hidden" name="Inventory5" value=" """,Inventory5,""" ">"""

        print "<!-- CGI which implements game activity and submit button -->"
        print "I have roads but no cars.</br>"
        print "I have lakes but no fish.</br>"
        print "What am I? </br></br>"
        print """Answer: <input type="text" name="answer" method="post" maxlength="5">"""
        #this is what will use the updated coins value to update the page
        print """<input type="hidden" name="coins" value=" """,coins,""" "> """
        print """<input type="hidden" name="select" value="riddle">"""
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print """<form name="command" action="game.py" method="post">"""
        print """<!--Hidden tags for inventory -->"""
        print """<input type="hidden" name="Inventory1" value=" """,Inventory1,""" ">"""
        print """<input type="hidden" name="Inventory2" value=" """,Inventory2,""" ">"""
        print """<input type="hidden" name="Inventory3" value=" """,Inventory3,""" ">"""
        print """<input type="hidden" name="Inventory4" value=" """,Inventory4,""" ">"""
        print """<input type="hidden" name="Inventory5" value=" """,Inventory5,""" ">"""

        print """<!-- CGI that implements the game commands -->"""
        print """Command: <input type="text" name="command" method="post" maxlength="10">"""
        #I pass in the coins again too.
        print """<input type="hidden" name="coins" value =" """,coins,""" "> """
        print """<input type="hidden" name="select" value="command">"""
        print """<input type="submit" value="Command">"""
        print """</form>"""
        
        print"</br>"


#Now I have to handle the two forms

#this handles if a user enters an answer
select=form.getvalue("select")

if select=="riddle":
	
        #get the user's answer to the riddle and convert to lowercase
        answer=form.getvalue("answer").lower()
        #If a user has coins, they can interact.
        if coins!=0:
                # loop through answer and find substring "map"
                if "map" in answer:
                        coins+=10
                        printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)
                        print '<font color="green"><p>That is correct! You have earned 10 more coins. You have',coins,' coins!</p></font>'
                
		else:
                        coins-=10
                        printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)
                        print '<font color="red"><p> You gave the wrong answer. You have lost 10 coins. You have',coins,' coins!</p></font>'
  
	#if a user has no coins, they cannot interact.
        else:
                printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)

#this handles if a user enters a command.        
elif select=="command":

        command = form.getvalue("command").lower()

        if command == "look":
                printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)
		file='inventory.csv'
		f=open(file, 'r')
		count=1
    		for line in f:
			print count,"."
        		print line
			print "</br>"
			count+=1

	#get all the inventory data and save to each inventory number 
	
        elif command[:6] == "pickup":
                num = int(command[7:])
                # remove n items from inventory and add it to first hidden inventory slot
                # if there are no slots available, error message and item should not be removed from csv.
                # room redisplayed

        elif command[:4] == "drop":
		num = int(command[5:])
		print InventoryList[num-1]
		if 1<=num<=5:
                	if InventoryList[num-1] is not None:
				file='inventory.csv'
				beginning=InventoryList[num-1]
				end="\n"
				insert=beginning+end
				f=open(file,'ab').write(insert)
				InventoryList[num-1]=""
				printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)
				print "Item was dropped!"
			else:
				print "<p> No item to drop!</p>"
				
		else:
			print "Please enter a valid pickup number from 1-5."
                

        elif command == "inventory":
		printPage(coins,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5)
                print "1.", Inventory1
		print "</br>"
		print "2.", Inventory2
		print "</br>"
		print "3.", Inventory3
		print "</br>"
		print "4.", Inventory4
		print "</br>"
		print "5.", Inventory5
                # displays the items the user has to the screen
                # room redisplayed


print '</body>'
print '</html>'

	
