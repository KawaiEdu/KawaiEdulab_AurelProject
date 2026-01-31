from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self): ...
    
class Persegi(Bentuk):
    def __init__(self, s): self.s=s
    def luas(self): return self.s*self.s
    
class Mesinsuara:
    def __init__(self, bunyi):self.bunyi = bunyi
    def suara(self): return self.bunyi
    
class Robotkucing:
    def __init__(self):
        self.audio = Mesinsuara("meong-robot")
    def suara(self):
        return self.audio.suara()
    
rk = Robotkucing()
print(rk.suara())