class Produk:
    def __init__(self, nama, harga):
        self.nama = nama; self.harga= harga
    def info(self):
        return f"{self.nama} - Rp{self.harga}"
    
class Buku(Produk):
    def __init__(self, nama, harga, penulis):
        super().__init__(nama, harga)
        self.penulis = penulis
    def info(self):
        return f"{self.nama} oleh {self.penulis} - Rp{self.harga}"
    
b1 = Buku("phyton fun" , 75000 , "devy")
print(b1.info()) 