# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withproperty(n):
	power=str(n**5)
	digit=['0','1','2','3','4','5','6','7','8','9']
	for num in digit:
		if num not in power:
			return False
	return True
	
def nthwithproperty309(n):
	if(n==0):
		return 309
	count=1
	b=309
	while(count<=n):
		b=b+1
		if(withproperty(b)):
			count=count+1
	return b




print(nthwithproperty309(10))
# print(withproperty(462))
# print(withproperty(475))
# print(withproperty(576))
# print(withproperty(634))
# print(withproperty(663))
# print(withproperty(2015))



