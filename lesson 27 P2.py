import math
import random
from utils import kali
from utils import max3

while True:
    print("WELCOME TO MY MODUL")
    print("pilih menu \n 1. math \n 2. random \n 3. kali \n 4. max3 \n 5. keluar")
    pilihan= int(input("masukan pilihan yang anda inginkan:"))
    
    if pilihan == 1:
        n = int(input("masukan angka yang anda inginkan:"))
        print(math.sqrt(n))
        print(math.pi)
    elif pilihan == 2:
        print("pilih yang anda inginkan: \n 1. randint \n 2. choice")
        menu= int(input("masukan pilihan anda:"))
        
        if menu == 1:
            try:
                angka1 = int(input("masukan angka yang anda inginkan:"))
                angka2 = int(input("masukan angka batas yang anda inginkan:"))
            except ValueError:
                 print("input harus angka!")
            print(random.randint(angka1,angka2))
        elif menu == 2:
            huruf1 = input("masukan huruf pertama yang kalian inginkan:")
            huruf2 = input("masukan huruf kedua yang kalian inginkan:")
            huruf3 = input("masukan huruf ketiga yang kalian inginkan:")
            
            print(random.choice([huruf1, huruf2 , huruf3]))
            
        else: 
            print("pilihan tidak valid!")
            break
    elif pilihan == 3:
        a = int(input("masukan angka untuk A:"))
        b = int(input("masukan angka untuk B:"))
        print(kali(a,b))
    elif pilihan == 4:
        x = int(input("masukan x:"))
        y = int(input("masukan y:"))
        z = int(input("masukan z:"))
        print(max3(x,y,z))
    elif pilihan == 5:
        print("THANKS FOR YOUR TIMES!")
        break
    else:
        print("pilihan tidak valid!")
        
