"""
	The following script must be run like this python netusage.py (type) (phase) (room)
	e.g. to get the percent of the bandwith used by the room 6109 in phase 3, you need to call
	the script as the following : python netusage.py percent 3 6109
"""

import urllib
import re
import sys
from datetime import datetime
import api

def getUsage(type,phase,room):
	""" 	type 	- percent 	-> 	percentage of your bandwidth used
					- left		->	quantity in GB of your bandwidth left
					- usage 	->	quantity in GB of your bandwidth usage
					- all 		->	summary of your usage
			phase	must be 1, 2  or 3
			room	must be an existing room in the block
	"""

	return api.getData(phase,room,datetime.now().month)

	if type == "percent":
		return "{:0.2f}%".format(pct)
	if type == "left":
		return "{:0.2f}GB".format(left)
	if type =="usage":
		return "{:0.2f}GB".format(usage/1024)
	if type =="all":
		return "Used :\t\t{:0.2f}GB ({:0.2f}%)\nLeft :\t\t{:0.2f}GB ({:0.2f}%)\nTotal :\t\t{:0.2f}GB".format(usage/1024,pct,left,100-pct,max/1024)
	raise Exception('Must choose between "percent" and "left" ')	


type = sys.argv[1]
phase = sys.argv[2]
room = sys.argv[3]


print getUsage(type,phase,room)
