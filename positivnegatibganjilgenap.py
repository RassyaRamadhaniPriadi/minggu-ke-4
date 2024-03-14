bilangan = float(input("Masukkan bilangan: "))

# Mengetahui ganjil genap
if bilangan % 2 == 0:
    print("Bilangan genap")
else:
    print("Bilangan ganjil")

# Mengtahun ganjil genap atau nol
if bilangan > 0:
    print("Bilangan positif")
elif bilangan < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")
