from doThreads import MyThread

someThreads = []
threadNum = 10

for x in range(0, threadNum):
	someThreads.append(MyThread(x + 1, "thread-" + str(x + 1), 10))

for nThread in someThreads:
	nThread.start()

#thread1 = MyThread(1, "thread-1", 2)
#thread2 = MyThread(2, "thread-2", 2)

#thread1.start()
#thread2.start()

print("Exiting Main Thread")
