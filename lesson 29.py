class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def perkenalan(self):
        return f"Halo, buku ini berjudul {self.judul} dan ditulis oleh {self.penulis}"

papabumi = buku("papah bumi & bumi", "hellnyla")
print(papabumi.perkenalan())