print("""
welcome
untuk mendaftar di kursus ini anda harus memenuhi beberapa kualifikasi
""")
usia = 21
umur = int(input("berapa usia mu? "))
kualifikasi = input("apakah anda lolos kualifikasi sebelumnya? (y/t) ")
if kualifikasi.upper() == "Y" and umur >= 21:
    print("Anda dapat mendaftar di kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")
