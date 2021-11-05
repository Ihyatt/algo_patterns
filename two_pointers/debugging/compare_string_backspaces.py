"""
Comparing Strings containing Backspaces

Given two strings containing backspaces 
(identified by the character ‘#’), check if the two strings are equal.

"""
def backspace_compare(s, t):
    pt = len(t) - 1
    ps = len(s) - 1
    
    count_t = 0 
    count_s = 0 
    
    while ps >= 0 or pt >= 0:
        while ps >= 0 and s[ps] == "#":
            count_s += 1
            ps -= 1
            
        while pt >= 0 and t[pt] == "#":
            count_t += 1
            pt -= 1
            
        while count_s:
            ps -= 1
            if ps >= 0 and s[ps] =="#":
                count_s += 1
                continue
            count_s -= 1
                
        while count_t:
            pt -= 1
            if pt >= 0 and t[pt] == "#":
                count_t += 1
                continue
            count_t -= 1

        
        if pt >= 0 and ps >= 0 and t[pt] != s[ps]:
            print( s[ps],  t[pt])
            return False
        if pt < 0 and ps >= 0 or pt >= 0 and ps < 0:
            return False
        pt -= 1
        ps -= 1
        
    return True

def test_1():
    results = triplets_sum_closest("xy#z", "xzz#")
    assert (results == True)

def test_2():
    results = triplets_sum_closest("xy#z", "xyz#")
    assert (results == False)

def test_3():
    results = triplets_sum_closest("xp#","xyz##")
    assert (results == True)

def test_3():
    results = triplets_sum_closest("xywrrmp","xywrrmu#p")
    assert (results == True)
     