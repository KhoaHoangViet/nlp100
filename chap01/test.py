import pytest

import a_00

def test_reverse_string_function():
    assert a_00.reverse_string("stressed") == "desserts"
    assert a_00.reverse_string("abc") == "cba"
    assert a_00.reverse_string("a") == "a"
    assert a_00.reverse_string("123456789") == "987654321"