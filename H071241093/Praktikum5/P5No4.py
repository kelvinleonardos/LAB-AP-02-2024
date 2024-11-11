def semua_substring(x):
    substr = []
    
    for panjang in range(1, len(x) + 1):
        for i in range(len(x) - panjang + 1):
            substr.append(x[i:i + panjang])
    return substr

input_str = input("Masukkan sebuah string : ")

hasil = semua_substring(input_str)

for substring in hasil:
    print(substring)


