
import os,sys
sys.path.append(os.getcwd())
from isAdditivePrime import isAdditivePrime
import pytest


@pytest.mark.parametrize("input_value, result",[
	(2, True),
	(3, True),
	(5, True),
	(13, False),
	(23, True),
	(29, True),
	(41, True),
	(98, False),
	(198, False),
	(290, True),
	(67, False),
    (97, True)
])
def test_issorted(input_value, result):    
    assert isAdditivePrime(input_value) == result
