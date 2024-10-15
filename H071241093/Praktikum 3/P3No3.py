try:
    n = int(input("N = "))
    m = int(input("M = "))

    for x in range(abs(n)):
        if x % 2 == 0:
            # Bergerak ke kanan
            for y in range(abs(m)):
                print(f"MOVE to ({x if n >= 0 else -x}, {y if m >= 0 else -y})")
        else:
            # Bergerak ke kiri
            for y in range(m-1, -1, -1):
                print(f"MOVE to ({x if n >= 0 else -x}, {y if m >= 0 else -y})")
except:
    print("Masukkan sebuah angka!")     
        
