**Authors**: < [nixawk](https://github.com/nixawk) >

----

# How to gather dns information ?

- Passive mode
  - DNS Enumeration
  - OSINT
- Offensive mode
  - spider websites
- Tools
  - recon-ng
  - dnsrecon
  - theHarvester

## Passive mode

### DNS Enumeration

**DNS enumeration** is the process of locating all the DNS servers and their corresponding records for an organization. A company may have both internal and external DNS servers that can yield information such as usernames, computer names, and IP addresses of potential target systems. There are a lot of tools that can be used to gain information for performing DNS enumeration. The examples of tool that can be used for DNS enumeration are NSlookup, DNSstuff, American Registry for Internet Numbers (ARIN), and Whois. To enumerate DNS, you must have understanding about DNS and how it works.

You must have knowledge about DNS records. The list of DNS record provides an overview of types of resource records (database records) stored in the zone files of the Domain Name System (DNS). The DNS implements a distributed, hierarchical, and redundant database for information associated with Internet domain names and addresses. In these domain servers, different record types are used for different purposes. The following list describes the common DNS record types and their use:

|**DNS Record types**|methods|description|
|:-----------------------|:----------|:--------------|
|dns query|A|***Address record***, Returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host, but it is also used for DNSBLs, storing subnet masks in RFC 1101, etc.|
|dns query|CNAME|***Canonical name record***, Alias of one name to another: the DNS lookup will continue by retrying the lookup with the new name.|
|dns query|AAAA|***IPv6 address record***, Returns a 128-bit IPv6 address, most commonly used to map hostnames to an IP address of the host.|
|dns query|MX|***Mail exchange record***, Maps a domain name to a list of message transfer agents for that domain|
|dns query|NS|***Name server record***, Delegates a DNS zone to use the given authoritative name servers|
|dns query|SOA|***zone of authority record***, Specifies authoritative information about a DNS zone, including the primary name server, the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.|
|dns query|SPF|***Sender Policy Framework***, a simple email-validation system designed to detect email spoofing by providing a mechanism to allow receiving mail exchangers to check that incoming mail from a domain comes from a host authorized by that domain's administrators.|
|dns query|TXT|***Text record***, Originally for arbitrary human-readable text in a DNS record.|
|dns query|PTR|***Pointer record***, Pointer to a canonical name. Unlike a CNAME, DNS processing stops and just the name is returned. The most common use is for implementing reverse DNS lookups, but other uses include such things as DNS-SD.|
|dns query|SRV|***Service locator***, Generalized service location record, used for newer protocols instead of creating protocol-specific records such as MX.|
|dns query|NSEC|***Next Secure record***, Part of DNSSEC—used to prove a name does not exist. Uses the same format as the (obsolete) NXT record.|
|dns query|AXFR|***Authoritative Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers. **DNS Zone Transfer** is typically used to replicate DNS data across a number of DNS servers, or to back up DNS files. A user or server will perform a specific zone transfer request from a ―name server.‖ If the name server allows zone transfers to occur, all the DNS names and IP addresses hosted by the name server will be returned in human-readable ASCII text.|
|dns query|IXFR|***Incremental Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers.|
|dns query|DNS Wildcard|Check if nameserver enable wildcard query, or dns faked.|
|dns query|domain bruteforce|bruteforce subdomains with wordlists.|
|dns query|reverse bruteforce|reverse ip for domain|
|dns query|srv bruteforce|bruteforce srv records|
|dns query|gtld bruteforce|bruteforce gtld records|
|dns query|tld bruteforce|bruteforce tld records|

### OSINT

|OSINT|Category|Description|
|:----|:-------|:----------|
|OSInt|Google|Spider domains from Google pages with domain:`demo.com`|
|OSInt|Bing|Spider domains from Bing pages with domain:`demo.com`|
|OSInt|Yahoo|Spider domains from Yahoo with domain:`demo.com`|
|OSInt|Baidu|Spider domains from Baidu with domain:`demo.com`|
|OSInt|Netcraft|Spider domains from netcraft searchdns pages|
|OSInt|Github|Spider domain from github pages|
|OSInt|Shodan|Search domains from Shodan|
|OSInt|Censys|Search domains from censys|
|OSInt|ZoomEye|Search domains from ZoomEye|


## Offensive mode

|**offensive mode**|**methods**|**description**|
|:-----------------|:----------|:--------------|
|Websites|Spider default page|Scan default pages and spider domains|
|Websites|Certificates|Scan domains certificates|


## Tools

|**recon-ng Command**|**Description**|
|:-------------------|:--------------|
|use recon/domains-hosts/baidu_site|Search domains with baidu|
|use recon/domains-hosts/bing_domain_api|Search domains with bing api|
|use recon/domains-hosts/bing_domain_web|Search domains from bing web pages.|
|use recon/domains-hosts/brute_hosts|Bruteforce subdomains|
|use recon/domains-hosts/google_site_api|Search domains with google api|
|use recon/domains-hosts/google_site_web|Search domains from google web pages.|
|use recon/domains-hosts/netcraft|Search domains from netcraft pages.|



|**dnsrecon Command**|**Description**|
|:----------|:--------------|
|dnsrecon -n `8.8.8.8` -d `demo.com`|Pleaes use a valid dns server in order to avoid dns fake. |
|dnsrecon -d `demo.com` -t std|SOA, NS, A, AAAA, MX and SRV if AXRF on the NS servers fail.|
|dnsrecon -d `demo.com` -t rvl|Reverse lookup of a given CIDR or IP range.|
|dnsrecon -d `demo.com` -t brt -D `/path/to/subdomains.wd`|Brute force domains and hosts using a given dictionary.|
|dnsrecon -d `demo.com` -t brt -D `/path/to/subdomains.wd` --iw|Brute force domains and hosts using a given dictionary. `Continue brute forcing a domain even if a wildcard records are discovered.`|
|dnsrecon -d `demo.com` -t srv|SRV records|
|dnsrecon -d `demo.com` -t axfr|Test all NS servers for a zone transfer.|
|dnsrecon -d `demo.com` -t goo|Perform Google search for subdomains and hosts.|
|dnsrecon -d `demo.com` -t tld|Remove the TLD of given domain and test against all TLDs registered in IANA.|
|dnsrecon -d `demo.com` -t zonewalk|Perform a DNSSEC zone walk using NSEC records.|
|dnsrecon -d `demo.com` --db `/path/to/results.sqlite`|Save results in a sqlite file.|
|dnsrecon -d `demo.com` --xml `/path/to/results.xml`|Save results in a xml file.|
|dnsrecon -d `demo.com` -c `/path/to/results.csv`|Save results in a csv file.|
|dnsrecon -d `demo.com` -j `/path/to/results.json`|Save results in a json file.|


|**theHarvester Command**|**Description**|
|:-----------------------|:--------------|
|theharvester -d `demo.com` -b all|Search google, googleCSE, bing, bingapi, pgp, linkedin,google-profiles, jigsaw, twitter, googleplus, all|
|theharvester -d `demo.com` -n|Perform a DNS reverse query on all ranges discovered|
|theharvester -d `demo.com` -c|Perform a DNS brute force for the domain name|
|theharvester -d `demo.com` -t|Perform a DNS TLD expansion discovery|
|theharvester -d `demo.com` -e `8.8.8.8`|Specfic a dns server|
|theharvester -d `demo.com` -h|use SHODAN database to query discovered hosts|

|**Metasploit Command**|**Description**|
|:---------------------|:--------------|
|msf > use auxiliary/gather/enum_dns|gather dns records information(A, AAAA, CNAME, ZoneTransfer, SRV, TLD, RVL, ...)|


# Links

1. https://en.wikipedia.org/wiki/List_of_DNS_record_types
2. https://www.exploit-db.com/docs/12389.pdf
3. https://pentestlab.blog/tag/dns-enumeration/
4. http://tools.kali.org/information-gathering/dnsrecon
5. https://github.com/nixawk/ig/
