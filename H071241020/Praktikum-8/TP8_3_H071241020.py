import re

#Username
def cek_usnm(a):
    if len(a) < 5:
        print("Username anda kurang dari 5 karakter.")
        return False
    elif len(a) > 20:
        print("Username yang anda masukkan melebihi 20 karakter.")
        return False

    rgxusnm = r'^[a-zA-Z0-9]+$'
    if re.match(rgxusnm, a):
        return True
    else:
        print("Username hanya boleh berisi huruf dan angka.")
        return False

#email
def cek_eml(b):
    rgx = r'^[a-z]+@[a-z]+\.[a-z]+(\.[a-z]+)?$'
    
    if re.match(rgx, b):
        return True
    else:
        print("Email yang anda masukkan tidak valid.")


#Password
def cek_pwd(c):
    if len(c) < 8:
        print("Password anda kurang dari 8 karakter.")
        return False

    rgxkcl = r'[a-z]'
    rgxkpl = r'[A-Z]'
    rgxang = r'[0-9]'

    if re.search(rgxkcl, c) and re.search(rgxkpl, c) and re.search(rgxang, c):
        return True
    else:
        print("Password harus mengandung huruf kecil, huruf besar, dan angka.")
        return False

#Fungsi masukkan input
def jf():
    username = input("Masukkan username: ")
    if not cek_usnm(username):
        return False

    email = input("Masukkan email: ")
    if not cek_eml(email):
        return False

    password = input("Masukkan password: ")
    if not cek_pwd(password):
        return False

    print(f"Registrasi berhasil. Selamat datanng {username}!")
    return True

#Jalankan fungsi
jf()

#CONTOH INPUT YANG BISA ANDA MASUKKAN UNTUK MENDETEKSI JALANNYA FUNGSI DENGAN BAIK
#USERNAME : kjaskhhjsjsdBABBA32
#EMAIL : bhssgyhhvs@yahoo.go.id
#PASSWORD : knsdjsdHBNN45

#INPUT YANG SALAH 
# KJSDFHJGJDFSGJKJJDFGDHJ
# BJHhahjshj@gmail.com
# knndsjjdjsjdjshdsh
