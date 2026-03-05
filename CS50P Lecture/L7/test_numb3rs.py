from numb3rs import validate

def test_right():
    assert validate("255.255.255.255") == True

def test_all_larger():
    assert validate("512.512.512.512") == False

def tes_one_larger():
    assert validate("1.2.3.1000") == False

def test_wrong_way():
    assert validate("192.168.001.1") == False

def test_not_num():
    assert validate("cat") == False