"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the 
longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
"""

def replacement_ones(arr, k):
    pass


def test_1():
    results = replacement_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
    assert (results == 6)

def test_2():
    results = replacement_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)
    assert (results == 9)
    