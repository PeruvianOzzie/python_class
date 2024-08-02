# wallet 
    # add cash 
    # spend cash 
    # initial amount 
    # insufficient funds

import pytest
from wallet import Wallet, InsufficientAmount

# def my_wallet():
#     # returns a wallet instance with a balance 0
#     return Wallet()

# @pytest.mark.parametrize("earned, spent, expected", [
#     (30, 10, 20),
#     (20, 2, 18),
# ])

# def test_transactions(earned, spent, expected):
#     wallet = Wallet()
#     wallet.add_cash(earned)
#     wallet.spend_cash(spent)
#     assert wallet.balance == expected




@pytest.fixture
def wallet():
    # Returns a Wallet instance with a balance of 20
    return Wallet(20)

@pytest.fixture
def empty_wallet():
    # Returns a Wallet instance with a balance of 0
    return Wallet()

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)