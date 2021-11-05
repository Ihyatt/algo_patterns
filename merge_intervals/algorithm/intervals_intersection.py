"""
Intervals Intersection

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
"""

def interval_intersection(arr1, arr2):
    pass



def test_1():
    results = interval_intersection([[1, 3], [5, 6], [7, 9]],[[2, 3], [5, 7]] )
    assert (results == [[2, 3], [5, 6], [7, 7]])

def test_2():
    results = interval_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])
    assert (results == [[5, 7], [9, 10]])
