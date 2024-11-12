from collections import Counter

def anagram(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    
    hapus_karakter = 0
    
    karakter = set(counter1.keys()).union(set(counter2.keys())) #.values
    
    for i in karakter:
        hapus_karakter += abs(counter1[i] - counter2[i])
    return hapus_karakter

s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

hasil = anagram(s1, s2)
print("Jumlah penghapusan untuk membuat anagram :", hasil)

print(Counter(s1).values())