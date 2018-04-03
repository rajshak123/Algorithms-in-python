def mergesort(a):
	if len(a)<2:
		return a
	mid=len(a)//2
	left=mergesort(a[:mid])
	right=mergesort(a[mid:])
	i=j=0
	b=[]
	while len(b)<len(a):
		

	return b