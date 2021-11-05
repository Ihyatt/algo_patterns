"""
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
"""

def max_sum_subarray():
    pass



def test_1():
    results = max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
    assert (results == 9)

def test_2():
    results = max_sum_subarray([2, 3, 4, 1, 5], 2)
    assert (results == 7)
    
def test_3():
    results = max_sum_subarray([], 5)
    assert (results == 0)

def test_4():
    results = max_sum_subarray([2, 3, 4, 1, 5], 0)
    assert (results == 0)

def test_5():
    results = max_sum_subarray([2, 3, 4, 1, 5], 6)
    assert (results == 0)
