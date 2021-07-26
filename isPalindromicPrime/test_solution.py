import os,sys
sys.path.append(os.getcwd())
from isPalindromicPrime import isPalindromicPrime
import pytest


@pytest.mark.parametrize("input_value, result",[
	(2, True),
	(10, False),
	(104, False),
    (235, False),
	(131, True),
	(900, False),
    (101, True),
	(383, True),
	(373, True),
	
])
def test_isPalindromicPrime(input_value, result):    
    assert isPalindromicPrime(input_value) == result