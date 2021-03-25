# Coba perbaiki kode berikut untuk mencetak informasi yang benar dengan mengubah
# stringnnya (s).

s = list("Hey there! what should this string be?")
s = s[0:20]

# Panjangnya harusnya 20 = bener
print("panjang dari s = %d" % len(s))

# huruf pertama ‘a’ harusnya di index no 8 = bener
s[8] = "a"
print("Kemunculan pertama a = %d" % s.index("a"))

# jumlah huruf a harusnya 2 = bener
print("a muncul sebanyak %d kali" % s.count("a"))


# memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])  # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s[5:10])  # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12])  # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" % s[1::2])  # (0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:])  # 5th-from-last to end

# konversikan ke upercase
s = list("Hey there! what should this string be?")
s[0] = "S"
s[1] = "t"
s[2] = "r"
s[34] = "o"
s[35] = "m"
s[36] = "e"
s[37] = "!"
s = "".join(s)
print("String dalam huruf besar: %s" % s.upper())

# konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())

# cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'Str'. Good!")

# cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good!")

# Pisahkan string menjadi tiga string yang terpisah,

# masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))

