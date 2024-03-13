from flag import FLAG
import random
from hashlib import md5
import pickle

"""
crackme - crack MD5 hash for length 12 (first 6 chars are known)
solveme - solve 15 equations with 4 variables each for next 10 chars
breakme - solve a chain of xored flag chars of length 11
"""

def solveme():
    FLAG_LEN = 10
    EQ_LEN = 4
    EQ_COUNT = 15

    to_target = FLAG[12: 12 + FLAG_LEN]
    index = [
        [6, 7, 8, 5], [6, 5, 5, 2], 
        [9, 3, 2, 5], [7, 0, 0, 3], 
        [1, 9, 5, 4], [2, 3, 1, 1], 
        [8, 7, 6, 5], [0, 8, 5, 3], 
        [5, 6, 8, 2], [5, 4, 5, 9], 
        [2, 9, 5, 0], [2, 5, 4, 9], 
        [8, 3, 7, 6], [6, 5, 0, 5], 
        [2, 5, 6, 4]
    ]

    ops = [
        ['+', '+', '-'], ['+', '+', '-'], 
        ['+', '+', '+'], ['+', '-', '+'], 
        ['-', '-', '+'], ['-', '+', '-'], 
        ['-', '-', '+'], ['+', '-', '-'], 
        ['+', '+', '+'], ['-', '-', '+'], 
        ['-', '+', '-'], ['-', '+', '-'], 
        ['+', '+', '-'], ['-', '-', '-'], 
        ['-', '-', '-']
    ]

    equations = list()

    """    
    index = list()
    ops = list()

    for _ in range(EQ_COUNT):
        start = [random.randint(0, FLAG_LEN - 1) for _ in range(EQ_LEN)]
        index.append(start)

        ops.append(
            [random.choice(["+", "-"]) for _ in range(EQ_LEN - 1)]
        )

    print(index)
    print(ops)
    print(to_target)
    """

    for i in range(len(index)):
        equation = f"flag[{index[i][0]}] "
        result = ord(to_target[index[i][0]])
        for j in range(1, len(index[i])):
            equation += f"{ops[i][j - 1]} flag[{index[i][j]}] "

            if ops[i][j - 1] == "+":
                result += ord(to_target[index[i][j]])
            elif ops[i][j - 1] == "-":
                result -= ord(to_target[index[i][j]])
            elif ops[i][j - 1] == "*":
                result *= ord(to_target[index[i][j]])

        equation += f"== {result}"
        print(equation + ", ")
        equations.append(equation)

    return equations

def crackme():
    return md5(FLAG[:12].encode()).hexdigest()

def gen_breakme():
    plier = 69
    target = FLAG[22: ]
    links = list()

    for i in range(len(target)):
        links.append(plier ^ ord(target[i]))
        plier = ord(target[i])

    return links

# print(gen_breakme())

def unlink(last):
    best = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]
    mod = list()
    plier = 69

    for i in range(len(last)):
        mod.append(plier ^ ord(last[i]))
        plier = ord(last[i])
    
    if mod == best:
        return True
    else:
        return False


unlink = pickle.dumps(unlink)
print(unlink)

