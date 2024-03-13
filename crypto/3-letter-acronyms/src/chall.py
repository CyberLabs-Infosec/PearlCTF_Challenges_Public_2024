from sage.all import *
from secret import MSG

assert len(MSG) == 150
assert MSG.isalpha

config = [
    (100, 85, 16),
    (100, 21, 80),
    (100, 19, 82),
    (100, 25, 76)
]

p, N, v, t = 23 ** 2, 100, 4, 41
F = GF(p)
M = MatrixSpace(F, v, v)

codeWords = list()
for n, k, _ in config:
    grsCode = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
    msg, MSG = vector(F, list(MSG[:k].encode())), MSG[k:]
    codeWords.append(grsCode.encode(msg))

while True:
    A = M.random_element()
    A[1,0] = A[2,0] = A[3,0] = A[2,1] = A[3,1] = A[3,2] = 0
    if not A.is_singular():
        break

r = column_matrix(codeWords) * A
rr = copy(r)
cnt = [0] * 4
for _ in range(t):
    i = randint(0, n - 1)
    j = randint(0, v - 1)
    if j < 2:
        j = 0
    else:
        j = randint(1, v - 1)
    cnt[j] += 1
    r[i, j] += F.random_element()

cnt = [0] * 4
for i in range(v):
    for j in range(n):
        if rr[j, i] != r[j, i]:
                cnt[i] += 1

with open("final.txt", "w") as f:
    f.write(f"r = {list(r)}\n")
    f.write(f"A = {list(A)}")
