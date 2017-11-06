import random
food=["Raviolli","Pasta", "Pizza", "Cheesecake"]
print(random.choice(food)) #return a item from list
random.shuffle(food) #doesn't return anything but shuffles the list
print(food)
