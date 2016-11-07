# Level13

#### About

There is a security check that prevents the program from continuing execution if the user invoking it does not match a specific user id. 
To do this level, log in as the level13 account with the password level13. Files for this level can be found in /home/flag13. 


#### Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <string.h>

#define FAKEUID 1000

int main(int argc, char **argv, char **envp)
{
	int c;
	char token[256];

	if(getuid() != FAKEUID) {
		printf("Security failure detected. UID %d started us, we expect %d\n", getuid(), FAKEUID);
		printf("The system administrators will be notified of this violation\n");
		exit(EXIT_FAILURE);
	}

	// snip, sorry :)

	printf("your token is %s\n", token);
	
}
```

#### Solutions

* gdb flag13
```
(gdb) disassemble main
break *0x080484f4
run
print $eax
set $eax=1000
print $eax
continue
```

* su flag13 < b705702b-76a8-42b0-8844-3adabbe5ac58


#### Recommends

http://www.yolinux.com/TUTORIALS/GDB-Commands.html 
objdump 
