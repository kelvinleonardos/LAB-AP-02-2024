import re

def is_valid_username(username):
    pattern = r'^[A-Za-z0-9]{5,20}$'
    return bool(re.match(pattern, username))

def is_valid_email(email):
    pattern = r'^[a-z0-9]+@[a-z]+\.(com|co\.id)$'
    return bool(re.match(pattern, email))

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8}$'
    return bool(re.match(pattern, password))

username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")
    
    if is_valid_email(email):
        password = input("Masukkan password: ")
        
        if is_valid_password(password):
            print(f"Registrasi berhasil! Halo {username}")
        else:
            print("Password yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("Email yang kamu input tidak valid. Registrasi gagal!")
else:
    print("Inputan username tidak valid dalam sistem. Registrasi gagal!")