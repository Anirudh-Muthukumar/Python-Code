def fibo():
    a=-1
    b=1
    while True:
        next=a+b
        yield next
        b,a=next,b