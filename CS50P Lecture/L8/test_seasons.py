import pytest
from seasons import get_minutes,convert_to_words

def test_int():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand six hundred minutes"