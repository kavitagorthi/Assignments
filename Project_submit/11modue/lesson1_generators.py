from itertools import islice

class genert:

    def fib_gtor(self):
        curr  = 1
        prev = 0
        while True:
           yield  prev
           prev,curr = curr,curr+prev

    def sum_gtor(self):
        curr  = 0
        i =0
        while True:
           i = i +1
           yield curr
           curr = curr+i

    def double_gtor(self):
        i =2
        while True:
           i = i+1
           if(i%2 ==1):
               yield i

    def prime_gtor(self):
        i =1
        while True:
             i = i+1
             if(i%2 == 1):
               yield i
class output:

    def __init__(self):
        c1 = genert()
        s1 =c1.fib_gtor()
        k1= list(islice(s1,10))
        k2 = k1.pop(0)
        print("fibnacci series", k1)
        s2 = c1.sum_gtor()
        k3 =list(islice(s2,10))
        print("sum of integers ",k3)
        s3 =c1.double_gtor()
        k4 = list(islice(s3,10))
        print("Double the integer",k4)
        s4 =c1.prime_gtor()
        k5 =list(islice(s4,10))
        k5.insert(0,2)
        print("prime numbers",k5)

c1=output()