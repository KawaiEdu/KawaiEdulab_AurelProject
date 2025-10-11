daftar_buah_favorit = []

while True:
    for i in range (5):
        buah = input("masukan nama buah yang ingin ditambahkan: ")
        daftar_buah_favorit.append(buah)
    
    for favorit in daftar_buah_favorit:
        print("aku menyukai buah", favorit)