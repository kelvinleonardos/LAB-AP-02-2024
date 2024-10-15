while True:
    try:
        N = int(input("N = "))
        M = int(input("M = "))

        if N < 0 or M < 0:
            print("N dan M tidak boleh negatif. Masukkan angka positif.")
            continue  
        break  
    except ValueError:
        print("Input tidak valid! Masukkan angka.")


for i in range(0, N):
    if i % 2 == 1:
        for j in range(M-1, -1, -1):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(0, M):
            print(f"MOVE to ({i},{j})")