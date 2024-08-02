import pytest
import deposit_funds

def test_create_account():
    bank_dict = {"1111": 200}
    deposit_funds.deposit_funds(bank_dict)
    assert 0 != len(bank_dict)

# def test_account_number_between_rage():
#     bank_dict = {}
#     create_account.create_account(bank_dict)
#     account_numb = int(list((bank_dict.keys()))[0])
#     assert account_numb >= 1000 and account_numb <= 2000

def test_create_account_with_100_deposit():
    bank_dict = {"1111": 200}
    deposit_funds.deposit_funds(bank_dict)
    account_numb = list((bank_dict.keys()))[0]
    assert 300 == bank_dict[account_numb] 

    