# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
	# lst=[a,b,c]
	# lst.sort()
	# return int("".join([str(i) for i in lst[::-1]]))
	
	minimum=min(a,b,c)
	maximum=max(a,b,c)
	# medium=a+b+c-maximum-minimum
	if (a!=minimum) and (a!=maximum):
		medium=a
	elif (b!=minimum) and (b!=maximum):
		medium=b
	else:
		medium=c
	return int(str(maximum)+str(medium)+str(minimum))

