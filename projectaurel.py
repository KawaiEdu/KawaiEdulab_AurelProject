import numpy as np
import statistics as stat

while True:
    print("welcome to my project!")
    print("menu:")
    print("\n 1.mean \n 2.median \n 3.modus \n 4.keluar")
    pilihan = int(input("masukan menu pilihan anda:"))
    
    if pilihan == 1:
        print("berapa angka yang anda inginkan?")
        print("\n a.) 2 angka \n b.) 3 angka \n c.) 4 angka \n d.) 5 angka  ")
        menu = input("masukan pilihan yang anda inginkan, harus huruf!:")
        
        if menu == "a":
            angka1= int(input("masukkan angka pertama yang anda inginkan:"))
            angka2= int(input("masukkan angka kedua yang anda inginkan:"))
            hasil2 = (angka1 + angka2) / 2
            print("hasilnya adalah:",hasil2) 
        elif menu == "b":
            angka1= int(input("masukkan angka pertama yang anda inginkan:"))
            angka2= int(input("masukkan angka kedua yang anda inginkan:"))
            angka3= int(input("masukkan angka ketiga yang anda inginkan:"))
            hasil3= (angka1 + angka2 + angka3) / 3
            print("hasilnya adalah:", hasil3)
        elif menu == "c":
            angka1= int(input("masukkan angka pertama yang anda inginkan:"))
            angka2= int(input("masukkan angka kedua yang anda inginkan:"))
            angka3= int(input("masukkan angka ketiga yang anda inginkan:"))
            angka4= int(input("masukkan angka keempat yang anda inginkan:"))
            hasil4= (angka1 + angka2 + angka3 + angka4) / 4
            print("hasilnya adalah:", hasil4)
        elif menu == "d":
            angka1= int(input("masukkan angka pertama yang anda inginkan:"))
            angka2= int(input("masukkan angka kedua yang anda inginkan:"))
            angka3= int(input("masukkan angka ketiga yang anda inginkan:"))
            angka4= int(input("masukkan angka keempat yang anda inginkan:"))
            angka5= int(input("masukkan angka keempat yang anda inginkan:"))
            hasil5= (angka1 + angka2 + angka3 + angka4 + angka5) / 5
            print("hasilnya adalah:", hasil5)
    elif pilihan == 2:
        data = []
        kali = int(input("Masukkan Berapa kali looping: "))
        for i in range(kali):
            angka = int(input(f"Masukkan angka ke {i+1} yang diinginkan: "))
            data.append(angka)
        median = np.median(data)
        print("Median:", median)
    elif pilihan == 3:
        data = []
        kali= int(input("masukan berapa kali looping: "))
        for i in range(kali):
            angka = int(input(f"masukan angka ke {i+1} yang diinginkan: "))
            data.append(angka) 
        modus = stat.mode(data)
        print(f"Modus dari data tersebut adalah {modus}")      
    elif pilihan == 4:
        print("terimakasih telah menggunakan program ini!")
        break
    else:
        print("silahkan coba lagi!")
        
        