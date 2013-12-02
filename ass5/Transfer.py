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
print """<div id = "header">"""
print '<h1> The Room </h1>'
print '</div>'
print '<!--Display the room -->'
print """<div id="main">"""

print """ <form name="goNorth" action="http://cs.mcgill.ca/~eraso/ass5/transfer.py" method="post">"""
print """<input type="hidden" name="coins" value=" """,coins,""" "> """
print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
print """<input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""
print "<!-- and the top button -->"
print """<a href="http://cs.mcgill.ca/~eraso/ass5/transfer.py" onclick = form.submit() class="top">North</a></br></br></br></br>"""
print "</form>"
	
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
	
print """<form name="goWest" action="http://cs.mcgill.ca/~cmacdo40/ass5/transfer.py" method="post">"""
print """<input type="hidden" name="coins" value=" """,coins,""" ">"""
print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
print """ <input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""
print "<!-- and the left button -->"
print """<a href="http://cs.mcgill.ca/~cmacdo40/ass5/transfer.py" onclick = form.submit() class="left">West</a></br>"""
print "</form>"

print """<form name="goEast" action="http://www.cs.mcgill.ca/~aturne15/room.html" method="post">"""
print """<input type="hidden" name="coins" value=" """,coins,""" "> """
print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
print """<input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""
print "<!-- the right button -->"
print """<a href="http://www.cs.mcgill.ca/~aturne15/room.html" onclik = form.submit() class="right">East</a></br>"""
print "</form>"

print """<form name="goSouth" action="http://cgi.cs.mcgill.ca/~phende/comp206/room.html" method="post">"""
print """<input type="hidden" name="coins" value=" """,coins,""" "> """
print """<input type="hidden" name="Inventory1" value=""",InventoryList[0],""">"""
print """<input type="hidden" name="Inventory2" value=""",InventoryList[1],""">"""
print """<input type="hidden" name="Inventory3" value=""",InventoryList[2],""">"""
print """<input type="hidden" name="Inventory4" value=""",InventoryList[3],""">"""
print """<input type="hidden" name="Inventory5" value=""",InventoryList[4],""">"""                       
print "<!-- and the bottom button -->"
print """<a href="http://cgi.cs.mcgill.ca/~phende/comp206/room.html" onclick = form.submit() class="bottom">South</a></br>"""
print"</form>" 

	
print "</br>"
print "</div>"

print '</body>'
print '</html>'
