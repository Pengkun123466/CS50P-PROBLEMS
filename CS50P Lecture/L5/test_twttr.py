from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"

def test_uppercase_vowels():
    assert shorten("APPLE") == "PPL"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation_marks():
    assert shorten("What's your name?") == "Wht's yr nm?"