n = int(input("N = "))
m = int(input("M = "))

if n < 0:
    for i in range(n, 1): 
        if i % 2 == 0: 
            for j in range(m, 1) if m < 0 else range(1, m+1): 
                print(f"MOVE to ({i}),({j})")
        else:  
            for j in range(1, m+1) if m > 0 else range(m, 1, -1):  
                print(f"MOVE to ({i}),({j})")
else:
    for i in range(1, n+1): 
        if i % 2 == 0:
            for j in range(1, m+1) if m > 0 else range(m, 1, -1): 
                print(f"MOVE to ({i}),({j})")
        else:
            for j in range(m, 1) if m < 0 else range(1, m+1):  
                print(f"MOVE to ({i}),({j})")
