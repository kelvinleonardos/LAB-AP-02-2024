# Input suhu dalam skala Celcius dari pengguna
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Konversi ke skala lain
kelvin = celcius + 273.15
reamur = celcius * 4/5
fahrenheit = (celcius * 9/5) + 32

# Munculkan hasil konversi
print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
print(f"Suhu dalam Reamur: {reamur:.2f} °Re")
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")
