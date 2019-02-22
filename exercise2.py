# Write a Python class, Flower, that has three instance variables of type str, int,
# and float, that respectively represent the name of the flower, its num- ber of petals, and its price.
# Your class must include a constructor method that initializes each variable to an appropriate value,
# and your class should include methods for setting the value of each type, and retrieving the value of each type.


class Flower():

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_petals(self, petals):
        self._petals = petals

    def get_petals(self):
        return self._petals

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price


# Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class
# to ensure that the caller sends a number as a parameter.

def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.
    Return True if charge was processed; False if charge was denied. """
    if not isinstance(price, (int, float)):
        raise TypeError('Price must be numeric.')
    if price + self._balance > self._limit:
        return False
    else:
        self._balance += price
        return True
# if charge would exceed limit, # cannot accept charge


def make_payment(self, amount):

    """Process customer payment that reduces balance."""
    try:
        self._balance -= amount
    except TypeError as t:
        print('Amount must be numeric', t)
        return

# If the parameter to the make payment method of the CreditCard class were a negative number,
# that would have the effect of raising the balance on the account.
# Revise the implementation so that it raises a ValueError if a negative value is sent.

def make_payment(self, amount):

    """Process customer payment that reduces balance."""
    if amount < 0:
        raise ValueError('Amount must not be negative')
    self._balance -= amount
