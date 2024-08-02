import pytest
import warmup

def test_true():
    assert True == warmup.is_palindrome("racecar")
    assert True == warmup.is_palindrome("madam")
    assert True == warmup.is_palindrome("A man, a plan, a canal, Panama")

def test_false():
    assert False == warmup.is_palindrome("OScar")
    assert False == warmup.is_palindrome("hello world")