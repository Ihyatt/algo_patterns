"""
Subsets

Given a set with distinct elements, find all of its distinct subsets.
"""
def find_subsets(arr):
    pass


def test_1():
    results = find_subsets([1,3])
    assert (results == [[], [1], [3], [1,3]])
    
def test_1():
    results = find_subsets([1, 5, 3])
    assert (results == [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]])
