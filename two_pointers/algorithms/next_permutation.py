"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

"""

def next_perm(nums):
    pass


def test_1():
    results = next_perm([1,2,3])
    assert (results == [1,3,2])

def test_2():
    results = next_perm([3,2,1])
    assert (results == [1,2,3])
    