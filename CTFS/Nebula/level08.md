# Level08

#### About

World readable files strike again. Check what that user was up to, and use it to log into flag08 account. 
To do this level, log in as the level08 account with the password level08. Files for this level can be found in /home/flag08. 


#### Source code

There is no source code available for this level 

* analysis capture.pcap
* hexdump -C dump.txt  <---- http://www.asciitable.com/

```
$ hexdump.exe -C dump.txt
00000000  ff fd 25 ff fc 25 ff fb  26 ff fd 18 ff fd 20 ff  |..%..%..&..... .|
00000010  fd 23 ff fd 27 ff fd 24  ff fe 26 ff fb 18 ff fb  |.#..'..$..&.....|
00000020  20 ff fb 23 ff fb 27 ff  fc 24 ff fa 20 01 ff f0  | ..#..'..$.. ...|
00000030  ff fa 23 01 ff f0 ff fa  27 01 ff f0 ff fa 18 01  |..#.....'.......|
00000040  ff f0 ff fa 20 00 33 38  34 30 30 2c 33 38 34 30  |.... .38400,3840|
00000050  30 ff f0 ff fa 23 00 53  6f 64 61 43 61 6e 3a 30  |0....#.SodaCan:0|
00000060  ff f0 ff fa 27 00 00 44  49 53 50 4c 41 59 01 53  |....'..DISPLAY.S|
00000070  6f 64 61 43 61 6e 3a 30  ff f0 ff fa 18 00 78 74  |odaCan:0......xt|
00000080  65 72 6d ff f0 ff fb 03  ff fd 01 ff fd 22 ff fd  |erm.........."..|
00000090  1f ff fb 05 ff fd 21 ff  fd 03 ff fc 01 ff fb 22  |......!........"|
000000a0  ff fa 22 03 01 00 00 03  62 03 04 02 0f 05 00 00  |..".....b.......|
000000b0  07 62 1c 08 02 04 09 42  1a 0a 02 7f 0b 02 15 0f  |.b.....B........|
000000c0  02 11 10 02 13 11 02 ff  ff 12 02 ff ff ff f0 ff  |................|
000000d0  fb 1f ff fa 1f 00 b1 00  31 ff f0 ff fd 05 ff fb  |........1.......|
000000e0  21 ff fa 22 01 03 ff f0  ff fa 22 01 07 ff f0 ff  |!.."......".....|
000000f0  fa 21 03 ff f0 ff fb 01  ff fd 00 ff fe 22 ff fd  |.!..........."..|
00000100  01 ff fb 00 ff fc 22 ff  fa 22 03 03 e2 03 04 82  |......".."......|
00000110  0f 07 e2 1c 08 82 04 09  c2 1a 0a 82 7f 0b 82 15  |................|
00000120  0f 82 11 10 82 13 11 82  ff ff 12 82 ff ff ff f0  |................|
00000130  0d 0a 4c 69 6e 75 78 20  32 2e 36 2e 33 38 2d 38  |..Linux 2.6.38-8|
00000140  2d 67 65 6e 65 72 69 63  2d 70 61 65 20 28 3a 3a  |-generic-pae (::|
00000150  66 66 66 66 3a 31 30 2e  31 2e 31 2e 32 29 20 28  |ffff:10.1.1.2) (|
00000160  70 74 73 2f 31 30 29 0d  0a 0a 01 00 77 77 77 62  |pts/10).....wwwb|
00000170  75 67 73 20 6c 6f 67 69  6e 3a 20 6c 00 6c 65 00  |ugs login: l.le.|
00000180  65 76 00 76 65 00 65 6c  00 6c 38 00 38 0d 01 00  |ev.ve.el.l8.8...|
00000190  0d 0a 50 61 73 73 77 6f  72 64 3a 20 62 61 63 6b  |..Password: back|
000001a0  64 6f 6f 72 7f 7f 7f 30  30 52 6d 38 7f 61 74 65  |door...00Rm8.ate|
000001b0  0d 00 0d 0a 01 00 0d 0a  4c 6f 67 69 6e 20 69 6e  |........Login in|
000001c0  63 6f 72 72 65 63 74 0d  0a 77 77 77 62 75 67 73  |correct..wwwbugs|
000001d0  20 6c 6f 67 69 6e 3a 20                           | login: |
000001d8
```

* Password: backdOORmate
