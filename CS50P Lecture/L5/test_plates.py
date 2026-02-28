from plates import is_valid

def test_length():
    assert is_valid("C") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True

def test_start_with_two_letters():
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("CS") == True

def test_numbers_in_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_first_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False