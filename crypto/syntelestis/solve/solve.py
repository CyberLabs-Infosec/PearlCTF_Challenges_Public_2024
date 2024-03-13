from sage.all import *
from itertools import product
from tqdm import tqdm

k, p = None, None
exec(open("../publish/output.txt").read())

F = GF(p)

M, V, C = list(), list(), list()

flag = b"706561726c7b" + b"?" * len(k) + b"#" * 8

# todo multithread this!
# preprocess
for data in k:
    target = data[-1]
    row = []
    crow = []
    for i in range(0, len(flag), 2):
        m, n = F(data[i]), F(data[i + 1])
        target -= 2 / (m ** 2 * n ** 2)
        cA = 1 / (m * n ** 3)
        cB = 1 / (n * m ** 3)
        if flag[i] == ord('?'):
            row.append(cA)
            row.append(cB)
        elif flag[i] == ord('#'):
            crow += [cA, cB]
        else:
            cA = (cA * flag[i]) / flag[i + 1]
            cB = (cB * flag[i + 1]) / flag[i]
            target -= (cA + cB)
    M.append(row)
    V.append(target)
    C.append(crow)

M = Matrix(F, M)
V = vector(F, V)
C = Matrix(F, C)
prod = product("0123456789", repeat = 6)

for p in tqdm(prod):
    brute = "".join(p).encode() + b"7d"
    brute = b"3174597d" # author's cheat

    D = list()
    for j in range(0, len(brute), 2):
        abinv = F(brute[j]) / F(brute[j + 1])
        ainvb = F(brute[j + 1]) / F(brute[j])
        D += [abinv, ainvb]
    D = vector(F, D)
    VV = V - C * D

    res = M.solve_right(VV)
    if res[0] * res[1] == 1:
        break

print(f"brute -> {brute}")
alphabet = b"0123456789abcdef"
flag = bytearray(b"706561726c7b")
for i in range(0, len(res), 2):
    for j in alphabet:
        cand = int(res[i] * j)
        if cand < 128 and cand in alphabet:
            flag.append(cand)
            flag.append(j)
            break
flag += brute
with open("flag.txt", "wb") as f:
    f.write(bytes.fromhex(flag.decode()))
