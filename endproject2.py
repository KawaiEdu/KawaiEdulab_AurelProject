def tampilan_menu():
    print("selamat datang di progam to do list!!!!")
    print("pilih menu:")
    print("1. tambah tujuan negara")
    print("2. tampilkan daftar tujuan negara")
    print("3. hapus tujuan negara")
    print("4. simpan daftar ke file")
    print("5. muat daftar ke file")
    print("6. keluar")
    
def tambah_negara(daftar):
    negara=input("masukan nama negara:")
    daftar.append(negara) 
    print("berhasil ditambahkan ke daftar tugas.")
    
def tampilkan_daftar(daftar):
    if daftar:
        print("\n daftar negara:")
        for i,negara in enumerate(daftar,start=1):
            print("{}.{}".format(i, negara))
    else:
        print("daftar negara tidak ditemukan.")
        
def hapus_negara(daftar):
    tampilkan_daftar(daftar)
    try:
        nomor=int(input("masukan nama negara yang ingin dihapus:"))
        if 1 <= nomor <= len(daftar):
            negara= daftar.pop(nomor -1)
            print("{} berhasil dihapus dari daftar tujuan negara.".format(negara))
        else:
            print("nomor negara tidak valid.")
    except ValueError:
        print("input harus angka:")

def simpan_daftar(daftar):
    try:
        with open("daftar_tujuan_negara.txt", "w") as file:
            for negara in daftar:
                file.write(negara + "\n")
                print("daftar negara telah berhasil tersimpan ke file.")
    except Exception as e:
        print("terjadi kesalahan saat menyimpan!:{}".format(e))

def muat_daftar():
    try:
        with open("daftar_tujuan_negara.txt", "r") as file:
            daftar = [line.strip()for line in file]
        print("daftar negar1a berhasil dimuat dari file.")
        return daftar
    except IOError:
        print("file daftar negara tidak ditemukan. Membuat daftar baru. ")
        return[]
    except Exception as e:
        print("terjadi kesalahan saat memuat: {}".format(e))
        

daftar= muat_daftar() 
while True:
    tampilan_menu()
    pilihan = int(input("masukan pilihan (1-6): "))
    
    if pilihan == 1:
        tambah_negara(daftar)
    elif pilihan == 2:
        tampilkan_daftar(daftar)
    elif pilihan == 3:
        hapus_negara(daftar)
    elif pilihan == 4:
        simpan_daftar(daftar)
    elif pilihan == 5:
        daftar= muat_daftar()
    elif pilihan == 6:
        print("terimakasih, sampai jumpa!!")
        break
    else:
        print("pilihan tidak valid, silahkan coba lagi!")

        
    