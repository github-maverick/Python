def print_prime(n):
	for y in range (2,n+1):
		count=0
		for i in range (1,y):
			if (y % i)==0:
				count+=1
		if not count>1:
			print(y)


x= int(input("Prime numbers Upto: "))
print_prime(x)
