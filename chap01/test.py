import pytest

import a_00
import a_01

def test_reverse_string_function():
    assert a_00.reverse_string("stressed") == "desserts"
    assert a_00.reverse_string("abc") == "cba"
    assert a_00.reverse_string("a") == "a"
    assert a_00.reverse_string("123456789") == "987654321"
    assert a_00.reverse_string("あカ美人") == "人美カあ"

def test_get_odd_positions():
    assert a_01.get_odd_positions("パタトクカシーー") == "タクシー"
    assert a_01.get_odd_positions("0123456789") == "13579"
    assert a_01.get_odd_positions("abcdef") == "bdf"
    assert a_01.get_odd_positions("a") == ""
    assert a_01.get_odd_positions("") == ""
