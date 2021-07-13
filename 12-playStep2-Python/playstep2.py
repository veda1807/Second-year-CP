# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

def playstep2(hand, dice):  #(413, 2312) == 421,23
	digit_1= hand//100      #4
	digit_2= (hand%100)//10  #1
	digit_3=hand%10   		#3
	lst1=[digit_1, digit_2, digit_3]  #[4,1,3]
	new_list=[]  #empty list
	if (digit_1!= digit_2 and digit_2!=digit_3 and digit_1!=digit_3):  #(4!=1 and 1!=3 and 3!=4)
		lst1.sort(reverse=True) #[4,3,1]
		new_list.append(str(lst1[0]))  #  newlist = ["4"]
		new_list.append(str(dice%10))   # in newlist = ["4","2"]
		d=(dice//10)%10  				# 2312//10 = 231 , 231%10 = 1
		dice=dice//10  					# dice=2312//10 = 231 == updating the dice
		new_list.append(str(d))  		# in newlist = ["4", "2", "1"]
		dice=dice//10 	  				# dice=231//10 = 23 == updating the dice
		new_list.sort(reverse=True) 	# it sorts the new_list in descending order
		result=int("".join(new_list)) 	#it converts into integer
		return(result, dice) 			
	elif (digit_1 == digit_2 or digit_3== digit_2 or digit_3== digit_1):
		if(digit_1==digit_2):  
			new_list.append(str(digit_1)) # adding digit_1 of hand to newlist
			new_list.append(str(digit_2)) # same .. now digit 2
			new_list.append(str(dice%10))  #taking last digit from dice
			new_list.sort(reverse=True)   # it sorts  in descending
			result=int("".join(new_list))  # converts into int
			return (result, dice//10)  # int , dice==>except the last digit , it returns remaining digits
		elif(digit_2==digit_3):
			new_list.append(str(digit_2))
			new_list.append(str(digit_3))
			new_list.append(str(dice%10))
			new_list.sort(reverse=True)
			result=int("".join(new_list))
			return (result, dice//10)
		elif(digit_1==digit_3):
			new_list.append(str(digit_1))
			new_list.append(str(dice%10))
			new_list.append(str(digit_3))
			new_list.sort(reverse=True)
			result=int("".join(new_list))
			return (result, dice//10)
	else:
			return (hand, dice)  #if all the digits same then it returns hand and dice
 




		



