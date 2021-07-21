# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
	k=(a+b+c)/2        				#(5+3+4)/2 =6 
	a=k*(k-a)*(k-b)*(k-c)			#36
	b=math.sqrt(a)					#6
	area_threelines=int(b)			#6
	return area_threelines			#6
	
