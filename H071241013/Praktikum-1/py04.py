print("konversi suhu dari celcius ke kelvin, reamur dan fahrenheit")
celcius = int(input("masukkan suhu dalam celcius:"))

k = int(celcius+273)
r = int(celcius*4/5)
f = int(celcius*9/5+32)

print(f"hasil konversi dari suhu {celcius} dejarat celcius ke kelvin adalah :{k}K")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke reamur adalah :{r}R")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke fahrenheit adalah :{f}F")