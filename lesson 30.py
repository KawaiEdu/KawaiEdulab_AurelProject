class Akun:
    def __init__(self, saldo=0):
        self._saldo= 0
        self.saldo= saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,nilai):
        assert nilai >=0, "saldo tidak boleh negatif"
        self._saldo = nilai
        
a = Akun(5000)
a.saldo += 2500
print(a.saldo)