from doThreads import MyThread

thread1 = MyThread(1, "thread-1", 2)
thread2 = MyThread(2, "thread-2", 2)

thread1.start()
thread2.start()

print("Exiting Main Thread")
