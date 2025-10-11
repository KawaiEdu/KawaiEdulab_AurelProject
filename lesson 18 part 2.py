def kafe():
    try:
        print("\npilihan menu")
        print("\ncoffe")
        print("1. americano 18.000")
        print("2. espresso 16.000")
        print("3. latte 20.000")
        print("4. aren latte 21.000")
        print("5. butterscotch sea salt crumble 25.000")
        print("6. spanish latte 22.000")
        print("\nnon-coffe")
        print("7. matcha latte 23.000")
        print("8. choco lava 22.000")
        print("9. chocochesee 25.000 ")
        pilih_menu = int(input("masukan menu pilihan pelanggan:"))
        
        print("\nmetode pembayaran")
        print("1.tunai")
        print("2.Qris")
        metode = int(input("pilih metode pembayaran:"))
        if metode == 1:
            tunai = int(input("masukan uang yang diterima:"))
            if pilih_menu == 1:
                kembalian = tunai - 18000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 2:
                kembalian = tunai - 16000
                print("kembalian adalah:", kembalian) 
            elif pilih_menu == 3:
                kembalian = tunai - 20000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 4:
                kembalian = tunai - 21000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 5:
                kembalian = tunai - 25000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 6:
                kembalian = tunai - 22000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 7:
                kembalian = tunai - 23000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 8:
                kembalian = tunai - 22000
                print("kembalian adalah:", kembalian)
            elif pilih_menu == 9:
                kembalian = tunai - 25000
                print("kembalian adalah:", kembalian)
            else:
                print("mohon maaf menu telah kosong!")
        elif metode == 2:
            print("scan barcode yang telah disediakan")
        else:
            print("tidak ada pilihan lagi ") 
            
    except ValueError:
        print("input harus angka!")

while True:
    print("\n menu cafe sejuta kopi")
    kasir = input("masukan nama kasir:")
    nama = input("masukan nama pelanggan:")
    kafe()
    print("Terimakasih!")
    break
                           
                           
                           
                           
                           
                           
                           