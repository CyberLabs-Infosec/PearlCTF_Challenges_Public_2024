PROG = god-of-war
CFLAGS = -g -no-pie -fno-stack-protector
LIBS= -lseccomp
all:
	gcc $(CFLAGS) $(PROG).c -o $(PROG) $(LIBS)

clean:
	rm -f $(PROG)
