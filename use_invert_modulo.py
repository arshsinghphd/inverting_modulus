from invert_modulo import find_mod_inverse

A = 15
B = 26

# response is a tuple
inv, works = find_mod_inverse(A, B, True)

# print mod inverse
print(inv)

# print the works
for line in works:
    print(line)
