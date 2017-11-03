file1=open("textfile.txt", "r")
'''r+ reads the file and wirtes it replacing the characters from the first not removing all the elements of before but only removing the elements upto where the new text goes'''
print(file1.readline())
print(file1.read())
print(file1.read())
'''has already read once so the cursor has reached to the last of document
Its easier from the python console'''
file1.seek(0,0)
print(file1.read(22))
print(file1.read(34))
print(file1.read(70))
file1.close()
