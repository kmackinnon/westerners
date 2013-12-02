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

print '</body>'
print '</html>'
