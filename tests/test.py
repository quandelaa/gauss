import gauss

A = [[1, 2, 3],
     [1, 4, 5],
     [2, 1, 13]]

U = gauss.ref(A)
R = gauss.rref(A)

rank = gauss.rank(A)
inv = gauss.inverse(A)

print(U)
print(R)

print(rank)
print(inv)
