import time
import subprocess
import os
import random
import json

random.seed(time.time())

DIRECTORY = "binaries"
BINARY_NAME = "not-so-easy"
FLAG = "pearl{d1d_y0u_aut0m4t3_0r_4r3_y0u_h4rdw0rk1ng_?}"
NUMBER_OF_BINARIES = 200

FINAL_ARRAY = []

def scramble_flag():
    global FLAG
    flag = ['_' for i in range(NUMBER_OF_BINARIES)]

    number_of_plus = 0
    while number_of_plus < NUMBER_OF_BINARIES - len(FLAG):
        position = random.randint(1, NUMBER_OF_BINARIES-2)
        if flag[position] == '+':
            continue
        flag[position] = '+'
        number_of_plus += 1

    i = 0
    for f in FLAG:
        while flag[i] == '+':
            i += 1
        flag[i] = f
        i += 1
    
    FLAG = ''.join(flag)

def encode(random_number, xor_number, flag_char, array):
    temp = random_number
    a = -1
    for num in array:
        temp += (a * num)
        a *= -1
    
    temp = temp ^ xor_number
    final_number = temp - ord(flag_char)

    return final_number

def decode(random_number, xor_number, final_number, array):
    temp = random_number
    a = -1
    for num in array:
        temp += (a * num)
        a *= -1

    temp = temp ^ xor_number
    flag_char = temp - final_number

    return flag_char

def generate_binary(i):
    flag_char = FLAG[i]
    array_length = random.randint(5, 20)
    array = []
    for j in range(array_length):
        array.append(random.randint(100, 500))

    random_number = random.randint(2000, 10000)
    xor_number = random.randint(1000, 2000)

    final_number = encode(random_number, xor_number, flag_char, array)
    flag_ascii = decode(random_number, xor_number, final_number, array)

    element = [
        array,
        random_number,
        xor_number,
        final_number,
        flag_ascii
    ]
    FINAL_ARRAY.append(element)

    if(ord(flag_char) != flag_ascii):
        print("ERROR OCCURRED!")
        exit(0)

    code = f"""#include<stdio.h>

int arr[{array_length}] = {{{", ".join([str(x) for x in array])}}};

void f(int *x)
{{
    *x = 0;
}}

void scramble()
{{
    int var = {random_number};
    f(&var);
    int a = -1;
    for(int i=0; i<{array_length}; i++){{
        var += (a * arr[i]);
        a *= -1;
        f(&var);
    }}
    var ^= {xor_number};
    f(&var);
    var -= {final_number};
}}

int main()
{{  
    scramble();

    return 0;
}}"""

    with open(f"{BINARY_NAME}.c", "w") as f:
        f.write(code)
    
    p = subprocess.Popen(["gcc", f"{BINARY_NAME}.c", "-O0", "-o", f"{DIRECTORY}/{BINARY_NAME}-{i}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        print("STDOUT:")
        print(stdout)
    if stderr:
        print("STDERR:")
        print(stderr)

def delete_generated():
    for file in os.listdir(DIRECTORY):
        if "not-so-easy" in file:
            os.remove(f"{DIRECTORY}/{file}")

def generate_binaries():
    for i in range(NUMBER_OF_BINARIES):
        print("\r" + f"Generating Binary {i}", end="", flush=False)
        generate_binary(i)
        if not os.path.exists(f"{DIRECTORY}/{BINARY_NAME}-{i}"):
            print("\nERROR")
            break
    
    with open("final_array.json", "w") as f:
        json.dump(FINAL_ARRAY, f, indent=4)

scramble_flag()
delete_generated()
generate_binaries()