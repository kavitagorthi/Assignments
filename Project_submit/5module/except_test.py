#!/usr/bin/env python3

"""
silly little test module that is designed to trigger Exceptions when
run from the except_exercise.py file
"""

import time

conclude = "And what leads you to that conclusion?"
district = "Finest in the district, sir."
cheese = "It's certainly uncontaminated by cheese."
clean = "Well, it's so clean."
shop = "Not much of a cheese shop really, is it?"
cust = "Customer: "
clerk = "Shopkeeper: "


def fun(reaper):
   try :
        if reaper == 'spam':
            print()
        elif reaper == 'cheese':
            print()
            print('Spam, Spam, Spam, Spam, Beautiful Spam')
        elif reaper == 'mr death':
            print()
            print('{}{}\n{}{}'.format(cust, shop, clerk, district))
   except Exception as e:
          print(e)



def more_fun(language):
    try :
        if language == 'java':
            test = [1, 2, 3]
            test[4] = language
        elif language == 'c':
            print('{}{}\n{}{}'.format(cust, conclude, clerk, clean))
    except IndexError as e:
            print(e)


def last_fun():
    print(cust, cheese)


