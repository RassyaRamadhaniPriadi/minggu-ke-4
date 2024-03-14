

# pilihan si pemain
pilihan = ["Batu", "Gunting", "Kertas"]

# Meminta input dari kedua pemain
pemain1 = input("Pemain 1, masukkan pilihan (Batu/Gunting/Kertas): ").capitalize()
pemain2 = input("Pemain 2, masukkan pilihan (Batu/Gunting/Kertas): ").capitalize()

# Memeriksa validitas input
if pemain1 not in pilihan or pemain2 not in pilihan:
    print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
else:
    print("Pemain 1 memilih:", pemain1)
    print("Pemain 2 memilih:", pemain2)

    # Menentukan pemenang
    if pemain1 == pemain2:
        print("Hasil: Seri!")
    elif (pemain1 == "Batu" and pemain2 == "Gunting") or \
         (pemain1 == "Gunting" and pemain2 == "Kertas") or \
         (pemain1 == "Kertas" and pemain2 == "Batu"):
        print("Pemain 1 menang!")
    else:
        print("Pemain 2 menang!")
