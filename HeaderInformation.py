#! /usr/bin/python3

# Vincent Arlequin  - Personal Project - Based on SP/25 CYS-337-01 - 03/13/25

# Prompts user for url and header information, returns requested header information continuously unless "STOP" is entered.

# Import urllib, allows us to read website information
import urllib.request

# Function takes header field and header to parse, returns value 
def getHeaderField(f, h):
        return h.get(f)

# Prompt user for website to parse
website = str(input("Enter URL to gather header information from: "))

# Prints name of website being parsed
print ("Retrieving header information from", website)

# Pretend we are Mozilla Firefox
agent = 'Mozilla/5.0'
hds = {'User-Agent':agent}
req = urllib.request.Request(website, headers = hds)

# Gathers website information
with urllib.request.urlopen(req) as response:

	# Read the header info
	headers = response.info()

	# First prompt for field to display
	requested_info=str(input("What header information would you like to view? Enter STOP to end: "))

	# Continuously prompts user for field to display, displays header information, stops when user enters "STOP"
	while requested_info != "STOP":
		print(requested_info, "is", getHeaderField(requested_info, headers))
		requested_info=str(input("What header information would you like to view? Enter STOP to end: "))