class Hewan:
    def __init__(self, nama,jenis,suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        
    def bergerak(self):
        return f"{self.nama} sedang bergerak."
    
    def bersuara(self):
        return f"{self.nama} bersuara: {self.suara}"
    
class Manusia:
    def __init__(self,nama,umur,pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan
        
    def perkenalan(self):
        return f"Halo, nama saya {self.nama}, umur {self.umur} tahun, bekerja sebagai {self.pekerjaan}."
    
    def berkerja(self):
        return f"{self.nama} sedang berkerja sebagai {self.pekerjaan}."
    
class Benda:
    def __init__(self,nama,fungsi,bahan):
        self.nama = nama
        self.fungsi = fungsi
        self.bahan = bahan
        
    def deskripsi(self):
        return f"{self.nama} terbuat dari {self.bahan}, digunakan untuk {self.fungsi}."
    
def main():
    kucing = Hewan("Kitty", "kucing", "meong")
    anjing = Hewan("Doggo", "anjing", "guk guk")
    manusia1 = Manusia("Yoesuf", 22, "TNI AD")
    manusia2 = Manusia("Lidya", 22, "Dokter")
    kursi = Benda("Kursi", "Tempat duduk" , "Kayu Jati")
    
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Tampilkan aktivitas Hewan")
        print("2. Tampilkan aktivitas Manusia")
        print("3. Tampilkan deskripsi Benda")
        print("4. Keluar")
        
        pilihan = input("Masukan pilihan(1-4): ")
        
        if pilihan == "1":
            print(kucing.bergerak())
            print(kucing.bersuara())
            print(anjing.bergerak())
            print(anjing.bersuara())
            
        elif pilihan == "2":
            print(manusia1.perkenalan())
            print(manusia1.berkerja())
            print(manusia2.perkenalan())
            print(manusia2.berkerja())
            
        elif pilihan == "3":
            print(kursi.deskripsi())
            
        elif pilihan == "4":
            print("anda telah keluar dari program, terimakasih!")
            break
            
        else:
            print("Pilihan tidak valid, coba lagi.")
            
            
if __name__ == "__main__":
    main()