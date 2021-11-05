"""
Search in Rotated Array
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.
"""

def search_rotated_array(arr, key):
    pass

def test_1():
    results = search_rotated_array([10, 15, 1, 3, 8], 15)
    assert (results == 1)
    
def test_2():
    results = search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10)
    assert (results == 4)
    
