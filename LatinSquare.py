# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    for i in range(len(lst)):
        # print(i)
        if(lst.count(lst[i])>1):
            return False
        else:
            for j in range(len(lst[i])):
                if( (lst[i].count(lst[i][j])>1) or (lst[i].count(lst[j][i])>1) ):
                    return False
    return True
print(isLatinSquare([
    [1,2,3],
    [2,3,1],
    [3,1,2]
]))
