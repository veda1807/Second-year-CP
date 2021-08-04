# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def isprime(n):
    if(n==2 or n==3):
        return True
    if(n<2 or n%2==0):
        return False
    if(n>3):
        for i in range(3,n//2):
            if(n%2==0):
                return False
        return True

def ishappyNumber(n):
    if(n<0):
        return False
    if (n==1):
        return True
    sum=0
    while(n>10):
        sum=0
        for i in str(n):
            sum=sum+(int(i)**2)
        n=sum
    return sum


def ishappyprimenumber(n):
    if (ishappyNumber(n) and isprime(n)):
        return True
    return False

    
print(ishappyprimenumber(2))
print(ishappyprimenumber(23))
print(ishappyprimenumber(19))
print(ishappyprimenumber(31))
print(ishappyprimenumber(709))