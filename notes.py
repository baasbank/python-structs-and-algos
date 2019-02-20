# temperature = 5.2
# print("The temperature is: ", temperature)
#
# original = temperature
# print("The value for original is :", original)
#
# temperature = temperature + 0.8
# print("The NEW value for temperature is: ", temperature)
#
# print("The NEW value for original is :", original)

# int('7f', 16) is a way to create an integer from a non-decimal number.
# --- Where the first argument is the number, and the second argument is its base.

# In the expression a = 2; a is an identifier and 2 is a literal.

## LISTS
# One way to split a string is to call the list() constructor and pass it the value of the string to be split
# For example list('hello') produces ['h', 'e', 'l', 'l', 'o']

##SETS
# The set class represents a collection of elements without duplicates and order
# {} doesn't represent an empty set; it represents an empty dictionary
# The constructor is used to make an empty set; like so: set()
# Passing a string to the set() constructor makes a set of elements out of the string
# For example: set('hello') will produce {'h', 'e', 'l', 'o'}

# a = str('hello')
# b = str('welcome')
# print(2 * a)

#FOR LOOP
# data = list('012345678')
# for j in range(len(data)):
#     print(j)
# biggest = data[0]
# for member in data:
#     if member > biggest:
#         biggest = member
# print (biggest)
# print(data)

#WHILE LOOP
# data = list('0123456785')
# biggest = data[0]
# i = 0
# while i < len(data):
#     if data[i] > biggest:
#         biggest = data[i]
#     i += 1
# print(biggest)

#FUNCTIONS
# def count(data, target):
#     n = 0
#     for item in data:
#         if item == target:
#             n += 1
#     return n
#
# a = ['2', '3', '2', '3,', '3', 3]
# print(count(a, 3))

# If a return statement is executed without an argument, the value None is returned

# I/O

# Calling print() without an argument returns a new line
# The separator between arguments supplied to the print function can be customized like so:
# print(a, b, c, sep=':') to use a colon as a separator.
# Also, the end character can be customized using the end keyword and the character you want to end with.

# age = int(input('Enter your age in years: '))
# max_heart_rate = 206.9 - (0.67  * age) # as per Med Sci Sports Exerc.
# target = 0.65 *  max_heart_rate
# print('Your target fat-burning heart rate is ', target)


#FILES
# fp = open('test.txt', 'a')
#print(fp.read())
# fp.seek(10)
# print(fp.readline())
# fp.write('I am adding this line to the file \n')
# fp.close()
# fp = open('test.txt')
# print(fp.read())

# EXCEPTIONS
# user_input = int(input('Please enter a number '))
# if user_input < 0:
#     raise ValueError('Input cannot be negative')
# else:
#     print('You entered', user_input)
# The try-except structure is used to run code and catch exceptions that may be thrown during execution
# 3 ways to write an except statement
# -- except ZeroDivisionError:
# -- except IOError as e:
# -- except (ValueError, EOFError):
# A try block can have more than one except block

# ITERATORS AND GENERATORS
# data = [1, 2, 3, 4, 5, 6]
# iterator = iter(data)
# i = 0
# for i in iterator:
#     print(next(iterator))

# dicki = {"key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4"}
# print(dicki.keys())
# print(dicki.values())
#print(dicki.items())
# print(list(dicki.items()))

# CONDITIONAL EXPRESSIONS
# expr1 if condition else expr2

# def testing(input):
#     print('Less than') if input < 10 else print('Greater than')
#     return
#
# testing(8)

# COMPREHENSION SYNTAX
# def facti(n):
#     factors = [k for k in range(1, n+1) if n % k == 0]
#     return factors
#
# print(facti(10))

# comprehension syntax can be used for iterable types; list, set, dictionary, generator
# n = 30
# print([k for k in range(1, 1 + n) if k % 2 == 0])

# PACKING AND UNPACKING SEQUENCES
# data = 2, 4, 5, 6, 2, 3
# print(data)

# quotient, remainder = divmod(10, 2)
# print(quotient, remainder)

# NAMESPACES
# The function, dir, reports the names of the identifiers in a given namespace (i.e., the keys of the dictionary),
# while the function, vars, returns the full dictionary.