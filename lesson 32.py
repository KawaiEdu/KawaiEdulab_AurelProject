class Kucing:
    def suara(self):return "meong"
    
class Anjing:
    def suara(self):return "guk"
    
def bunyikan(hewan):
    print(hewan.suara())
    
bunyikan(Kucing())
bunyikan(Anjing())