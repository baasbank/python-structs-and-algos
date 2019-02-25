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


# The CreditCard class of Section 2.3 initializes the balance of a new account to zero.
# Modify that class so that a new account can be given a nonzero balance using an optional fifth parameter to the constructor.
# The four-parameter constructor syntax should continue to produce an account with zero balance.

def __init__(self, customer, bank, acnt, limit, balance=0):
    """Create a new credit card instance.
    The initial balance is zero.

    customer the name of the customer (e.g., John Bowman )
    bank the name of the bank (e.g., California Savings )
    acnt the acount identifier (e.g., 5391 0375 9387 5309 )
    limit credit limit (measured in dollars)
    """

    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = balance


# Implement the __sub__ method for the Vector class of Section 2.3.3, so that the expression u−v returns a new vector instance representing the difference between two vectors.

def __sub__(self, other):
    """Return difference of two vectors."""
    if len(self) != len(other):  # relies on __len__  method
        raise ValueError('dimensions must agree')
    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = self[j] - other[j]
    return result


# Implement the __neg__ method for the Vector class of Section 2.3.3, so that the expression −v returns a new vector instance whose coordinates are all the negated values of the respective coordinates of v.

def __neg__(self):
    result = Vector(len(self))
    print(len(self) - 1)
    for j in range(len(self)):
        result[j] = -self[j]
    return result


# Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expression v * 3 returns a new vector with coordinates that are 3 times the respective coordinates of v.

def __mul__(self, multiplier):
    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = self[j] * multiplier
    return result

# Exercise R-2.12 asks for an implementation of __mul__ ,
# for the Vector class of Section 2.3.3, to provide support for the syntax v * 3. Implement the __rmul__ method, to provide additional support for syntax 3 * v.

def __rmul__(self, multiplier):
    result = Vector(len(self))
    for j in range(len(self)):
        result[j] = multiplier * self[j]
    return result
