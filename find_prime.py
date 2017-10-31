def find_prime(n):
	count=0
	for i in range (1,n):
		if (n % i)==0:
			count+=1
	if n==0 or n==1:
		return("%s is neither prime nor composite number."%n)
	if not count>1:
		return("%s is a prime number."%n)
	return("%s is a composite number."%n)


x= int(input("Input the number:"))
print(find_prime(x))
