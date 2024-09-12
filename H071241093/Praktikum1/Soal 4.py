#Input suhu dalam Celcius dari pengguna
suhu_dalam_celcius = float(input("Masukkan suhu dalam Celcius:"))

#Menghitung konversi ke skala - lain

suhu_kelvin = int (suhu_dalam_celcius + 273.15)   #Konversi-to-Kelvin
suhu_reamur = int ((4/5)* suhu_dalam_celcius)          #Konversi ke Reamur   
suhu_fahrenheit = int ((9/5)* suhu_dalam_celcius+32) #Konversi ke Fahrenheit

#Menampilkan hasil konversi
print(f"hasil konversi dari suhu: {suhu_kelvin:.2f}K")
print(f"Suhu dalam Reamur: {suhu_reamur:.2f}.°R")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit:.2f} °F")