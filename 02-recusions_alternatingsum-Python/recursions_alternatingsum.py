# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def fun_recursions_alternatingsum(l): 
    count=1
    sum = 0
    n=-1
    if len(l)==0:
        return 0
    if(n==len(l)):
        return
    if(count%2==0):
        n+=1
        count=count+1
        sum+= l[n] + fun_recursions_alternatingsum(l[1:])
    else:
        count = count+1
        n+=1
        sum+= l[n] - fun_recursions_alternatingsum(l[1:])
    return sum
