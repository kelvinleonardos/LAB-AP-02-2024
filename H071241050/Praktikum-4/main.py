def penjumlahan(x, y):
    return x+y

try:
    x = int(input())
    y = int(input())
except:
    exit()
z = penjumlahan(x, y)

print(z)