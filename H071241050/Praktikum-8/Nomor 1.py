import re

def valid_string(a):
    pattern = r"^[A-Za-z02468]{40}[13579\s]{5}$"
    return bool (re.match(pattern,a))

a = input("Masukkan string: ")
print(valid_string(a))

# 2222222222aaaaaaaaaa2222222222aaaaaaaaaa77713 57
# 2222222222aaaaaaaaaa2222222222aaaaaaaaaaabc13 57
