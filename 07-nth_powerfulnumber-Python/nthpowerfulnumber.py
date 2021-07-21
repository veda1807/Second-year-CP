# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


	# Your code goes here

def primeOrNot(p):
	if(p==2 or p==3):
		return True
	if(p<2 or p%2==0):
		return False

	if(p>3):
		for i in range(3,p//2):
			if(p%i==0):
				return False
		return True

def powerFulNumber(p):
	if(p<0):
		return False
	if(p==1):
		return True
	for i in range(2,p+1):	
		if(p%i==0 and primeOrNot(i) and p%(i**2)!=0):
			return False
	return True
			
def nthpowerfulnumber(n):
	count=1
	a=2
	if(n==0):
		return 1
	while(count<=n):
		if(powerFulNumber(a)):
			count=count+1
		a=a+1
	return a-1
