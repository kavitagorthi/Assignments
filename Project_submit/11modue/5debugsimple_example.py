
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
    for i in range(int(1e04)):
        l = i + 1
        if i == 777:
            print("terrible bug at ", i)
    result = i + 1
    print(result)

if __name__ == '__main__':
     main()
     print("last statement")

