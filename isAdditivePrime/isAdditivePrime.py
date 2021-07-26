'''IsAdditivePrime: Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.
Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.'''

def prime(n):
    if n==2 or n==3:
        return True
    if(n<2 or n%2==0):
        return False
    if(n>3):
        for i in range(3,n):
            if(n%i==0):
                return False
        return True
def isAdditivePrime(n):
    sum=0
    while(n>9):
        n=str(n)
        for i in n:
            sum=sum+int(i)
        n=sum
        sum=0
    else:
        if(prime(n)):
            return True
        return False
# print(isAdditivePrime(98))
# print(isAdditivePrime(19))
