import re
string = "adasdasdsadsadCheeseadasdsdsasadas sadasdas asdasCake asdasdasd Pizza"
position = re.search("Cheese", string) # this gives the position of the string Cheese in the string
print(string[position.start(): position.end()])
#position.start() and position.end() gives the location of strings
