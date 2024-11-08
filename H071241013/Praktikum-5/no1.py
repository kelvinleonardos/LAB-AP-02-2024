def palindrom(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

string = input("Masukkan kata atau kalimat: ")
if palindrom(string):
    print(f"'{string}' adalah palindrom.")
else:
    print(f"'{string}' bukan palindrom.")
