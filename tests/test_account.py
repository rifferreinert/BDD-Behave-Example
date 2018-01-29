import pytest
from account import Account

def test_deposit():
    a = Account(0)
    a.deposit(50)
    assert a.current_value == 50