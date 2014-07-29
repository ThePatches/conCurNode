import http.client
import json
from random import randrange, choice

def doAttack(currThread):
	#TODO: Seed the generator in a reasonable fashion
	currList = GetCurrentList()
	newList = DoAddition() 	
	print(currThread + ": " + str(len(newList)))

def GenJob():
	jobs = ["Pilot", "Developer", "Secretary", "Maid", "Teacher", "Writer", "Administrator", "Doctor"]
	return choice(jobs);

def GenPerson():
	name = ["Michael", "Kerry", "Patricia", "Larry", "Curly", "Moe", "Wyatt", "Josh", "Balazs", "Myka"]
	return choice(name)

def GetCurrentList():
	conn = http.client.HTTPConnection("localhost:1337")
	conn.request("GET", "/showList")
	response = conn.getresponse()
	respBody = response.read()
	someVar = json.JSONDecoder().decode(respBody.decode("utf-8"))

	return someVar

def DoAddition():
	anAge = str(randrange(10, 75))
	aName = GenPerson()
	aJob = GenJob()

	URL = "/add?name={0}&age={1}&job={2}".format(aName, anAge, aJob)

	conn = http.client.HTTPConnection("localhost:1337")
	conn.request("GET", URL)
	response = conn.getresponse()
	respBody = response.read()
	someVar = json.JSONDecoder().decode(respBody.decode("utf-8"))

	return someVar

	

if __name__ == "__main__":
	doAttack("MainThread")
