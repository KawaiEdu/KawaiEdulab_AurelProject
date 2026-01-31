class Dompet:
    def __init__(self, saldo=0):
        self._saldo = 0; self.saldo= saldo
        
    @property
    def saldo(self): return self._saldo
    
    @saldo.setter
    def saldo(self, v):
        assert v >= 0, "saldo tidak boleh negatif"
        self._saldo = v
        
    def topup(self, n):
        assert n > 0, "top up harus > 0"
        self._saldo += n
        
    def bayar(self, n):
        assert 0 < n <= self._saldo, "pembayaran tidak valid"
        self._saldo -= n