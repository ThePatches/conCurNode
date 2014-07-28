from attack import doAttack
import threading

exitFlag = 0

class MyThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("Starting " + self.name);	
		attackLoop(self.name, self.counter);
		print("Exiting: " + self.name);

def attackLoop(threadName, counter):
	while counter:
		if exitFlag:
			thread.exit()
		doAttack(threadName)
		counter -= 1	
