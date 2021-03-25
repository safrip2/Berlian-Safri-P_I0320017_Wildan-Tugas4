#periksa berat bagasi
#berat maksimum = 50lbs (22,67kg)
#output = penumpang boleh masuk? =  True / False

#"jadi pertama di oknversi dulu ke lbs, terus di compare, jika lebih = false"

weightkg = float(input("weight(kg): "))
weightlbs = weightkg * 2.2 <= 50
if weightlbs == True:
    print(f"{weightlbs}, silakan masuk")
else:
    print(f"{weightlbs}, kurangi beban terlebih dahulu")
