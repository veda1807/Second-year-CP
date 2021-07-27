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
# def isPalindrome(n):
#     return (str(n)==str(n)[::-1])
def isPalindromicPrime(n):
    if(n==2):
        return True
    if(n>9):
        n=str(n)
        if(len(n)%2==0):
            n=int(n)
            a=n//2
            n=str(n)
        else:
            a=len(n)//2+1
        j=len(n)-1
        for i in range(a):
            if(n[i]!=n[j]):
                return False
            else:
                
                j-=1
                
        c=isPrime(a)
        return c


    # if(isPalindrome(n) and isPrime(n)):
    #     return True
    # return False

# def isPalindromicPrime(n):
    # num=n
    # rev=0
    # if(isPrime(n)):
    #     while(n>0):
    #         a=n%10
    #         rev=rev*10+a
    #         n=n//10
    #     if(rev==num):
    #         return True
        
    # return False



    
    


# assert(isPalindromicPrime(2) == True)
# print(assert(isPalindromicPrime(10) == False))
# print(assert(isPalindromicPrime(104) == False))
# print(assert(isPalindromicPrime(235) == False))
# print(assert(isPalindromicPrime(131) == True))
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
