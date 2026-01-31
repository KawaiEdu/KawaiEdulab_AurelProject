class Persegi:
    def __init__(self, s): self.s=s
    def luas(self): return self.s*self.s
    
class Lingkaran:
    def __init__(self, r): self.r=r
    def luas(self): return 3.14*self.r*self.r
    
bentuk= [Persegi(2), Lingkaran(3), Persegi(5)]
total = 0
for b in bentuk:
    total += b.luas()
print(total)