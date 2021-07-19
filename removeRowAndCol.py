# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

# list
# [ [ 2, 3, 4, 5],
#   [ 8, 7, 6, 5],
#   [ 0, 1, 2, 3] ]

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]

# import numpy as np
import pytest

def removeRowAndCol(L, row, col):

    for i in L:
        i.pop(col)
    L.pop(row)
    return L

# Write your own test cases.
@pytest.mark.parametrize ('L,row,col, result',[
    ([ [ 2, 3, 4, 5],
  [ 8, 7, 6, 5],
  [ 0, 1, 2, 3] ], 1,2, [ [ 2, 3, 5],
  [ 0, 1, 3] ])
    ])
def test(L, row,col, result):
    assert removeRowAndCol(L, row, col)==result