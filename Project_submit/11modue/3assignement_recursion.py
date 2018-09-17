
def outer(exp):
    def inner(n,n1):
        if n>0:
            return exp(n,n1)
        else:
            print("enter valid positive number")
    return inner




@outer
def fact_fun(x,res = 1):
    if (x == 1):
        return res
    else :
        return fact_fun(x-1,res*x)

k = fact_fun(5,1)
print(k)


