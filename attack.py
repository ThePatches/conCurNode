import http.client
import json

def doAttack(currThread):
	conn = http.client.HTTPConnection("localhost:1337")
	conn.request("GET", "/add?name=Larry&age=22&job=Sweeper");
	response = conn.getresponse()
	respBody = response.read()
	someVar = json.JSONDecoder().decode(respBody.decode("utf-8"));
	#print(currThread);
	print(currThread + ": " + str(len(someVar)))

if __name__ == "__main__":
	doAttack("MainThread")
