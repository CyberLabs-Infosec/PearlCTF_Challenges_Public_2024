from sage.all import *

def mpcDecoder(r, A, D, s = 1):
    B = A.inverse()
    c = [0] * 4
    for i in range(s, 4):
        w = zero_vector(F, v)
        w[i] = 1
        c[i] = D[i].decode_to_code(r * B * w)
    r = r.columns()
    for i in range(1, 4):
        for j in range(4):
            r[j] -= A[i, j] * c[i]

    for i in range(4):
        try:
            c[0] = D[0].decode_to_code(r[i] / A[0, i])
        except Exception:
            continue
        return c


config = [
    (100, 85, 16),
    (100, 21, 80),
    (100, 19, 82),
    (100, 25, 76)
]

p, N, v, t = 23 ** 2, 100, 4, 31
F = GF(p)
F.inject_variables()
M = MatrixSpace(F, v, v)

exec(open("../publish/output.txt").read())

A = matrix(F, A)
r = matrix(F, r)
E = [codes.GeneralizedReedSolomonCode(F.list()[:n], k) for n, k, _ in config]
D = [c.decoder("BerlekampWelch") for c in E]

try:
    mpcDecoder(r, A, D, s = 0)
except:
    print("Naive Solution Failed")

MSG = list()
for i, c in enumerate(mpcDecoder(r, A, D)):
    MSG += E[i].decode_to_message(c)

FLAG = bytearray()
for i in MSG:
    for j in b'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if j % 23 == i:
            FLAG.append(j)
            break
with open("decoded.txt", "wb") as f:
    f.write(FLAG)
