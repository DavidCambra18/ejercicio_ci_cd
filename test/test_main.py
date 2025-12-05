from src.main import *


def test_elevar():
    assert elevar(2, 3) == 8

def test_to_upper():
    assert to_upper('David') == 'DaVID'

def test_to_lower():
    assert to_lower('DAVID') == 'dAvid'