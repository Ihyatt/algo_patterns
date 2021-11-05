"""
Given a string of characters, check if the string contains anagram of target string.

Input:
astr = 'absolfuefkepppde'
target = 'fuel'

Output:
True

"""

def is_anagram_a_string(astr, target):
    pass




def test_1():
    results = is_anagram_a_string('absolfuefkepppde', 'fuel')
    assert (results == True)

def test_2():
    results = is_anagram_a_string('absolfuefkepppde', 'absolute')
    assert (results == True)
    
def test_3():
    results = is_anagram_a_string('', 'fluffy')
    assert (results == True)

def test_4():
    results = is_anagram_a_string('absolfuefkepppde', '')
    assert (results == True)

def test_5():
    results = is_anagram_a_string('absolfuefkrepppyde', 'preppy')
    assert (results == True)
