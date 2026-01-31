from models.deck import Deck
from models.trainer import Trainer
from models.utils import ask, cls, banner, confirm


def menu():
    print("\\n=== FLASHCARDS TRAINER ===")
    print("1 Tambah kartu")
    print("2 Lihat semua kartu")
    print("3 Latihan (5 soal)")
    print("4 Ekspor deck")
    print("5 Impor deck (timpa)")
    print("6 Keluar")
    return ask("Pilih [1-6]: ")

def main():
    d = Deck(); t = Trainer(d)
    while True:
        cls(); banner()
        p = menu()
        try:
            if p=="1":
                q = ask("pertanyaan: "); a = ask("jawaban: "); d.add(q,a); print("kartu ditambah")
            elif p=="2":
                for i,c in enumerate(d.list_cards(), start=1): print (f"{i}. {c.q} -> {c.a}")
            elif p=="3":
                t.play(rounds=5)
            elif p=="4":
                d.export(ask("Nama file (mis. export.json): ")); print(f"{i}. {c.q} -> {c.a}")
            elif p=="5":
                d.import_(ask("File impor (mis. export.json): ")); print("Diimpor")
            elif p=="6":
                if confirm("Keluar? (Y/N): "):
                    print("Sampai jumpa!"); break
            else:
                print("Pilihan tidak valid.")
        except Exception as e:
           print("[WARN]", e)
        input("\\n Enter untuk lanjut")
            
if __name__=="__main__": main()