# if the value of i was 50 and above the zeroDivisionError will occur try and except block will handle it.


def my_fun():

    for i in range(1, 500):
        try :
             123 / (50 - i)
        except ZeroDivisionError:
            print("Tried to divide by zero. Var i was {} and above. Recovered gracefully.".format(i))

def secret_print():
    print("HERE!")



if __name__=='__main__':
    secret_print()
    my_fun()

