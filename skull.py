#!/usr/bin/python
import os, sys

argc = len(sys.argv)
if argc < 2 or argc > 3:
	print("usage: skull pwnable_path [libc_path]")
	sys.exit()
elif argc == 2:
	libc_name = ""
	elf_name = sys.argv[1]
elif argc == 3:
	libc_name = sys.argv[2]
        elf_name = sys.argv[1]


skeleton = '''from pwn import *
import sys

elf_name = "''' + elf_name + '''"
libc_name = "''' + libc_name + '''"
#libc = ELF(libc_name)

if len(sys.argv) > 1:
	r = remote(sys.argv[1], int(sys.argv[2]))
else:
	r = process(elf_name, env={"LD_PRELOAD": libc_name})

io = lambda : r.interactive()
sla = lambda x, y : r.sendlineafter(x, y)
sa = lambda x, y : r.sendafter(x, y)
rl = lambda : r.recvline()
ru = lambda x : r.recvuntil(x)
###---------- XXX ----------###





###---------- XXX ----------###
io()
'''

if not os.path.isfile("./sploit.py"): 
	open("./sploit.py", "wb").write(skeleton)
else:
	print("Err: sploit.py file already exists!")
