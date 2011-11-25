#Bandwidth usage tool
This script was built to visualize your bandwidth usage in the ETS apartments.

##Usage
The following script must be run like this :

	python netusage.py (type) (phase) (room)

e.g. to get the percent of the bandwith used by the room 6109 in phase 3, you need to call
the script as the following :

	python netusage.py percent 3 6109


##API
I wrote a wrapper for the Cooptel site. My wrapper returns the information in a JSON format.
All you need is to import my script (api.py) and use the following function :

	getData(phase,room,month)

It will return you a JSON object with the following properties :

* room : the room specified
* phase : the phase specified
* month : the month specified
* usage : total used (in GB)
* left : total left (in GB)
* maximum : total (in GB)
* details : array of each day of the month

The *details* property is an array of JSON objects with the following properties :

* port : port identifer for this day usage
* date : date of the stat
* upload : total upload for this day (in GB)
* download : total download for this day (in GB)
* total : total usage for this day (upload + download) (in GB)