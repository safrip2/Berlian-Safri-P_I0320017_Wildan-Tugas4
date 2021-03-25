#minta user input 2 bilangan bulat
#output = berapa banyak angka kedua dapat dikalikan sampai mendekati angka pertama
bilangan = input("masukkan dua angka dipisahkan dengan spasi> ")
pecah = bilangan.split(" ")
if pecah[0] >= pecah[1]:
    print(f"angka kedua dapat dikali dengan {int(pecah[0]) // int(pecah[1])} untuk mendekati angka pertama")
elif pecah[0] <= pecah[1]:
    print(f"angka pertama dapat dikali dengan {int(pecah[1]) // int(pecah[0])} untuk mendekati angka kedua")
else:
    print(" ")
