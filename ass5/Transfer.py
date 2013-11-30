#! usr/bin/python

import sys
import cgi

def main():
	coins = "0"
	inv1 = ""
	inv2 = ""
	inv3 = ""
	inv4 = ""
	inv5 = ""
	#gather points and inventory items from form
	form = cgi.FieldStorage()
	if form.has_key("coins") and form["coins"].value != "":
		coins = form["coins"].value
	if form.has_key("Inventory1") and form["Inventory1"].value != "":
		inv1 = form["Inventory1"].value
	if form.has_key("Inventory2") and form["Inventory2"].value != "":
		inv2 = form["Inventory2"].value
	if form.has_key("Inventory3") and form["Inventory3"].value != "":
		inv3 = form["Inventory3"].value
	if form.has_key("Inventory4") and form["Inventory4"].value != "":
		inv4 = form["Inventory4"].value
	if form.has_key("Inventory5") and form["Inventory5"].value != "":
		inv5 = form["Inventory5"].value
	#print the page given the information gathered
	printPage(coins,inv1,inv2,inv3,inv4,inv5)

#similar to method in room, however this updates the hidden fields
def printPage(coins,inv1,inv2,inv3,inv4,inv5):
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
        print """<input type="hidden" name="points" value=" """,coins,""" "> """
	#added to generate inventorys passed from other pages
        print """<input type="hidden" name="Inventory1" value=" """,inv1,""" "> """
        print """<input type="hidden" name="Inventory2" value=" """,inv2,""" "> """
        print """<input type="hidden" name="Inventory3" value=" """,inv3,""" "> """
        print """<input type="hidden" name="Inventory4" value=" """,inv4,""" "> """
        print """<input type="hidden" name="Inventory5" value=" """,inv5,""" "> """
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print """<form name="goNorth" action="http://www.cs.mcgill.ca/~eraso/Grid.html" method="post">"""
      	#this is what will use the updated coins value to update the page
        print """<input type="hidden" name="points" value=" """,coins,""" "> """
	#added to generate inventorys passed from other pages
        print """<input type="hidden" name="Inventory1" value=" """,inv1,""" "> """
        print """<input type="hidden" name="Inventory2" value=" """,inv2,""" "> """
        print """<input type="hidden" name="Inventory3" value=" """,inv3,""" "> """
        print """<input type="hidden" name="Inventory4" value=" """,inv4,""" "> """
        print """<input type="hidden" name="Inventory5" value=" """,inv5,""" "> """
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print "<!-- and the top button -->"
        print "</form>"

        print """<form name="goWest" action="http://cs.mcgill.ca/~cmacdo40/room.html" method="post">"""
      	#this is what will use the updated coins value to update the page
        print """<input type="hidden" name="points" value=" """,coins,""" "> """
	#added to generate inventorys passed from other pages
        print """<input type="hidden" name="Inventory1" value=" """,inv1,""" "> """
        print """<input type="hidden" name="Inventory2" value=" """,inv2,""" "> """
        print """<input type="hidden" name="Inventory3" value=" """,inv3,""" "> """
        print """<input type="hidden" name="Inventory4" value=" """,inv4,""" "> """
        print """<input type="hidden" name="Inventory5" value=" """,inv5,""" "> """
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print "<!-- and the left button -->"
        print "</form>"

        print """<form name="goEast" action="http://www.cs.mcgill.ca/~aturne15/room.html" method="post">"""
        #this is what will use the updated coins value to update the page
        print """<input type="hidden" name="points" value=" """,coins,""" "> """
	#added to generate inventorys passed from other pages
        print """<input type="hidden" name="Inventory1" value=" """,inv1,""" "> """
        print """<input type="hidden" name="Inventory2" value=" """,inv2,""" "> """
        print """<input type="hidden" name="Inventory3" value=" """,inv3,""" "> """
        print """<input type="hidden" name="Inventory4" value=" """,inv4,""" "> """
        print """<input type="hidden" name="Inventory5" value=" """,inv5,""" "> """
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print """<!-- and the right button -->"""
        print "</form>"

        print"""<form name="goSouth" action="http://cgi.cs.mcgill.ca/~phende/comp206/room.html" method="post">"""
      	#this is what will use the updated coins value to update the page
        print """<input type="hidden" name="points" value=" """,coins,""" "> """
	#added to generate inventorys passed from other pages
        print """<input type="hidden" name="Inventory1" value=" """,inv1,""" "> """
        print """<input type="hidden" name="Inventory2" value=" """,inv2,""" "> """
        print """<input type="hidden" name="Inventory3" value=" """,inv3,""" "> """
        print """<input type="hidden" name="Inventory4" value=" """,inv4,""" "> """
        print """<input type="hidden" name="Inventory5" value=" """,inv5,""" "> """
        print """<input type="submit" value="Submit">"""
        print "</form>"

        print"<!-- and the bottom button -->"
        print"</form>"
        
        print"</br>"
