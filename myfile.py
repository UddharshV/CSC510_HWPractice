def recursive_expo(a,n):
    if(n==0):
        return 1
    if(n==1):
        return a
    if(n%2==0):
        return recursive_expo(a,n//2)**2
    else:
        return recursive_expo(a,n-1)*a