
def main():
    x = 'main'
    one()

def one():
    y = 'one'
    two()

def two():
    z = 'two'
    long_loop()

def long_loop():
    try:
        for i in range(2, int(1e03), 5):
            for j in range(3, int(1e03), 7):
                for k in range(12, int(1e03)):
                                    z = k / (i % k + j % k)


    except ZeroDivisionError:
        print("Tried to divide by zero. Var i was {}  and k was {}  and j was {} . Recovered gracefully.".format(i,k,j))




if __name__ == '__main__':
    main()
    print("last statement")

