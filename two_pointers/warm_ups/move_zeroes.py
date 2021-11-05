"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def move_zeroes(nums):
    pass


def test_1():
    results = move_zeroes([0,1,0,3,12])
    assert (results == [1,3,12,0,0])

def test_2():
    results = move_zeroes([0])
    assert (results == [0])
    
