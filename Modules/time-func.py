import time
def numbers(num):
	time1=time.time()
	for i in range(num):
		print(i)
	time2=time.time()
	print("Time taken to run the program is %f"%(time2-time1))

numbers(100)
print(time.asctime()) #to print the current time
print(time.localtime())
t=time.localtime() #it acts as a array
print("The current date is %d/%d/%d."%(t[0], t[1], t[2]))
#time.sleep(x) to stop the program for some seconds x is the value in seconds
