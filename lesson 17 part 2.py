def tulis_catatan():
    catatan = input("masukan catatan anda: ")
    with open("catatan.txt", "a") as file:
        file.write(catatan + "\n")
    print("catatan berhasil disimpan!")
    
def baca_catatan():
    try:
        with open("catatan.txt", "r") as file:
            print("\n catatan harian anda:")
            print(file.read())
    except FileNotFoundError:
        print("belum ada catatan yang tersimpan.")
        
def hapus_catatan():
    catatan = input("masukan catatan baru anda: ")
    with open("catatan.txt", "w") as file:
        file.write(catatan + "\n")
    print("catatan berhasil dihapus")
        
while True:
    print("\n pilih menu:")
    print("1. tulis catatan")
    print("2. baca catatan")
    print("3. hapus catatan")
    print("4. keluar")
    pilihan = input("masukkan pilihan (1/2/3/4):")
    
    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        hapus_catatan()
    elif pilihan == "4":
        print("terimakasih! sampai jumpa.")
        break
    else:
        print("pilihan tidak valid. silahkan coba lagi.")