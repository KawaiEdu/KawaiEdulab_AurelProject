class Card:
    def __init__(self , q , a):
        assert q and a, "Pertanyaan dan Jawaban wajib"
        self.q = q; self.a = a
    def to_dict(self): return{"q": self.q, "a": self.a}