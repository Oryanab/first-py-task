"""
Implement all functions in only one line of code!
They should contain a single return statement.
If you think of several implementations, do them all.
No need to validate user input anywhere.
"""


from operator import index
from xml.etree.ElementTree import tostring


def sum_digits(num):
    return sum(int(digit) for digit in str(num))
print(sum_digits(22))


def is_palindrome(seq):
    """
    Checks whether a given sequence is a palindrome.
    (without changing the original sequence)

    Hints:
    - there are 2 easy ways:
        - one using builtin functions
        - another using a knife
    """
    return seq==seq[::-1]
print(is_palindrome("roo"))


def is_gmail(string):
    """
    Checks whether a string is a Gmail email address.

    For our purposes, a valid address looks like "abcd@gmail.com".
    It must be a string of alphabetic letters (no dots) followed by '@gmail.com'.
    """
    return string.split('@')[1] == "gmail.com" and len(string.split('@')[0])>0 and len(string.split('@')) == 2
print(is_gmail("@gmail.com"))


def union(items, more_items):
    """
    Unites 2 lists/tuples into a list/tuple that contains all their elements without duplication.
    The return type must be that of the first argument `items`.
    """
    return set(items).union(more_items)
print(union([1, 4, 3], (1, 4, 5)))


# This is not a one-liner challenge, but should be 4 lines max
def distribution(items):
    """
    Finds how many times each item appears in a sequence of items.
    """
    return [[x,items.count(x)] for x in set(items)]
print(distribution(["a","b","b", "b"]))

# remember us? :)
formula1Champions = [
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Alonso",
    "Alonso",
    "Räikkönen",
    "Hamilton",
    "Button",
    "Vettel",
    "Vettel",
    "Vettel",
    "Vettel",
    "Hamilton",
    "Hamilton",
    "Rosberg",
    "Hamilton",
    "Hamilton",
    "Hamilton",
    "Hamilton"
]


def all_time_champion(champions):
    """
    Finds the person has the most wins.

    Hints:
    - distribution
    - max
    - lambda
    """
    return sorted([[champions.count(x),x] for x in set(champions)])[-1][1]
print(all_time_champion(formula1Champions))

def dictify(keys, values):
    """
    Creates a dict mapping the given keys to the given values.
    """
    return [{key:values[index]} for index, key in enumerate(keys)]
    
print(dictify([1,2,3], ["me", "ye", "bo"]))

def is_prime(num):
    """
    Checks whether a number is prime.

    Hints:
    - I can do this any day, and all day long!
    """
    numbers = [2,3,4,5,6,7,8,9,10]
    print(i for i in numbers if type(num/i) != float and num != i)
    return len([i for i in numbers if type(num/i) != float and num != i]) == 0
print(is_prime(4))

def caesar_encrypt(plain, key):
    """
    Encrypts a string using caesar cipher, with the given key as the offset.

    Hints:
    - from string import ascii_letters
    - https://www.youtube.com/watch?v=IjcX3MVSdyA
    """
    pass


def all_time_champion2(champions):
    """
    Your previous code is cool, but now make it shorter!

    Hints:
    - from
    - collections
    - import
    - Counter
    """
    pass


def factorial(num):
    """
    Computes the factorial of a number (1 * 2 * 3 * ... * num).

    Hints:
    - def factorial(num):
          '''
          Computes the factorial of a number (1 * 2 * 3 * ... * num).

          Hints:
          - ...
          '''
          pass
    """
    pass


def compose(*funcs):
    """
    Composes all given functions.
    compose(f, g, h)(x) == f(g(h(x)))

    Hints:
    - from functools import reduce
    """
    pass