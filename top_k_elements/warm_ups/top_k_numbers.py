"""
Top 'K' Numbers 

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
"""

import heapq

def find_k_largest_numbers(nums, k):
    pass

def test_1():
    results = find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)
    assert (results == [5, 12, 11])
    
def test_2():
    results = find_k_largest_numbers([5, 12, 11, -1, 12], 3)
    assert (results == [12, 11, 12])
    
