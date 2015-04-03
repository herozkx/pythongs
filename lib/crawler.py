import urllib
import httplib

def fetchurl(url,method):
	proto, rest = urllib.splittype(url)
	domain,rest = urllib.splithost(rest)
	conn = httplib.HTTPConnection(domain)
	conn.request(method, rest)
	res = conn.getresponse()
	if res.status != 200:
		print "fetch%serror,with status:%d" %(url,res.status)
		data = ""
	else:
		data = res.read()
		conn.close()
	return dataimport 

