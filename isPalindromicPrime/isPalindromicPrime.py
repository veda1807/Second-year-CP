def isPrime(x):
    if(x<2):
        return False
    if(x==2):
        return True
    if(x % 2 == 0):
        return False        
    maxfactor=round(x**0.5)
    for factor in range(3,maxfactor+1,2):    
        if(x%factor==0):
            return False
    return True
def Palindrome(n):
    
    if(n>9):
        n=str(n)
        if(len(n)%2==0):
            a=n//2
        else:
            a=len(n)//2+1
        # n=str(n)
        j=len(n)-1
        for i in range(a):
            if(n[i]!=n[j]):
                return False
            else:
                
                j-=1
                
        c=isPrime(a)
        return c
# print(Palindrome(182))