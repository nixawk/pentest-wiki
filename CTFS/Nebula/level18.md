# Level18

#### About

Analyse the C program, and look for vulnerabilities in the program. There is an easy way to solve this level, an intermediate way to solve it, and a more difficult/unreliable way to solve it.  

To do this level, log in as the level18 account with the password level18. Files for this level can be found in /home/flag18. 


#### Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <fcntl.h>
#include <getopt.h>

struct {
	FILE *debugfile;
	int verbose;
	int loggedin;
} globals;

#define dprintf(...) if(globals.debugfile) \
  fprintf(globals.debugfile, __VA_ARGS__)
#define dvprintf(num, ...) if(globals.debugfile && globals.verbose >= num) \
  fprintf(globals.debugfile, __VA_ARGS__)

#define PWFILE "/home/flag18/password"

void login(char *pw)
{
	FILE *fp;

	fp = fopen(PWFILE, "r");
	if(fp) {
		char file[64];

		if(fgets(file, sizeof(file) - 1, fp) == NULL) {
			dprintf("Unable to read password file %s\n", PWFILE);
			return;
		}
                fclose(fp);
		if(strcmp(pw, file) != 0) return;		
	}
	dprintf("logged in successfully (with%s password file)\n", 
		fp == NULL ? "out" : "");
	
	globals.loggedin = 1;

}

void notsupported(char *what)
{
	char *buffer = NULL;
	asprintf(&buffer, "--> [%s] is unsupported at this current time.\n", what);
	dprintf(what);
	free(buffer);
}

void setuser(char *user)
{
	char msg[128];

	sprintf(msg, "unable to set user to '%s' -- not supported.\n", user);
	printf("%s\n", msg);

}

int main(int argc, char **argv, char **envp)
{
	char c;

	while((c = getopt(argc, argv, "d:v")) != -1) {
		switch(c) {
			case 'd':
				globals.debugfile = fopen(optarg, "w+");
				if(globals.debugfile == NULL) err(1, "Unable to open %s", optarg);
				setvbuf(globals.debugfile, NULL, _IONBF, 0);
				break;
			case 'v':
				globals.verbose++;
				break;
		}
	}

	dprintf("Starting up. Verbose level = %d\n", globals.verbose);

	setresgid(getegid(), getegid(), getegid());
	setresuid(geteuid(), geteuid(), geteuid());
	
	while(1) {
		char line[256];
		char *p, *q;

		q = fgets(line, sizeof(line)-1, stdin);
		if(q == NULL) break;
		p = strchr(line, '\n'); if(p) *p = 0;
		p = strchr(line, '\r'); if(p) *p = 0;

		dvprintf(2, "got [%s] as input\n", line);

		if(strncmp(line, "login", 5) == 0) {
			dvprintf(3, "attempting to login\n");
			login(line + 6);
		} else if(strncmp(line, "logout", 6) == 0) {
			globals.loggedin = 0;
		} else if(strncmp(line, "shell", 5) == 0) {
			dvprintf(3, "attempting to start shell\n");
			if(globals.loggedin) {
				execve("/bin/sh", argv, envp);
				err(1, "unable to execve");
			}
			dprintf("Permission denied\n");
		} else if(strncmp(line, "logout", 4) == 0) {
			globals.loggedin = 0;
		} else if(strncmp(line, "closelog", 8) == 0) {
			if(globals.debugfile) fclose(globals.debugfile);
			globals.debugfile = NULL;
		} else if(strncmp(line, "site exec", 9) == 0) {
			notsupported(line + 10);
		} else if(strncmp(line, "setuser", 7) == 0) {
			setuser(line + 8);
		}
	}

	return 0;
}

```

