print("## Program Konversi Suhu ##")
print("===========================")
print()

celcius = float(input("Masukkan Suhu Celcius : ", end='derajat'))

kelvin = int(celcius + 273.15)
reamur = int(celcius * (4/5))
fahrenheit = int((9/5 * celcius) + 32)

print(celcius, "derajat Celcius =", kelvin, "Kelvin")
print(celcius, "derajat Celcius =", reamur, "derajat Reamur")
print(celcius, "derajat Celcius =", fahrenheit, "derajat Fahrenheit")