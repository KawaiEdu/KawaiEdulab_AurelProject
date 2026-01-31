from rec import faktorial, fib, pangkat
from utils import to_int, menu

while True:
    menu()
    p = input("pilih:").strip()
    if p == "0": print("bye!");break
    if p not in {"1","2","3","4"}: print("pilihan tidak valid");continue
    if p == "4": 
        print("anda telah keluar dari program, Terimakasih")
        break
    
    a= to_int(input("masukkan n/angka -1; "))
    if a is None: print("harus angka!") ;continue
    
    if p == "1":
        print("hasil:" , faktorial(a))
    elif p == "2":
        print("hasil: ", fib(a))
    elif p == "3":
        b= to_int(input("masukan angka -2 (pangkat): "))
        if b is None: print("harus angka!");continue
        print("hasil:", pangkat(a, b))
    
    
        