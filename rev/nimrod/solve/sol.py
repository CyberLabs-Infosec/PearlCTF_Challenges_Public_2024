import os
import z3

directory = os.getenv("HOME")


def scanFolder(path: str):
    final = []

    files = os.listdir(path)

    for file in files:
        if file.startswith("."):
            continue
        if os.path.isdir(os.path.join(path, file)):
            final.extend(scanFolder(os.path.join(path, file)))
        elif os.path.isfile(os.path.join(path, file)):
            final.append(os.path.join(path, file))

    return final


def cleanFileNames(paths: list):
    for path in paths:
        baseDir, ext = os.path.splitext(path)
        name = baseDir.split("/")[-1]
        modifiedPath = os.path.join(
            baseDir[:len(baseDir) - len(name)], name[16:] + ext)

        data = open(path, "rb").read()
        open(modifiedPath, "wb").write(data)

        os.remove(path)


def sym_xoroshiro128plus(solver, sym_s0, sym_s1, mask, result):
    s0 = sym_s0
    s1 = sym_s1
    sym_r = (sym_s0 + sym_s1)

    condition = z3.Bool('c0x%0.16x' % result)
    solver.add(z3.Implies(condition, (sym_r & mask) == result & mask))

    s1 ^= s0
    sym_s0 = z3.RotateLeft(s0, 55) ^ s1 ^ (s1 << 14)
    sym_s1 = z3.RotateLeft(s1, 36)

    return sym_s0, sym_s1, condition


def find_seed(results_with_masks):
    start_s0, start_s1 = z3.BitVecs('start_s0 start_s1', 64)
    sym_s0 = start_s0
    sym_s1 = start_s1
    solver = z3.Solver()
    conditions = []

    for result, mask in results_with_masks:
        sym_s0, sym_s1, condition = sym_xoroshiro128plus(
            solver, sym_s0, sym_s1, mask, result)
        conditions.append(condition)

    if solver.check(conditions) == z3.sat:
        model = solver.model()

        return [model[start_s0].as_long(), model[start_s1].as_long()]

    else:
        return None


class Xoroshiro128Plus(object):
    def __init__(self, seed):
        self.seed = seed

    @staticmethod
    def rotl(x, k):
        return ((x << k) & 0xffffffffffffffff) | (x >> 64 - k)

    def next(self):
        s0 = self.seed[0]
        s1 = self.seed[1]
        result = (s0 + s1) & 0xffffffffffffffff

        s1 ^= s0
        self.seed[0] = self.rotl(s0, 55) ^ s1 ^ (
            (s1 << 14) & 0xffffffffffffffff)
        self.seed[1] = self.rotl(s1, 36)

        return result


def generateKey(size: int, generator: Xoroshiro128Plus) -> list:
    result = []
    for _ in range(size):
        result.append(generator.next() % 256)

    return result


def decryptFiles(paths: list, generator: Xoroshiro128Plus):
    for path in paths:
        with open(path, "rb") as file:
            data = open(path, "rb").read()
            file.close()

        key = generateKey(len(data), generator)

        for _ in range(2):
            hex(generator.next())[2:].upper().rjust(16, "0")

        final = b""
        for index, char in enumerate(data):
            final += chr(char ^ key[index]).encode()

        open(path, "wb").write(final)


if __name__ == "__main__":
    uint1 = 0x8645E4A10D834AF7
    uint2 = 0x6648E73D2FE0FFEE

    seed = find_seed([(uint1, 0xffffffffffffffff),
                     (uint2, 0xffffffffffffffff)])
    if seed is None:
        print("could not find seed from the given integers :(")
        exit()
    generator = Xoroshiro128Plus(seed)
    for _ in range(2):
        hex(generator.next())[2:].upper().rjust(16, "0")

    initial_paths = scanFolder(directory)
    cleanFileNames(initial_paths)

    paths = scanFolder(directory)
    decryptFiles(paths[1:], generator)
