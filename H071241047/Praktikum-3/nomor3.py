N = int(input("Masukkan nilai N: "))
M = int(input("Masukkan nilai M: "))

for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            print(f"MOVE to ({i},{j})")
        else:
            print(f"MOVE to ({i},{M-j-1})")