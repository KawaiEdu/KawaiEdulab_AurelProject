def diskon(harga,persen):
    potongan= harga * persen / 100
    return harga - potongan

def pajak(harga,persen):
    tambahan= harga * persen / 100
    return harga + tambahan

while True:
    print("1.hitung diskon")
    print("2.hitung pajak")
    pilihan= int(input("masukan nomor pilihan anda:"))
    
    if pilihan == 1:
        harga = int(input("masukan harga:"))
        persen = int(input("masukan persen:"))
        print(diskon(harga,persen))
    
    elif pilihan == 2:
        harga = int(input("masukan harga:"))
        persen = int(input("masukan persen:"))
        print(pajak(harga,persen))
        
    else:
        print("pilihan tidak ditemukan")
