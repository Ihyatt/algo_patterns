"""
Find the Missing Number

We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ 
numbers out of the total ‘n+1’ numbers, find the missing number.
"""

def find_missing_number(arr):
    pass



def test_1():
    results = find_missing_number([4, 0, 3, 1])
    assert (results == 2)

def test_2():
    results = find_missing_number([8, 3, 5, 2, 4, 6, 0, 1])
    assert (results == 7)
    