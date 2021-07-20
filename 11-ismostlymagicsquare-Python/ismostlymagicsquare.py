# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.


# [16, 3, 2, 13], 
# [5, 10, 11, 8], 
# [9, 6, 7, 12],
# [4, 15, 14, 1]

def ismostlymagicsquare(a):
	for i in range(len(a)):
		sum_row=0     #initially sum of the row=0
		sum_col=0		#initially col=0
		for j in range(len(a[0])):
			sum_row=sum_row+a[i][j]	 #0,0== 16 ==> 0,1==>3 , 0,2==>2
			sum_col=sum_col+a[j][i]	 #0,0=16  ==> 1,0 =	5, 2,0 ==>9
		if(sum_col!=sum_row):		
			return False
	d1=0
	d2=0
	for i in range(len(a)):
		d1+=a[i][i]
		d2+=a[i][len(a)-1-i]     
	if(d1!=d2):
		return False
	return True

		
