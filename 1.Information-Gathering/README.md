**Authors**: < [nixawk](https://github.com/nixawk) >, < [sjas](https://github.com/sjas) >

----

# Information Gathering

In the *information gathering* phase, you will gather any information you can about the organization you are attacking by using social-media networks, Google hacking, footprinting the target, and so on. One of the most important skills a penetration tester can have is the ability to learn about a target, including how it behaves, how it operates, and how it ultimately can be attacked. The information that you gather about your target will give you valuable insight into the types of security controls in place.

During *information gathering*, you attempt to identify what protection mechanisms are in place at the target by slowly starting to probe its systems. For example, an organization will often only allow traffic on a certain subset of ports on externally facing devices, and if you query the organization on any- thing other than a whitelisted port, you will be blocked. It is generally a good idea to test this blocking behavior by initially probing from an expendable IP address that you are willing to have blocked or detected. The same holds true when you’re testing web applications, where, after a certain threshold, the web application firewalls will block you from making further requests.
To remain undetected during these sorts of tests, you can perform your initial scans from IP address ranges that can’t be linked back to you and your team. Typically, organizations with an external presence on the Internet experience attacks every day, and your initial probing will likely be an unde- tected part of the background noise.

|**Information Categroy**|**Bookmarks**|
|:---------------------|:----------|
| IP Analysis |https://www.iana.org/numbers<BR>https://www.iana.org/assignments/as-numbers/as-numbers.xml<BR>https://www.iso.org/obp/ui/#home<BR>https://www.ultratools.com/tools/toolsHome<BR>https://www.robtex.com/<BR>http://www.team-cymru.org/IP-ASN-mapping.html<BR>http://www.iplocation.net/<BR>http://thyme.apnic.net/<BR>http://bgp.he.net/<BR>https://ipinfo.io|
| Whois Analysis |https://www.iana.org/numbers<BR>http://www.domaintools.com/|
| DNS Analysis |http://www.alexa.com/<BR>http://searchdns.netcraft.com/<BR>http://centralops.net/co/<BR>http://www.yougetsignal.com/<BR>http://webhosting.info/whois/<BR>http://reverseip.domaintools.com/<BR>http://viewdns.info/reverseip/<BR>|
| Identify Live Hosts |https://nmap.org/dist/sigs/?C=M;O=D<BR>https://zmap.io/<BR>http://masscan.net/<BR>http://www.secdev.org/projects/scapy/|
| IDS/IPS Identification |https://www.monkey.org/~dugsong/fragroute/<BR>http://pytbull.sourceforge.net/<BR>http://tcpreplay.synfin.net/|
| OSINT |https://www.shodan.io/<BR>https://www.exploit-db.com/google-hacking-database/<BR>|

# Links

1. [**How to gather Windows information ?**](./Windows/README.md)
2. [**How to gather Linux information ?**](./Linux/README.md)
3. [**How to gather Mac OSX information ?**]()
