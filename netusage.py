import urllib
import re
import sys
from datetime import datetime


def getUsage(type,room,phase):

	regexUsage = '<TR><TD COLSPAN="3"><B>Total combin&eacute;:</B></TD><TD ALIGN="RIGHT">(.*)</TD></TR>'
	regexMax ='<TD>Quota permis pour la p&eacute;riode</TD><TD ALIGN="RIGHT">(.*)</TD></TD></TR>'


	url ="http://ets-res%s-%s:ets%s@www2.cooptel.qc.ca/services/temps/?mois=%s&cmd=Visualiser" % (phase,room,room,datetime.now().month)

	f = urllib.urlopen(url)
	s = f.read()
	f.close()

	m = re.search(regexUsage,s)

	usage = float(m.group(1).lstrip())


	m = re.search(regexMax,s)
	max = float(m.group(1))

	pct = usage/max*100
	left = (max-usage)/1024

	if type == "percent":
		return "{:0.2f}%".format(pct)
	
	if type == "left":
		return "{:0.2f}GB".format(left)
		
	raise Exception('Must choose between "percent" and "left" ')	


type = sys.argv[1]
phase = sys.argv[2]
room = sys.argv[3]


print getUsage(type,room,phase)

#print "You used {:0.2f}% of your bandwidth.".format(getUsage())
#print "There is {:0.2f}gb left.".format(left)