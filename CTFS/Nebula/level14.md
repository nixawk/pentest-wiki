# Level14

#### About

This program resides in /home/flag14/flag14. It encrypts input and writes it to standard output. An encrypted token file is also in that home directory, decrypt it :) 
To do this level, log in as the level14 account with the password level14. Files for this level can be found in /home/flag14. 


#### Source code

There is no source code available for this level

#### Solutions
```
11111111111111111111111111111111111111111111111 
123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^` 


Output: 8457c118-887c-4e40-a5a6-33a25353165
su flag14 < 8457c118-887c-4e40-a5a6-33a25353165
/bin/getflag
```

#### Exploits

```
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def main():
    with open('/home/flag14/token', 'r') as f:
        keys = []
        data = f.read().strip()
        for i, j in enumerate(data):
            key = chr(ord(j) - i)
            keys.append(key)

    pwd = "".join(keys)
    return pwd


if __name__ == "__main__":
    main()
```

#### Recommends

How to run command as a different user ? 

http://www.cyberciti.biz/open-source/command-line-hacks/linux-run-command-as-different-user/ 
http://stackoverflow.com/questions/233217/pass-password-to-su-sudo-ssh 
http://www.experts-exchange.com/Programming/Languages/Scripting/Python/Q_23048208.html 
