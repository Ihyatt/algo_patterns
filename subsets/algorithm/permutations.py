'''
Permutations

Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n! permutations.

'''

def find_permutations(nums):
    pass


def test_1():
    results = find_permutations([1,3,5])
    assert (results == [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]])
    
