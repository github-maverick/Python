f=open("testfile.txt", "a") #append instead of rewriting and also create a new file if not already present
'''a+ writes from the end of program and also enables us to read it.'''
f.write("\nThis is my appending text to my testfile.txt.")
f.close()
