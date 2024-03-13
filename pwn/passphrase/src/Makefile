PROG = passphrase
CFLAGS = -g -pie -fstack-protector-all
LIBS= -lseccomp
all:
	gcc $(CFLAGS) $(PROG).c -o $(PROG) $(LIBS)

clean:
	rm -f $(PROG)
