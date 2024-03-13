from pwn import *
import random

context.arch="amd64"

random.seed(0x693133769)
FLAG = b"pearl{s3lf_m0d1fy1ng_c0d3_by_x0r_4nd_jmp}"
RICK_ROLL=b"https://www.youtube.com/watch/dQw4w9WgXcQ"


decoder = """
lea rdx, [rip + {}]
mov rcx, {}
mov r8, 0x8ffc28c0c4a451f7
.loop:
    xor [rdx], r8
    add rdx, 8
    loop .loop
jmp .end + {}
.end:
"""
decoder_padding=0x169
tmp = asm(decoder.format(0, 0, decoder_padding))

segfault="""mov dword [0], {}"""

def encode(program):
	eprogram = b""
	for i in range(0, len(program), 8):
		eprogram += int.to_bytes(int.from_bytes(program[i:i + 8], "little") ^ 0x8ffc28c0c4a451f7, 8, "little")
	return eprogram

END_CHUNK =asm("""push 0xa736579
mov edx, 4
mov eax, SYS_write
mov edi, 1
mov rsi, rsp
syscall
mov eax, SYS_exit
xor edi, edi
syscall""")

testing=asm(decoder.format(len(tmp) - 7 + decoder_padding, len(END_CHUNK) // 8, decoder_padding)) + random.randbytes(decoder_padding) + encode(END_CHUNK)

# TODO: Add the below to start chunk
# mov eax, SYS_ptrace
# syscall
# test eax, eax
# jnz $+0x31337
# /* arg checking */
START_CHUNK="""pop rsi
cmp rsi, 2
jl $+0x31337
pop rsi
pop rsi"""

BASIC_CHUNK="""
movzx eax, byte ptr [rsi]
cmp al,{}
je $+10
mov byte ptr [0],{}
inc rsi"""

PTRACE="""
mov eax, SYS_ptrace
syscall
test eax, eax
jnz $+0x31337"""


payload=b""

END_CHUNK=END_CHUNK.rjust((len(END_CHUNK)+7)&(-8),b"\x90")
paylaod=random.randbytes(decoder_padding)+encode(END_CHUNK)+payload
prev=asm(BASIC_CHUNK.format(hex(RICK_ROLL[-1]),hex(FLAG[-1])))+asm(decoder.format(len(tmp) - 7 + decoder_padding, len(END_CHUNK) // 8, decoder_padding))

for i in range(39,-1,-1):
	prev=prev.rjust((len(prev)+7)&(-8),b"\x90")
	paylaod=random.randbytes(decoder_padding)+encode(prev)+paylaod
	prev=asm(BASIC_CHUNK.format(hex(RICK_ROLL[i]),hex(FLAG[i])))+asm(decoder.format(len(tmp) - 7 + decoder_padding, len(prev) // 8, decoder_padding))

prev=asm(START_CHUNK)+prev
prev=prev.rjust((len(prev)+7)&(-8),b"\x90")
FINAL=asm(PTRACE)+asm(decoder.format(len(tmp) - 7 + decoder_padding, len(prev) // 8, decoder_padding))+random.randbytes(decoder_padding)+encode(prev)+paylaod

ELF.from_bytes(FINAL).save("./help_me")


def rand_addr():
    return random.getrandbits(32) << 12

def align(x):
    if x % 0x1000 != 0:
        return x + (0x1000 - x % 0x1000)
    return x

FINAL=random.randbytes(0x191)+FINAL

entrypoint=rand_addr()
entrypad=0x191

segs=[(entrypoint,FINAL)]

elf = b""
elf += b"\x7fELF" # header
elf += bytes([1, 2]) # 32-bit big endian (unchecked)
elf += random.randbytes(10) # padding
elf += p16(2) # executable file
elf += p16(0x3e) # amd64
elf += random.randbytes(4) # padding
elf += p64(entrypoint + entrypad) # entrypoint
elf += p64(0x3a) # pheader offset
elf += random.randbytes(14) # padding
elf += p16(0x38) # pheader size
elf += p16(len(segs)) # pheader count

header_size = align(len(elf) + 0x38 * len(segs))

cur_offset = header_size
for (addr, seg) in segs:
    aligned_len = align(len(seg))
    elf += p32(1) # loadable segment
    elf += p32(random.getrandbits(32) | 7) # rwx segment
    elf += p64(cur_offset) # file offset
    elf += p64(addr) # vaddr
    elf += random.randbytes(8) # padding
    elf += p64(aligned_len) * 2 # file size and mem size
    elf += random.randbytes(8) # padding
    cur_offset += aligned_len
    
for (_, seg) in segs:
    if len(elf) % 0x1000 != 0:
        elf += random.randbytes(0x1000 - len(elf) % 0x1000)
    elf += seg

with open("help_me_evil", "wb") as f:
    f.write(elf)