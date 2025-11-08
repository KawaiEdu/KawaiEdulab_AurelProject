kelas = {
    "kelas A": ["amanda","kenny"],
    "kelas B": ["kael","seraphine"]
}

for nama_kelas, siswa in kelas.items():
    print(nama_kelas + ":")
    for s in siswa:
        print("-" + s)
    print()
