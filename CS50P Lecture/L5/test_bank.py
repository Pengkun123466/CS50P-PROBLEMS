from bank import value

def test_Standard_case():
    assert value("hello") == 0

def test_Onlyh_case():
    assert value("hi") == 20

def test_Othergreetings_case():
    assert value("What's up") == 100

def test_Mixed_case():
    assert value("HeLlO") == 0