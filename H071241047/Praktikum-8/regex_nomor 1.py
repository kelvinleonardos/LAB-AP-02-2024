import re

def validate_string(s):
    pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'
    return bool(re.match(pattern, s))


s = input("Masukkan string: ")


if validate_string(s):
    print("True")
else:
    print("False")
