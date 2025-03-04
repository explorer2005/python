def factorial(n):
    if(n==0 or n==1):
        return 1
    else: 
        ans=n*factorial(n-1)
    return ans
k=factorial(5)
print(k)
