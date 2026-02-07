import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

from models.deck import Deck

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Trainer GUI")
        self.root.geometry("500x450")

        # Inisialisasi Deck
        self.deck = Deck()

        # --- TAMPILAN MENU UTAMA ---
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)

        # Judul
        tk.Label(self.main_frame, text="FLASHCARDS TRAINER", font=("Helvetica", 18, "bold")).pack(pady=20)

        # Tombol Menu
        btn_opts = {"width": 30, "pady": 5}
        
        tk.Button(self.main_frame, text="1. Tambah Kartu", command=self.menu_tambah, **btn_opts).pack(pady=5)
        tk.Button(self.main_frame, text="2. Lihat Semua Kartu", command=self.menu_lihat, **btn_opts).pack(pady=5)
        tk.Button(self.main_frame, text="3. Latihan (5 Soal)", command=self.menu_latihan, bg="#dff9fb", **btn_opts).pack(pady=5)
        tk.Button(self.main_frame, text="4. Ekspor Deck", command=self.menu_ekspor, **btn_opts).pack(pady=5)
        tk.Button(self.main_frame, text="5. Impor Deck", command=self.menu_impor, **btn_opts).pack(pady=5)
        
        tk.Button(self.main_frame, text="6. Keluar", command=self.keluar, bg="#ffcccc", width=30).pack(pady=20)

        # Status Bar
        self.lbl_status = tk.Label(root, text="Siap belajar.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.lbl_status.pack(side=tk.BOTTOM, fill=tk.X)

    def menu_tambah(self):
        top = tk.Toplevel(self.root)
        top.title("Tambah Kartu")
        top.geometry("350x250")

        tk.Label(top, text="Pertanyaan (Front):").pack(pady=5)
        entry_q = tk.Entry(top, width=40)
        entry_q.pack(pady=5)

        tk.Label(top, text="Jawaban (Back):").pack(pady=5)
        entry_a = tk.Entry(top, width=40)
        entry_a.pack(pady=5)

        def simpan():
            q = entry_q.get().strip()
            a = entry_a.get().strip()
            if q and a:
                self.deck.add(q, a)
                messagebox.showinfo("Sukses", "Kartu berhasil ditambahkan!")
                # Kosongkan field agar bisa input lagi
                entry_q.delete(0, tk.END)
                entry_a.delete(0, tk.END)
                entry_q.focus()
            else:
                messagebox.showwarning("Error", "Pertanyaan dan Jawaban tidak boleh kosong.")

        tk.Button(top, text="Simpan", command=simpan, bg="lightblue").pack(pady=20)

    def menu_lihat(self):
        top = tk.Toplevel(self.root)
        top.title("Daftar Kartu")
        top.geometry("500x400")

        cols = ("No", "Pertanyaan", "Jawaban")
        tree = ttk.Treeview(top, columns=cols, show='headings')
        
        tree.heading("No", text="No")
        tree.heading("Pertanyaan", text="Pertanyaan")
        tree.heading("Jawaban", text="Jawaban")
        
        tree.column("No", width=50, anchor="center")
        tree.column("Pertanyaan", width=200)
        tree.column("Jawaban", width=200)
        
        # Scrollbar
        scroll = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Masukkan data
        cards = self.deck.list_cards()
        for i, c in enumerate(cards, start=1):
            tree.insert("", "end", values=(i, c.q, c.a))

    def menu_latihan(self):
        """Membuat logika latihan versi GUI"""
        all_cards = self.deck.list_cards()
        
        if not all_cards:
            messagebox.showwarning("Kosong", "Belum ada kartu. Silakan tambah kartu dulu!")
            return

        # Ambil maksimal 5 kartu secara acak
        jumlah_soal = min(5, len(all_cards))
        session_cards = random.sample(all_cards, jumlah_soal)
        
        # Jendela Latihan
        game_win = tk.Toplevel(self.root)
        game_win.title("Latihan Flashcard")
        game_win.geometry("400x300")

        # Variabel State Game
        self.current_idx = 0
        self.score = 0
        self.quiz_cards = session_cards

        # UI Elements Latihan
        lbl_progress = tk.Label(game_win, text=f"Soal 1 / {jumlah_soal}", fg="gray")
        lbl_progress.pack(pady=5)

        lbl_soal = tk.Label(game_win, text="", font=("Arial", 14, "bold"), wraplength=380)
        lbl_soal.pack(pady=20)

        entry_jawaban = tk.Entry(game_win, font=("Arial", 12))
        entry_jawaban.pack(pady=5)
        entry_jawaban.bind("<Return>", lambda event: cek_jawaban()) # Bisa tekan Enter

        lbl_feedback = tk.Label(game_win, text="", font=("Arial", 10, "italic"))
        lbl_feedback.pack(pady=10)

        def tampilkan_soal():
            if self.current_idx < len(self.quiz_cards):
                card = self.quiz_cards[self.current_idx]
                lbl_progress.config(text=f"Soal {self.current_idx + 1} / {jumlah_soal}")
                lbl_soal.config(text=card.q)
                entry_jawaban.delete(0, tk.END)
                entry_jawaban.config(state="normal")
                entry_jawaban.focus()
                lbl_feedback.config(text="")
                btn_submit.config(state="normal")
            else:
                selesai()

        def cek_jawaban():
            user_ans = entry_jawaban.get().strip().lower()
            correct_ans = self.quiz_cards[self.current_idx].a.strip().lower()
            
            if user_ans == correct_ans:
                self.score += 1
                lbl_feedback.config(text="✅ Benar!", fg="green")
            else:
                lbl_feedback.config(text=f"❌ Salah! Jawaban: {self.quiz_cards[self.current_idx].a}", fg="red")
            
            # Disable input agar user membaca feedback dulu
            entry_jawaban.config(state="disabled")
            btn_submit.config(state="disabled")
            
            # Lanjut ke soal berikutnya setelah 1.5 detik
            self.current_idx += 1
            game_win.after(1500, tampilkan_soal)

        def selesai():
            game_win.destroy()
            msg = f"Latihan Selesai!\nSkor Anda: {self.score} dari {jumlah_soal}"
            messagebox.showinfo("Hasil", msg)

        btn_submit = tk.Button(game_win, text="Jawab", command=cek_jawaban, bg="#badc58")
        btn_submit.pack(pady=5)

        # Mulai soal pertama
        tampilkan_soal()

    def menu_ekspor(self):
        # Menggunakan File Dialog agar user tidak perlu mengetik path manual
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if filepath:
            try:
                self.deck.export(filepath)
                messagebox.showinfo("Sukses", f"Deck berhasil diekspor ke:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def menu_impor(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if filepath:
            if messagebox.askyesno("Konfirmasi", "Impor akan menimpa data deck saat ini. Lanjut?"):
                try:
                    self.deck.import_(filepath)
                    messagebox.showinfo("Sukses", "Deck berhasil diimpor.")
                    self.lbl_status.config(text=f"Deck dimuat dari {filepath}")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def keluar(self):
        if messagebox.askyesno("Keluar", "Yakin ingin keluar?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()