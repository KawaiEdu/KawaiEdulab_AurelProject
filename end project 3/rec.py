def faktorial(n):
    if n <= 1: return 1
    return n * faktorial(n-1)

def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)

def pangkat(a,b):
    if b == 0: return 1
    return a * pangkat(a, b-1)
