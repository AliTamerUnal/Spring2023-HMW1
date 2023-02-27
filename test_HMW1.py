import HMW1

def test_1_1():
    assert HMW1.doIt1([1,2,3]) == 1
    
def test_1_2():
    assert HMW1.doIt1([1,2,3,4]) == 1

def test_1_3():
    assert HMW1.doIt1([1,2,3,5]) == 2
    
def test_1_4():
    assert HMW1.doIt1([1,2,4,5]) == 0
    
def test_2_1():
    assert HMW1.doIt2([1,2,3]) == 1
    
def test_2_2():
    assert HMW1.doIt2([1,2,3,4]) == 1

def test_2_3():
    assert HMW1.doIt2([1,2,3,5]) == 2
    
def test_2_4():
    assert HMW1.doIt2([1,2,4,5]) == 0