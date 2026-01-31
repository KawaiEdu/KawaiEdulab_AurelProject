class Member:
    def __init__(self, id, nama, saldo= 0):
        self._id= id; self._nama = nama
        self._saldo = 0; self.saldo = saldo
        
    @property
    def id(self): return self._id
    @property
    def nama(self): return self._nama
    
    
    @property
    def saldo(self): return self._saldo
    @saldo.setter
    def saldo(self, v):
        assert v >= 0, "saldo tidak boleh negatif"
        self._saldo = v
        
    def isi(self, n):
        assert n > 0, "isi harus > 0"
        self._saldo += n
        
    def beli(self, n):
        assert 0 < n <= self._saldo, "saldo tidak cukup"
        self._saldo -= n
        
    def info(self):
        return f"{self.nama} (#{self.id}) - saldo: {self.saldo}"
    
m = Member(101, "Dara", 10000)
m.beli(2500);m.isi(5000)
print(m.info())