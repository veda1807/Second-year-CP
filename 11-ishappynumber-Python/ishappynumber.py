# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:

def ishappynumber(n):
    # your code goes here  
    if(n<0 or (n>1 and n<10)):     
        return False
    while(n>=10):
        sum=0
        for i in (str(n)):
            sum=sum+(int(i)*int(i))
        n=sum
    if(n==1):
        return True
    else:
        return False
# print(ishappynumber(98))
# print(ishappynumber(97))
# print(ishappynumber(404))



	