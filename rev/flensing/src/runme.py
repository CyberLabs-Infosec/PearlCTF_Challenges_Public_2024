#!/usr/local/bin/python3

import os
import time
import random
from Crypto.Util.strxor import strxor 

FLAG = os.getenv("FLAG")

def setConditions(value: int) -> bytes:
    random.seed(value)
    return random.randbytes(len(FLAG))

def writeToLog(name: str, content: str):
    with open(name, "w") as f:
        f.write(content)
        f.close()

def showAmbergris():
    current = int(time.time())
    initial = setConditions(current)
    processed = strxor(initial, FLAG.encode())

    writeToLog("/var/log/status", processed.hex())
    writeToLog("/root/secret", hex(current)[2:])


if __name__ == "__main__":
    message = """
    Ambergris is a solid, waxy, flammable substance of a dull grey or blackish colour produced in the digestive system of sperm whales. Freshly produced ambergris has a marine, fecal odor. It acquires a sweet, earthy scent as it ages, commonly likened to the fragrance of isopropyl alcohol without the vaporous chemical astringency.

    Ambergris has been highly valued by perfume makers as a fixative that allows the scent to last much longer, although it has been mostly replaced by synthetic ambroxide.
    """

    print(message)
    showAmbergris()
