## Twistd

How to start a ftp server with **Twisted**.

```
root@lab:/tmp# twistd -n ftp --help
Usage: twistd [options] ftp [options].
    WARNING: This FTP server is probably INSECURE do not use it.
Options:
  -p, --port=            set the port number [default: 2121]
  -r, --root=            define the root of the ftp-site. [default:
                         /usr/local/ftp]
      --userAnonymous=   Name of the anonymous user. [default: anonymous]
      --help             Display this help and exit.
      --help-auth-type=  Show help for a particular authentication type.
      --auth=            Specify an authentication method for the server.
      --password-file=   Specify a file containing username:password login info
                         for         authenticated connections. (DEPRECATED; see
                         --help-auth instead)
      --version          Display Twisted version and exit.
      --help-auth        Show all authentication methods available.

```

```
sroot@lab:/tmp# tudo easy_install twisted
root@lab:/tmp# twistd -n ftp -p 2121 --userAnonymous=anonymous 
2016-03-06 11:24:24-0500 [-] Log opened.
2016-03-06 11:24:24-0500 [-] twistd 15.5.0 (/usr/bin/python 2.7.11) starting up.
2016-03-06 11:24:24-0500 [-] reactor class: twisted.internet.epollreactor.EPollReactor.
2016-03-06 11:24:24-0500 [-] FTPFactory starting on 2121
2016-03-06 11:24:24-0500 [-] Starting factory <twisted.protocols.ftp.FTPFactory instance at 0xb6c2474c>
```

