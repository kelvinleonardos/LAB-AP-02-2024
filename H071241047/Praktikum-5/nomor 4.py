def turunan(kata):
    for i in range(len(kata)):
        for j in range(i + 1, len(kata) + 1):
            print(kata[i:j])
        break
    return kata
n = input("Masukkan sebuah kata: ")
print(turunan(n))
