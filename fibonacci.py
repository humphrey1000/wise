def fib(x):
    a,b=0,1
    while b < x:
        print(b,end=",")
        a,b = b,a+b

fib(10)
