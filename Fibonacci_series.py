def Fibonacci(n):
    a,b = 0,1
    print(a,b,sep=",",end=",")
    for i in range(n):
        a,b = b , a+b
        print(b,end=",")


Fibonacci(7)