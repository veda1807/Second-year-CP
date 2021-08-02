# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math
def fun_nth_smithnumber(n):
   count=0
   a = 0
   while(n>=count):
       a=a+1
       if(smith(a)):
           count+=1
   return a
 
def isPrime(n):
   if (n < 2):
       return False
   if (n == 2):
       return True
   if (n % 2 == 0):
       return False
   for i in range(2,n):
       if (n % i == 0):
           return False
   return True
def sumOfDigits(n):
    sum=0
    while(n>0):
        sum=sum+(n%10)
        n=n//10
    return sum
def primeFactors(n):
    i=2
    sum=0
    lst=[]
    while i*i<=n:
        if n%i==0:
            sum=sum+sumOfDigits(i)
            lst.append(i)
            n//=i
        else:
            i=i+1
    if n>1:
        lst.append(i)
        sum=sum+sumOfDigits(n)
    return sum
def smith(n):
    if(isPrime(n)):
        return False
    if(sumOfDigits(n)==primeFactors(n)):
        return True
    return False

