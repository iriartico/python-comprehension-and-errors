set_A = {'col', 'mex', 'bol'}
set_B = {'pe', 'bol'}

# Union
set_C = set_A.union(set_B)
print(set_C)
print(set_A | set_B)

# Intersection
set_C = set_A.intersection(set_B)
print(set_C)
print(set_A & set_B)

# Difference
set_C = set_A.difference(set_B)
print(set_C)
print(set_A - set_B)

# Symmetric Difference
set_C = set_A.symmetric_difference(set_B)
print(set_C)
print(set_A ^ set_B)