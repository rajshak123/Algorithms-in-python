past_fib={}
def fibonacci(n):
	if n==0 or n==1:
		past_fib[n]=1
		return 1
	else:
		total=fibonacci(n-1)+fibonacci(n-2)
		past_fib[n]=total
		return total
print(fibonacci(32))