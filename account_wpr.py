# account.py
"""Account class definition with properties."""
from decimal import Decimal


class AccountWPR:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance, bonus):
        """Initialize an Account object."""
        self.name = name
        self.balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @name.setter
    def name(self, name):
        #print(f"Setting {name=}")
        self._name = name

    @balance.setter
    def balance(self, balance):
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
        self._balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount

    def clear_account(self):
        self.balance = 0
