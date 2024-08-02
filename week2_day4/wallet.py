
class InsufficientAmount(Exception):
    pass

class Wallet():
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        

    def add_cash(self, amount):
        self.balance += amount

    def spend_cash(self, amount):
        if self.balance <= amount:
            raise InsufficientAmount("Not enough funds")
        self.balance -= amount


wallet = Wallet()

print(wallet.balance)
wallet.add_cash(100)
print(wallet.balance)
wallet.spend_cash(10)
print(wallet.balance)