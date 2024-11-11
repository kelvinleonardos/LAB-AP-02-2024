def palindrom (x):
    if x == x[::-1]:
        print("Palindrom")
    else:
        print("Bukan Palindrom")
palindrom(str(input("Masukkan Kata: ")))