**Authors**: < [nixawk](https://github.com/nixawk) >

----

# How to gather whois information ?

- Whois Searches
- Querying a Whois Database

Information in regard to whois gathering and how attackers use the information use the information that is displayed in whois records against unsuspecting organizational members, leaders and employees. This documentation touches the windows side of whois information gathering. This documentation is intended more for Linux / Unix users than for Windows.

## Whois Searches

whois searches allow the general public to search for information based on the grounds of, who web locations are registered to, expiry records, when a domain has been created, name servers and contact information. However whois information can also aid attackers in obtaining information to help launch a successful penetration into a network.

The documentation contained here will describe the venues in which an attacker will undergo in order to successfully obtain information to breach into a network using such details. We will also show you how to protect your organization and organizational information from such attacks. This document will cover details of what the attacker will perform when attempting to penetrate or gain information from whois records which may help them in successfully breaching your security.

## Querying a Whois Database

A whois look up will return information about the target company. Using this type of query you can also search for other entities associated with the target company. To perform the whois query against a remote host an attacker will issue the following command whois target-server.com -h whois.crsnic.net -H, this output will produce the following data:

```
$ whois google.com -h whois.arin.net

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

Aborting search 50 records found .....
GOOGLE.COM.ACKNOWLEDGES.NON-FREE.COM
GOOGLE.COM.AFRICANBATS.ORG
GOOGLE.COM.ANGRYPIRATES.COM
GOOGLE.COM.AR
GOOGLE.COM.AU
GOOGLE.COM.BAISAD.COM
GOOGLE.COM.BD
GOOGLE.COM.BEYONDWHOIS.COM
GOOGLE.COM.BR
GOOGLE.COM.BUGBOUNTY.TEST.CIPRI.COM
GOOGLE.COM.CN
GOOGLE.COM.CO
GOOGLE.COM.DEADKNIFERECORDS.COM
GOOGLE.COM.DGJTEST028-PP-QM-STG.COM
GOOGLE.COM.DIGNITYPRODUCT.COM
GOOGLE.COM.DO
GOOGLE.COM.EG
GOOGLE.COM.FORSALE
GOOGLE.COM.HACKED.BY.JAPTRON.ES
GOOGLE.COM.HANNAHJESSICA.COM
GOOGLE.COM.HAS.LESS.FREE.PORN.IN.ITS.SEARCH.ENGINE.THAN.SECZY.COM
GOOGLE.COM.HK
GOOGLE.COM.HOUDA.DO.YOU.WANT.TO.MARRY.ME.JEN.RE
GOOGLE.COM.IS.APPROVED.BY.NUMEA.COM
GOOGLE.COM.IS.NOT.HOSTED.BY.ACTIVEDOMAINDNS.NET
GOOGLE.COM.LASERPIPE.COM.DOMAINPENDINGDELETE.COM
GOOGLE.COM.LOLOLOLOLOL.SHTHEAD.COM
GOOGLE.COM.MAIKO.BE
GOOGLE.COM.MX
GOOGLE.COM.MY
GOOGLE.COM.NOHAREKART.COM
GOOGLE.COM.NS1.CHALESHGAR.COM
GOOGLE.COM.NS2.CHALESHGAR.COM
GOOGLE.COM.PE
GOOGLE.COM.PK
GOOGLE.COM.SA
GOOGLE.COM.SG
GOOGLE.COM.SHQIPERIA.COM
GOOGLE.COM.SOUTHBEACHNEEDLEARTISTRY.COM
GOOGLE.COM.SPAMMING.IS.UNETHICAL.PLEASE.STOP.THEM.HUAXUEERBAN.COM
GOOGLE.COM.SPROSIUYANDEKSA.RU
GOOGLE.COM.SUCKS.FIND.CRACKZ.WITH.SEARCH.GULLI.COM
GOOGLE.COM.TESTZZZZ.3000-RI.COM.DELETE-DNS.COM
GOOGLE.COM.TR
GOOGLE.COM.TW
GOOGLE.COM.UA
GOOGLE.COM.UK
GOOGLE.COM.UY
GOOGLE.COM.VABDAYOFF.COM
GOOGLE.COM

To single out one record, look it up with "xxx", where xxx is one of the
records displayed above. If the records are the same, look them up
with "=xxx" to receive a full display for each record.

>>> Last update of whois database: Thu, 29 Dec 2016 05:10:29 GMT <<<

For more information on Whois status codes, please visit https://icann.org/epp

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

No match for "-H".
>>> Last update of whois database: Thu, 29 Dec 2016 05:10:29 GMT <<<

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

No match for "WHOIS.ARIN.NET".
>>> Last update of whois database: Thu, 29 Dec 2016 05:10:46 GMT <<<

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.
```

We will refer to each bracket from the start, to finish as bracket A - D. We will then go into much more details as to each sector of brackets explaining how each section can effect security, and how attackers will use this information to gather a detailed map; and other details about the internal network, and structure of your organization to prepare for penetration. However, before we delve deeper into the information displayed on the whois sections, we will describe each domain in which whois searches can be compiled through. The following chart displays the information to query each region of the world in regard to whois look-ups.

|**Whois Server**|**Locations Effected**|**Server Address**|
|:---------------|:---------------------|:-----------------|
| ARIN | American Registry of Internet Numbers Continental United States. | http://arin.net |
| APNIC | Asia Pacific Information Center. |http://apnic.net |
| LACNIC | Latin American and Caribbean Internet Addresses Registry | http://lacnic.net |
| NIC.gov | Government Searches | http://nic.gov/whois.html |
| NetworkSolutions.com | Com, Net, Org, Edu name look ups | http://networksolutions.com |
| Whois.net | Whois lookup Server | http://whois.net |
| Crsnic.net | Verisign Whois Lookup | http://crsnic.net<BR>http://registrar.verisign-grs.com/whois/ |

Additional Information that can be returned from a whois query and abused is as follows:

|Return Query|Data Returned|Used for|
|:-----------|:------------|:-------|
|Address - Country|Location of Target|- Location of Target<BR>\- Physical Security<BR>- Dumpster Diving<BR>- Social Engineering|
|Net Range - Name Servers|Internet Addressing Scheme|- Utilzing for Targeting<BR>- Zone Transfers (ixfr | axfr)|
|Registration Update & Expirary|Date formats & Times|- Social Engineering<BR>- DNS Cache Poisoning|
|RTech handle - Rtech Email|Admin Contact Info|- First / Last Name<BR>- Social Engineering<BR>- Reverse Engineering<BR>- E-mail Contact<BR>- Possible Phone Contact<BR>- Home Location|

Additional resources for whois gathering and data mining:

|Resource|Information Gained|Information Used for|
|:-------|:-----------------|:-------------------|
|myspace.com,<BR>meetspot.com,<BR>adultfriendfinder.com,<BR>friendfinder.com,<BR>facebook.com,<BR>classmates.com|- Targets profile through surveys<BR>- persons they'd be receptive to<BR>- Complete likes, dislikes and vulnerabilities<BR>- A nonchalant vantage point into their lives|- Social / Reverse Engineering<BR>- Leveraging access from their machine to a corporate machine.<BR>- Passive information gathering utilzing sniffing<BR>- Possibility of physical invasion where physical attacks can take residence utilzing keyloggers and other hardware attacks.|
|Corporate BBS,<BR>Google Searches for Help,<BR>IT/IS Vendor Seaches (IBM, Solaris, Etc)|- Specific problems and help documentation<BR>- Techs, or Security professionals involved in solving tasks<BR>- Longterm / short term solutions which can be leveraged<BR>- Possibility of user names, or even passwords being utilized.|- Social / Reverse Engineering<BR>- User names for brute force and other attacks<BR>- Minor map of internal network<BR>- Short term solutions, which may contain vulnerabilities; long term solutions which may need further digging to circumvent<BR>- The ability of exposure to test locations, with the availability of passwords, and usernames where access can be granted.|
|monster.com,<BR>bigapplehead.com,<BR>dice.com,<BR>other job searches|- Architecture Utilzed<BR>- Contact information<BR>- Geographic Location<BR>- Possibility of additional links on corporate site, which may return more hidden links.|- Reverse & Social Engineering<BR>- Ability to possibly gain temporary access on site to take pictures, and social engineer employer.<BR>- Gather which technologies are in use to launch a penetration test, or attack the target.<BR>- Further understand and physical security implementations during job interview<BR>- With interview access, this gives "candidate" the ability to place road apples in or around the facility.|
