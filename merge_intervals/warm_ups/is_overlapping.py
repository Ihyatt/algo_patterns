"""
Are Intervals Overlapping

Given two intervals, determine if they are intervals.
"""

def is_overlapping(interval_1, interval_2):
    pass




def test_1():
    results = is_overlapping([1,1], [4,5])
    assert (results == False)

def test_2():
    results = is_overlapping([1,2], [2,3])
    assert (results == True)
    