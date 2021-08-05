# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
		return powerof3ton(int(n))
def powerof3ton(n,i=0,lst=[]):
	power=3**i
	if(n<=0):
		return None
	elif(power>n):
		return lst
	else:
		if(power<=n) and power not in lst:
			lst.append(power)
		return powerof3ton(n,i+1,lst)
print(powerof3ton(100))
