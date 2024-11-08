#TP3_3_H071241020
def move_robot():
    N = int(input("Masukkan jumlah baris (N): "))
    M = int(input("Masukkan jumlah kolom (M): "))
    
    for i in range(N):
        if i % 2 == 0:
            # Baris genap: bergerak ke kanan
            for j in range(M):
                print(f"MOVE to ({i}, {j})")
        else:
            # Baris ganjil: bergerak ke kiri
            for j in range(M-1, -1, -1):
                print(f"MOVE to ({i}, {j})")
move_robot()
for i in range (5 ):
    print(i)

