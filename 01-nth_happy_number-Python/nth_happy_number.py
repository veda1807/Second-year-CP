# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

	
def ishappynumber(n):
    # your code goes here  
    if(n<0):     
        return False
    while(n>=10):
        sum=0
        for i in (str(n)):
            sum=sum+(int(i)*int(i))
        n=sum
    if(n==1 or n==7):
        return True
    else:
        return False

def nth_happy_number(n):
	count=0
	result=1
	while (count<=n):
		if(ishappynumber(result)):
			count=count+1
		if(count==n):
			break
		result=result+1
	return result
