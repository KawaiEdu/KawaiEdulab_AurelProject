def faktorial(n):
    if n <= 1: return 1
    return n * faktorial(n-1)

def jumlah(n):
    if n == 0: return 0
    return n + faktorial(n-1)

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

while True:
    print("\\n [1] Faktorial [2] Jumlah 1..n [3] Fibonacci [0] Keluar")
    p = input("pilih:")
    if p == "0":
        break
    n = int(input("n: "))
    if p == "1":
        print("hasil:", faktorial(n))
    elif p == "2":
        print("hasil:", jumlah(n))
    elif p == "3":
        print("hasil:", fib(n))
    else:
        print("ERROR")
        print("silahkan coba lagi!")