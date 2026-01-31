import random
from .utils import ask
class Trainer:
    def __init__(self, deck):
        self.deck = deck
    def random_card(self):
        if not self.deck.cards:return None
        return random.choice(self.deck.cards)
    def play(self, rounds=5):
        if not self.deck.cards:
            print("Belum ada kartu."); return 0
        score = 0
        for i in range(1, rounds+1):
            c = self.random_card()
            print(f"Q{i}: {c.q}")
            ans = ask("Jawab: ")
            if ans.strip().lower() == c.a.strip().lower():
                print("Benar! +1"); score += 1
            else:
                print(f"Salah. Jawaban: {c.a}")
        print(f"Skor kamu: {score}/{rounds}")
        return score