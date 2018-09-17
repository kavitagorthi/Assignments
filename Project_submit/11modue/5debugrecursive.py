
# if n value >= 2 will not get any recursion issues

import sys


def my_fun(n):
    if (n>= 2):
        if n == 2:
            return True
        else:
            return n+my_fun(n-1)/2
    else:
        return None

if __name__ == '__main__':
    n = int(2)
    print(my_fun(n))

