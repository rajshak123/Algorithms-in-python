import random
def isPrime(n,k=5):
	for i in range(k):
		a=random.randint(1, n-1)
		val=pow(a,n-1,n)
		if val!=1:
			return False
	return True

print(isPrime(7,1000))