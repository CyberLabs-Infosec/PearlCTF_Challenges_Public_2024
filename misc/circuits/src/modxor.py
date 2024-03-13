

import sys, os, re

KEY_LEN = 20

# Read two files as byte arrays
file1_b = bytearray(open(sys.argv[1], 'rb').read())
file2_b = bytearray(open(sys.argv[2], 'rb').read())
has_output = len(sys.argv) > 3
out_path = os.path.abspath(sys.argv[3]) if has_output else f"xor_{sys.argv[1]}_vs_{sys.argv[2]}.txt"
# out_hex_path = os.path.abspath(sys.argv[3].replace('.', '.hexcode.')) if has_output else  f"xor_{sys.argv[1]}_vs_{sys.argv[2]}.hexcode.txt"

# Set the length to be the smaller one
size = len(file1_b) if len(file1_b) > len(file2_b) else len(file2_b)
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
    if len(file1_b)>len(file2_b):
        xord_byte_array[i] = file1_b[i] ^ file2_b[i % len(file2_b)]
    else:
        xord_byte_array[i] = file1_b[i % len(file1_b)] ^ file2_b[i]
    

# Write the XORd bytes to the output file
with open(out_path, 'wb') as f: f.write(xord_byte_array)
xorkey = xord_byte_array[:KEY_LEN]
print("Key", xorkey, len(xorkey))
escaped_key = r"\x" + r"\x".join("{:02x}".format(int(c)) for c in xorkey)
# with open(out_hex_path, 'w') as f: f.write(escaped_key)
# print("[*] %s XOR %s\n[*] Saved to '%s'|'%s'" % (sys.argv[1], sys.argv[2], out_path, out_hex_path))