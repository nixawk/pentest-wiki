
## How to setup a ftp server quickly

Pleaes install [**pyftpdlib**](https://github.com/giampaolo/pyftpdlib) with pip or easy_install.

```
sudo easy_install pysendfile
sudo easy_install pyftpdlib
```

or

```
sudo pip2 install pysendfile
sudo pip2 install pyftpdlib
```

If you have installed **pyftpdlib** successfully, please start it as follow:

```
root@lab:/tmp/pyftpdlib# python -m pyftpdlib -w -p 21
pyftpdlib/authorizers.py:240: RuntimeWarning: write permissions assigned to anonymous user.
  RuntimeWarning)
  [I 2016-03-06 10:00:11] >>> starting FTP server on 0.0.0.0:21, pid=2090 <<<
  [I 2016-03-06 10:00:11] concurrency model: async
  [I 2016-03-06 10:00:11] masquerade (NAT) address: None
  [I 2016-03-06 10:00:11] passive ports: None
  [I 2016-03-06 10:00:40] 192.168.1.103:52874-[] FTP session opened (connect)
  [I 2016-03-06 10:00:40] 192.168.1.103:52874-[anonymous] USER 'anonymous' logged in.
  [I 2016-03-06 10:00:45] 192.168.1.103:52874-[anonymous] FTP session closed (disconnect).
  [I 2016-03-06 10:01:42] 192.168.1.101:49312-[] FTP session opened (connect)
  [I 2016-03-06 10:02:12] 192.168.1.101:49312-[] FTP session closed (disconnect).
  [I 2016-03-06 10:02:24] 192.168.1.101:49313-[] FTP session opened (connect)
  [I 2016-03-06 10:02:31] 192.168.1.101:49313-[anonymous] USER 'anonymous' logged in.
  [I 2016-03-06 10:06:28] 192.168.1.101:49313-[anonymous] RETR /tmp/pyftpdlib/setup.py completed=1 bytes=5183 seconds=0.004
  [I 2016-03-06 10:07:29] 192.168.1.101:49313-[anonymous] FTP session closed (disconnect).
  [I 2016-03-06 10:08:11] 192.168.1.104:1033-[] FTP session opened (connect)
  [I 2016-03-06 10:08:17] 192.168.1.104:1033-[anonymous] USER 'anonymous' logged in.
  [I 2016-03-06 10:10:43] 192.168.1.104:1033-[anonymous] FTP session closed (disconnect).

```

Windows FTP console client:

```
C:\Documents and Settings\test\Desktop>ver

Microsoft Windows XP [Version 5.1.2600]

C:\Documents and Settings\test\Desktop>ftp 192.168.1.103
Connected to 192.168.1.103.
220 pyftpdlib 1.5.0 ready.
User (192.168.1.103:(none)): anonymous
331 Username ok, send password.
Password:
230 Login successful.
ftp> ls
200 Active data connection established.
125 Data connection already open. Transfer starting.
.ci
.coveragerc
.git
...
...
```

You can also use other clients, ex: ncftp.
