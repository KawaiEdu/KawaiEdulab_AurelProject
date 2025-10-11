angka = float(input("masukan angka:"))

if angka % 2 == 0:
    print(f"{angka} adalah genap")
elif angka % 2 == 1:
    print(f"{angka} adalah sisa 1")
else:
    print(f"{angka} adalah ganjil")
