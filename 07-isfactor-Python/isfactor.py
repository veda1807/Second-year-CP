# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.


# def fun_isfactor(f, n):
# 	if (n==0):
# 		return True
# 	elif (f==0) :
# 		return False
# 	elif(n%f==0):
# 		return True
# 	elif(n%f!=0):
# 		return False
	

def fun_isfactor(f, n):
	if(n==0 and f==0):
		return True
	elif (f==0) or  n%f!=0:
		return False
	
	elif (n==0) and (n%f==0):
		return True
	else:
		return True # replace with your solution
