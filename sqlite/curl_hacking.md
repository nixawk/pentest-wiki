#CURL#

----

##GENERAL##

```
curl http://curl.haxx.se
curl http://site.{one,two,three}.com  
curl ftp://ftp.numericals.com/file[1-100].txt  
curl ftp://ftp.numericals.com/file[001-100].txt  
curl ftp://ftp.letters.com/file[a-z].txt  

curl http://any.org/archive[1996-1999]/vol[1-4]/part{a,b,c}.html  

curl http://www.numericals.com/file[1-100:10].txt  
curl http://www.letters.com/file[a-z:2].txt  

curl -o index.html http://curl.haxx.se/  
curl http://curl.haxx.se/ > index.html  

curl -# http://curl.haxx.se/ > index.html  
  
curl -0 http://curl.haxx.se/  
curl --http1.1 http://curl.haxx.se/  
curl --http2 http://curl.haxx.se/  

curl -1 http://curl.haxx.se/  
curl --tlsv1 http://curl.haxx.se/

curl -2 http://curl.haxx.se/  
curl --sslv2 http://curl.haxx.se/

curl -3 http://curl.haxx.se/  
curl --sslv3 http://curl.haxx.se/

curl -4 http://curl.haxx.se/  
curl --ipv4 http://curl.haxx.se/

curl -6 http://curl.haxx.se/  
curl --ipv6 http://curl.haxx.se/

curl -A "wget/1.0" http://curl.haxx.se/  
curl --user-agent "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)" [URL]
curl --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" [URL]

curl -b "phpsession=Testtest" http://demo.com/    
curl --cookie "name=Daniel" http://curl.haxx.se

curl -c cookies.txt http://curl.haxx.se/  
curl --cookie-jar cookies.txt http://curl.haxx.se

curl -d "username=admin&password=pass" http://curl.haxx.se/  
curl --data "birthyear=1905&press=%20OK%20"  http://curl.haxx.se/when.cgi
curl --data-urlencode "name=I am Daniel" http://curl.haxx.se
curl --data "<xml>" --header "Content-Type: text/xml" --request PROPFIND url.com

curl -e "http://referer" http://demo.com/  
curl --referer http://curl.haxx.see http://curl.haxx.se

curl --header "Host:" http://curl.haxx.se
curl --header "Destination: http://nowhere" http://curl.haxx.se

curl -D - http://curl.haxx.se/  
curl --dump-header headers_and_cookies http://curl.haxx.se

curl -L http://github.com/  
curl --location http://curl.haxx.se

curl --dns-servers 8.8.8.8 http://demo.com/  

curl --trace-ascii debugdump.txt http://curl.haxx.se/
curl --form upload=@localfilename --form press=OK [URL]
curl --upload-file uploadfile http://curl.haxx.se/receive.cgi
curl --user name:password http://curl.haxx.se
curl --proxy-user proxyuser:proxypassword curl.haxx.se

curl --cert mycert.pem https://secure.example.com
```

----

#REFERENCES#

$ man curl  
http://curl.haxx.se/docs/manual.html  
http://curl.haxx.se/docs/httpscripting.html  
http://httpkit.com/resources/HTTP-from-the-Command-Line/  
