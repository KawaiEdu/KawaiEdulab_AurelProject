daftar_negara= set()

while True:
    nama_negara= input("masukan nama negara yang ingin dikunjungi(atau ketik 'selesai' untuk berhenti):")
    if nama_negara.lower() == "selesai":
        break
    daftar_negara.add(nama_negara)
    
print("daftar negara yang anda ingin kunjungi:")
for nama_negara in daftar_negara:
    print(f"-{nama_negara}")