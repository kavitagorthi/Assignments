#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun

print("Whoops! there is a joke for : spam")
first_try = ['spam', 'cheese', 'mr death']

joke = fun(first_try[0])

try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
finally:
    langs = ['java', 'c', 'python']
    more_joke = more_fun(langs[1])
    last_fun()

