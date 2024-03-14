# Mengonversi suhu 
konversi = input("Konversi dari Celsius ke Fahrenheit (C) atau dari Fahrenheit ke Celsius (F)? ").upper()

# Memeriksa validitas input
if konversi != 'C' and konversi != 'F':
    print("Input tidak valid. Silakan masukkan 'C' untuk konversi dari Celsius ke Fahrenheit atau 'F' untuk konversi dari Fahrenheit ke Celsius.")
else:
    suhu = float(input("Masukkan suhu: "))

    if konversi == 'C':
        hasil = (suhu * 9/5) + 32
        print("Suhu dalam Fahrenheit:", hasil)
    else:
        hasil = (suhu - 32) * 5/9
        print("Suhu dalam Celsius:", hasil)
