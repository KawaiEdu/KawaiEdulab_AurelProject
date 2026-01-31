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
    
    
skor = skor()
print(skor.tambah(10))
print(skor.reset())
print(skor.kurang(2))