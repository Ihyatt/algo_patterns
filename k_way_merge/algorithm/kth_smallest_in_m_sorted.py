"""
Kth Smallest Number in M Sorted Lists


Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
"""

import heapq

def find_Kth_smallest(lists, k):
    pass


def test_1():
    results = find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)
    assert (results == 4)
    
def test_2():
    results = find_Kth_smallest([[5, 8, 9],[1, 7]],3 )
    assert (results == 7)
    
