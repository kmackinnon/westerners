#!/usr/bin/python
import cgi
import cgitb; cgitb.enable() # enable debugging mode
import csv
import os, sys

form = cgi.FieldStorage()

if form.getvalue('coins') is not None:
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

for i in range(len(InventoryList)):
	if InventoryList[i] == "None":
		InventoryList[i]=""

# regenerates the page
def printPage(coins, InventoryList):
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
        print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
        print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
        print """<input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
        print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
        print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""
        print "<!-- CGI which implements game activity and submit button -->"
        print "I have roads but no cars.</br>"
        print "I have lakes but no fish.</br>"
        print "What am I? </br></br>"
        print """Answer: <input type="text" name="answer" method="post" maxlength="5">"""
        #updates coins value to update the page
        print """<input type="hidden" name="coins" value=" """,coins,""" "> """
        print """<input type="hidden" name="select" value="riddle">"""
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print """<form name="command" action="game.py" method="post">"""
        print """<!--Hidden tags for inventory -->"""
        print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
        print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
        print """<input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
        print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
        print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""
        print """<!-- CGI which implements the command -->"""
        print """Command: <input type="text" name="command" method="post" maxlength="10">"""
        #pass in the coins again too.
        print """<input type="hidden" name="coins" value =" """,coins,""" "> """
        print """<input type="hidden" name="select" value="command">"""
        print """<input type="submit" value="Command">"""
        print """</form>"""
        
        print"</br>"


#Now have to handle the two forms
select=form.getvalue("select")

# if the user tries to answer the riddle
if select=="riddle":
	#get the user's answer to the riddle and convert to lowercase
    answer=form.getvalue("answer").lower()
    #If a user has coins, they can interact.
    if coins != 0:
        # loop through answer and find substring "map"
        if "map" in answer:
            coins+=10
            printPage(coins,InventoryList)
            print '<font color="green"><p>That is correct! You have earned 10 more coins. You have',coins,' coins!</p></font>'
        else:
            coins-=10
            printPage(coins,InventoryList)
            print '<font color="red"><p> You gave the wrong answer. You have lost 10 coins. You have',coins,' coins!</p></font>'
	#if a user has no coins, they cannot interact.
    else:
        printPage(coins,InventoryList)

# if the user enters a command       
elif select=="command":
	command = form.getvalue("command").lower()
	
	# look which prints out the inventory from the csv file
	if command == "look":
		printPage(coins,InventoryList)
		file='inventory.csv'
		f=open(file, 'r')
		count=1
		for line in f:
			print count,"."
			print line
			print "</br>"
			count+=1
	
	# pickup which removed inventory from the csv and adds it to available inventory slot
	elif command[:6] == "pickup":
		num = int(command[7:])
		maxLine=0
		f=open('inventory.csv', 'r')
		for line in f:
			maxLine+=1

		if num>maxLine or num<=0:
			printPage(coins,InventoryList)
			print '<font color="red">Not a valid pickup choice.</font></br>'
			print '<font color="red">Enter a number from 1 to ',maxLine,'</font>'
		else:
			emptySlot=False 
			slot=0
			for i, val in enumerate(InventoryList):
				if val is None:
					emptySlot=True
					slot=i
					break
			if not emptySlot:
				printPage(coins,InventoryList)
				print '<font color="red">Your inventory is full right now. Please drop something first.</font>'
			else:
				file='temporary.csv'
				f1=open(file,'w+')
				file='inventory.csv'
				f2=open(file,'r')
				#f1 is the new file to write to, f2 is the old file to read from
				linecount=0
				for line in f2:
					linecount+=1
					if linecount!=num:
						f1.write(line)
					#If I'm here, desired line in the inventory.csv has been reached					
					else:
						InventoryList[slot]=line
					
				#Entire file has been read. Now can copy temporary.csv into the inventory.csv file.	
				os.remove('inventory.csv')		
				os.rename('temporary.csv','inventory.csv')
				printPage(coins,InventoryList)
				print "You have added",InventoryList[slot],"to your inventory.</br>"
				print "It is located at inventory slot",slot+1,"." # inventory starts at 1
	
	# drop which allows users to drop items in our room
	elif command[:4] == "drop":
		num = int(command[5:])
		if 1<=num<=5:
			if InventoryList[num-1]: #enters if statement when not None
				file='inventory.csv'
				f=open(file,'ab')
				f.write(str(InventoryList[num-1]))
				f.write("\n")
				InventoryList[num-1]=""
				printPage(coins,InventoryList)
				print InventoryList[num-1]
				print "Item was dropped!"
			else:
				printPage(coins,InventoryList)
				print "No item to drop!"
		else:
			print "Please enter a valid pickup number from 1-5."
	
	# inventory which displays what the user has in his possession
	elif command == "inventory":
		printPage(coins,InventoryList)
		print "1.", Inventory1
		print "</br>"
		print "2.", Inventory2
		print "</br>"
		print "3.", Inventory3
		print "</br>"
		print "4.", Inventory4
		print "</br>"
		print "5.", Inventory5

print '</body>'
print '</html>'
