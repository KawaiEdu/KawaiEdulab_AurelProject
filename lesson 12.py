jadwal= []
kegiatan_tambahan= ["mandarin","english","japanese"]


while True:
    print("\nJadwal Kegiatan Harian:", jadwal)
    print("1. Tambah kegiatan")
    print("2. Hapus kegiatan")
    print("3. extend kegiatan")
    print("4. copy kegiatan")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1/2/3/4/5): ")
    
    if pilihan == "1":
        kegiatan = input("Masukkan kegiatan baru: ")
        jadwal.append(kegiatan)
         
    elif pilihan == "2":
        kegiatan = input("Masukkan kegiatan yang ingin dihapus: ")
        if kegiatan in jadwal:
            jadwal.remove(kegiatan)
            print(f"Kegiatan '{kegiatan}' telah dihapus.")
        else:
            print("kegiatan tidak ditemukan!")
     
    elif pilihan == "3":
         jadwal.extend(kegiatan_tambahan)
         print("kegiatan telah digabung.")
    elif pilihan == "4":
        kegiatan_baru= jadwal.copy()
        print(f"kegiatan telah dicopy. {kegiatan_baru}")
    elif pilihan == "5":
        print("semoga harimu menyenangkan")
        break 
    else:
        print("pilihan tidak ditemukan")