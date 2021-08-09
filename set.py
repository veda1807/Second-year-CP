# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

import itertools
def limitedPowerSer(n,k):
    s=set(())
    lst=[{}]
    for i in range(1,n+1):
        s.add(i)
    for i in range(1, len(s)+1):
        a=list(map(set, itertools.combinations(s,i)))
        for j in range(len(a)):
            if(len(lst)!=k):
                lst.append(a[j])
            else:
                return lst

assert(limitedPowerSer(5,7)== [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
print("test cases Passed")
































# import itertools 
# # from itertools import chain, combinations
# def limitedPowerSet(n, k):
#     # Your code goes here...
#     lst=[{}]
#     s=set(())
#     for i in range(1,n+1):
#         s.add(i)
#     for i in range(1, len(s)+1):
#         a=list(map(set, itertools.combinations(s,i)))
#         for j in range(len(a)):
#             if(len(lst)!=k):
#                 lst.append(a[j])
#             else:
#                 return lst


# assert(limitedPowerSet(5, 7)== [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
# print("All passed")