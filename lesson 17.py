file= open("data.txt", "w")
file.write("hallo ini first text saya!\n")
file.close()

file= open("data.txt", "r")
print(file.read())
file.close()

file= open("data.txt", "a")
file.write("tambahkan baris kedua.\n")
file.close()