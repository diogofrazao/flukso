import urllib2
import ssl
import csv
import json
import time

###################################
sensor_id = 'id'
token_id = 'id'
interval = 'hour'
unit = 'watt' 
name_of_file = 'example'
###################################

url = 'https://api.flukso.net/sensor/'+sensor_id+'?interval='+interval+'&unit='+unit
file_name = name_of_file + '.csv'

req = urllib2.Request(url)
req.add_header('Accept', 'application/json')
req.add_header('X-Version', '1.0')
req.add_header('X-Token', token_id)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

response = urllib2.urlopen(req, context=gcontext)
data = json.load(response)

for row in data:
	row[0] = time.strftime("%D %H:%M", time.localtime(row[0]))

with open('almost.csv', 'w') as fp:
	a = csv.writer(fp, delimiter=';')
	a.writerows(data)
