# Write a short Python function, is multiple(n, m), that takes two integer values
# and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def multiple(n, m):
    return True if n % m == 0 else False

print(multiple(15, 5))


# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise.
# However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
     return False if k & 1 else True

print(is_even(105))

# Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    sorted_data = sorted(data)
    x,y = sorted_data[0], sorted_data[(len(sorted_data) - 1)]
    return x,y

print(minmax([1, 2, 3, 4, 5, 30, 100, 2000]))


# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    return sum([k * k for k in range(1, n) if k < n])

print(sum_of_squares(8))

# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the odd positive integers smaller than n.

def sum_of_squares(n):
    return sum([k * k for k in range(1, n) if (k % 2 != 0 and k < n)])

print(sum_of_squares(8))


# Python allows negative integers to be used as indices into a sequence, such as a string.
# If string s has length n, and expression s[k] is used for in- dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?

# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
print(list(range(50, 90, 10)))

# What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
print(list(range(8, -10, -2)))

# Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
list_comprehension = [pow(2, k) for k in range(0, 9)]
print(list_comprehension)

# Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange,
# with parameterization similar to the built-in range function, that return a random choice from the given range.
# Using only the randrange function, implement your own version of the choice function.

def my_choice(data):
    import random
    try:
        sorted_sequence = sorted(data)
        print(random.randrange(sorted_sequence[0], sorted_sequence[len(sorted_sequence) - 1] + 1))
    except TypeError:
        print('Argument supplied must be a sequence')



# Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before,
# and compare this method to an equivalent Python function for doing the same thing.

def reversa(data):
    reversed = []
    for i in range(-1, -len(data) - 1, -1):
        reversed.append(data[i])
    return reversed

print(reversa([5,6,7,8,9,10]))

# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

def odd_product(data):
    count = 0
    for number in data:
        if number % 2 != 0:
            count += 1
    return count if count >= 2 else None

print(odd_product([1,2,3,4,5]))


# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

def differen(data):
    distinct_list = set(data)
    if len(distinct_list) != len(data):
        return False, distinct_list
    else:
        return True, distinct_list

print(differen([1,2,3,4,5]))

# In our implementation of the scale function(page25),the body of the loop executes the command data[j] * = factor.
# We have discussed that numeric types are immutable,
# and that use of the  *= operator in this context causes the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?
#

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data

def scale(data, factor):
    for val in data:
        val  *= factor
    return data

print(scale([1,2,3,4], 2))

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

fibonacci_multiplier = [i * (i + 1) for i in range(0, 10)]
print(fibonacci_multiplier)

# Demonstrate how to use Python’s list comprehension syntax to produce thelist[ a , b , c ,..., z ],
# but without having to type all 26 such characters literally.

english_alphabets = [chr(i) for i in range(97, 123)]
print(english_alphabets)


# Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b.
# That is, it returns an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.

def dot_product(first_list, second_list):
    real_dot = []
    if len(first_list) != len(second_list):
        return "Lists must be of equal length"
    for i in range(0, len(first_list)):
        real_dot.append(first_list[i] * second_list[i])
    return real_dot

print(dot_product([1,2,6], [1,2,9]))

# Write a short Python function that counts the number of vowels in a given
# character string.


def no_of_vowels(string):
    number_of_vowels = 0
    character_list = list(string)
    for i in character_list:
        if ord(i) == 97 or ord(i) == 101 or ord(i) == 105 or ord(i) == 111 or ord(i) == 117:
            number_of_vowels += 1
    return number_of_vowels

print(no_of_vowels("aeiou"))


# Write a short Python function that takes a string s,representing a sentence,
# and returns a copy of the string with all punctuation removed.
# For example, if given the string "Let's try, Mike.", this function would return "Lets try Mike".

