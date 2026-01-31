class skor:
    def __init__(self, nilai_awal=0):
        self.nilai= nilai_awal
        
    def tambah(self,n):
        self.nilai += n
        return self.nilai
    
    def reset(self,n=0):
        self.nilai = n
        return self.nilai
    
    def kurang(self,n):
        self.nilai -= n
        return self.nilai

class player:
    def __init__(self, nama: str, umur: int):
        self.nama : str= nama
        self.umur : int= umur
        self.skor : skor= skor()
        
    def info(self):
        return f"player: {self.nama}, umur: {self.umur}, skor: {self.skor.nilai}"
    
skor1 = skor()
print(skor1.tambah(10))
print(skor1.reset())

pemain1 = player("yuan", "29")
print(pemain1.info())

pemain1.skor.tambah(1000)
print(pemain1.info())
        