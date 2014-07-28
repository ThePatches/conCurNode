import http.client

def doAttack():
	conn = http.client.HTTPConnection("localhost:1337")
	conn.request("GET", "/add?name=Larry&age=22&job=Sweeper");
	response = conn.getresponse()
	print(response.read())
