#Input panjang masing masing sisi
ps1 = int(input("Masukkan panjang sisi pertama : "))
ps2 = int(input("Masukkan panjang sisi kedua : "))
ps3 = int(input("Masukkan panjang sisi ketiga : "))

#Kondisi jenis segitiga
if ps1 == ps2 == ps3 : 
    print(f"Berdasarkan panjang sisi sisinya, segitiga tersebut adalah segitiga sama sisi.")
elif ps1 == ps2 != ps3 :
    print(f"Berdasarkan panjang sisi sisinya, segitiga tersebut adalah segitiga sama kaki.")
elif ps1 != ps2 == ps3 :
    print(f"Berdasarkan panjang sisi sisinya, segitiga tersebut adalah segitiga sama kaki.")
elif ps1 == ps3 != ps2 : 
    print(f"Berdasarkan panjang sisi sisinya, segitiga tersebut adalah segitiga sama kaki")
else :
    print(f"Tidak dapat membentuk segitiga yang valid.")
