daftar_belanja = []

while True:
    print("\n daftar belanja:", daftar_belanja)
    print("1. tambah item")
    print("2. hapus item")
    print("3. keluar")
    pilihan = input ("pilih opsi: (1/2/3):")
    if pilihan == "1":
        item = input("masukan nama item yang ingin ditambahkan: ")
        daftar_belanja.append(item)
    elif pilihan == "2":
        item = input("masukan nama item yang ingin dihapus: ")
        if item in daftar_belanja :
            daftar_belanja.remove(item)
        else:
            print("item tidak ditemukan dalam daftar!")
    elif pilihan == "3":
        print("Thanks for u bcs doing this program!")
        break
    else:
        print("pilihan tidak valid, coba lagi.")