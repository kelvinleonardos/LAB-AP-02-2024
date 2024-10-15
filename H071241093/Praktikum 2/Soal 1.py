x = int(input( "masukkan panjang sisi pertama :"))
y = int(input( "masukkan panjang sisi kedua :"))
z = int(input( "masukkan panjang sisi terakhir :"))

#syarat pembentukan segitiga
if x+y >z and x + z > y and  y + z > x:

  if x==y==z :
    segitiga = 'segitiga sama sisi'
  elif x==z or x==y or y==z :
    segitiga = 'segitiga sama kaki'
  else :
    segitiga = 'segitiga sembarang'
else: 
  segitiga = "segitiga tidak valid"
print(segitiga)



