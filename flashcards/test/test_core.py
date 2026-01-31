from models.card import Card
from models.deck import Deck

def test_add_and_list():
    d = Deck(path="data/test_deck.json")
    d.cards=[]; d.save()
    d.add("2=2", "4")
    assert len(d.list_cards())==1
if __name__=="__main__":
    test_add_and_list(); print("semua tes lulus!")