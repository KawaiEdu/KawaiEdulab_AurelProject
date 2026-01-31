import json, os
from .card import Card

class Deck:
    def __init__(self, path="data/deck.json"):
        self.path = path
        self.cards = []
        self._load()
        
    def _load(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self.save(); return
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.cards= [Card(**c)for c in data.get("cards", [])]
        
    def save(self):
        with open(self.path, "w" , encoding="utf-8",) as f:
            json.dump({"cards": [c.to_dict()for c in self.cards]}, f, ensure_ascii=False, indent=2)
            
    def add(self, q, a):
        self.cards.append(Card(q, a)); self.save()
        
    def list_cards(self):
        return list(self.cards)
    def export(self, out_path):
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"cards":[c.to_dict() for c in self.cards]}, f, ensure_ascii=False,indent=2)
    def import_(self, in_path):
        with open(in_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.cards = [Card(**c) for c in data.get("cards", [])]
        self.save()