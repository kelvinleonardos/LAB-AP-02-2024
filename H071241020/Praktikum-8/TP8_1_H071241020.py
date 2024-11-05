import re

def cek_string(S):
    # Memastikan panjang string tepat 45 karakter
    if len(S) != 45:
        print("Masukkan 45 karakter.")

    regex_40_karakter_pertama = r'^[a-zA-Z02468]{40}'
    
    regex_5_karakter_terakhir = r'[13579 ]{5}$'

    if re.match(regex_40_karakter_pertama, S[:40]) and re.match(regex_5_karakter_terakhir, S[-5:]):
        return True
    else:
        return False

S = input("Masukkan string : ")

if cek_string(S):
    print("True")
else:
    print("False")

#Inputan yang bisa anda masukkan untuk mencoba apakah program benar dapat mengecek sesuai pada persyaratan :
#aaaaaaaaaa2222222222aaaaaaaaaa444444444413579
#AAAADDDFGH4426864242HJJGsdfvcd884424686811313