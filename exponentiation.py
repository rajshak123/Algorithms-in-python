def exponentiation(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2:
        return x*exponentiation(x*x,(n-1)/2)
    return exponentiation(x*x,(n)/2)


