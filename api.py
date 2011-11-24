import re
import urllib
import simplejson as json
import time
import datetime

def getData(phase,room,month):

	regexRowUsage = '<TR><TD>(.*)</TD><TD>(.*)</TD><TD ALIGN="RIGHT">(.*)</TD><TD ALIGN="RIGHT">(.*)</TD></TR>'
	regexUsage = '<TR><TD COLSPAN="3"><B>Total combin&eacute;:</B></TD><TD ALIGN="RIGHT">(.*)</TD></TR>'
	regexMax ='<TD>Quota permis pour la p&eacute;riode</TD><TD ALIGN="RIGHT">(.*)</TD></TD></TR>'

	url ="http://ets-res%s-%s:ets%s@www2.cooptel.qc.ca/services/temps/?mois=%s&cmd=Visualiser" % (phase,room,room,month)

	f = urllib.urlopen(url)
	s = f.read()
	f.close()

	data = {}


	rowMatches = re.findall(regexRowUsage,s)

	data['details']=[]

	for match in rowMatches:
		port = match[0]
		dateString = match[1]
		if dateString.startswith('Jour'):
			today = datetime.datetime.now()
			date = today.replace(hour=0,minute=0,second=0,microsecond=0)
		else:
			date = datetime.datetime.strptime(dateString,'%Y-%m-%d')
		upload = float(match[2].lstrip())/1024
		download = float(match[3].lstrip())/1024
		total = upload+download
		data['details'].append({
			'port':port,
			'date':date,
			'upload':upload,
			'download':download,
			'total':total
		})

	m = re.search(regexUsage,s)
	usage = float(m.group(1).lstrip())/1024
	m = re.search(regexMax,s)
	maximum = float(m.group(1))/1024
	left = maximum-usage

	data['room']=room
	data['phase']=phase
	data['month']=month

	data['usage']=usage
	data['left']=left
	data['maximum']=maximum

	dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
	return json.dumps(data,default=dthandler)