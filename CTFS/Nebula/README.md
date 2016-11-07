# exploit-exercises Nebula walkthrough

#### Site:  
https://exploit-exercises.com/nebula  
http://vulnhub.com/entry/exploit-exercises-nebula-v5,31/  


#### About

Nebula takes the participant through a variety of common (and less than common) weaknesses and vulnerabilities in Linux. It takes a look at  
  
    SUID files  
    Permissions  
    Race conditions 
    Shell meta-variables 
    $PATH weaknesses  
    Scripting language weaknesses 
    Binary compilation failures  

At the end of Nebula, the user will have a reasonably thorough understanding of local attacks against Linux systems, and a cursory look at some of the remote attacks that are possible. 


#### Getting started 

##### Levels 

Have a look at the levels available on the side bar, and log into the virtual machine as the username “levelXX” with a password of “levelXX” (without quotes), where XX is the level number. 

Some levels can be done purely remotely. 


##### Getting root: 

In case you need root access to change stuff (such as key mappings, etc), you can do the following:  

Log in as the "nebula" user account with the password "nebula" (both without quotes), followed by "sudo -s" with the password "nebula". You'll then have root privileges in order to change whatever needs to be changed. 

```
level19@nebula:~$ su nebula 
Password:  
nebula@nebula:/home/level19$ id 
uid=1000(nebula) gid=1000(nebula) groups=1000(nebula),4(adm),20(dialout),24(cdrom),46(plugdev),108(lpadmin),109(sambashare),110(admin) 
nebula@nebula:/home/level19$ sudo -s /bin/bash 
[sudo] password for nebula:  
root@nebula:/home/level19# id 
uid=0(root) gid=0(root) groups=0(root) 
```

#### Workthrough 

* Contents: 
* level00  ---- find a Set User ID program  
* level01  ---- env hijacking  
* level02  ---- command injection (c) 
* level03  ---- scheduler 
* level04  ---- bypass filename limit with a symbolic 
* level05  ---- get ssh perms from backup files 
* level06  ---- crack Unix/linux os user password 
* level07  ---- command injection (perl) 
* level08  ---- packet analysis (tcpdump) 
* level09  ---- code injection (php) 
* level10  ---- time-of-use to time-of-check or TOCTOU bug 
* level11  ---- command injection (c) 
* level12  ---- command injection (lua) 
* level13  ---- prog debug (c) 
* level14  ---- decrypt 
* level15  ---- compile a shared library in linux 
* level16  ---- command injection (perl) 
* level17  ---- pickle bug 
* level18  ---- bypass login auth (c) 
* level19  ---- process security 

Linux os/shell/command/security  
level00/level01/level03/level04/level05/level06/level08/level10  

c/perl/lua/php/python  
level02/level07/level09/level11/level12/level13/level14/level15/level16/level17/level18/level19 
