
## Command line swithes

![](https://github.com/all3g/exploit-exercises/blob/master/IDA/IDA-command-line-options.png)

IDA can be launched with one of the following command lines:

  - idaq input-file  (All platforms: start graphical interface)
  - idaw input-file  (Windows: start text interface)
  - idal input-file  (Linux/Mac: start text interface)
 
Add the '64' postfix to the command name in order to start the 64-bit version of IDA. For example:

  ```idaq64 input-file```

will start 64-bit graphical interface.

The following command line switches are recognized:

```
-a     disable auto analysis
-A     autonomous mode. IDA will not display dialog boxes.
       Designed to be used together with -S switch.
-b#### loading address, a hexadecimal number, in paragraphs
       (a paragraph is 16 bytes)
-B     batch mode. IDA will generate .IDB and .ASM files automatically
-c     disassemble a new file (delete the old database)
-ddirective
       A configuration directive which must be processed at the first
	   pass. Example:
	           -dVPAGESIZE=8192
-Ddirective
       A configuration directive which must be processed at the second
	   pass.
-f     disable FPP instructions (IBM PC only)
-h     help screen
-i#### program entry point (hex)
-I#    set IDA as just-in-time debugger (0 to disable and 1 to enable)
-L#### name of the log file
-M     disable mouse (text only)
-O#### options to pass to plugins
-o#### specify the output database (implies -c)
-p#### processor type
-P+    compress database (create zipped idb)
-P     pack database (create unzipped idb)
-P-    do not pack  database (not recommaned, see Abort command)
-r###  immediately run the built-in debugger
       format of this switch is explained here
-R     load	MS Windows exe file resources
-S###  Execute a script file when the database is opened.
       The script file extension is used to determine which extlang will run the script.
	   It is possible to pass command line arguments after the script name.
	   For example: -S"myscript.idc argument1 \"argument 2\" argument3"
	   The passed parameters are stored in the "ARGV" global IDC variable.
	   Use "ARGV.count" to determine the number of arguments.
	   The first argument "ARGV[0]" contains the script name
-T###  interpret the input file as the spwecified file type
       The file type is specified as a prefix of a file type
	   visible in the 'load file' dialog box
-t	   create an empty database.
-W###  specify MS Windows directory
-x     do not create segmentation
       (used in pair with Dump database command)
	   this switch affects EXE and COM format files only.
-z     debug:
               00000001 drefs
			   00000002 offsets
			   00000004 first
			   00000008 idp module
			   00000010 idr module
			   00000020 plugin module
			   00000040 ids files
			   00000080 config file
			   00000100 check heap
			   00000200 checkarg
			   00000400 demangler
			   00000800 queue
			   00001000 rollback
			   00002000 already data or code
			   00004000 type system
			   00008000 show all notifications
			   00010000 debugger
			   00200000 Appcall 
			   00400000 source-level debugger
-?     this screen (works for the next version)
?      this screnn (works for the next version)
```

For batch mode, IDA must be invoked with the following command line:

  ```idaq -B input-file```

 which is equivalent to

  ```idaq -c -A -Sanalysis.idc input-file```

The text interface (idaw.exe/idal) is better for batch mode because it uses less system resources. Howeveer, please note that regular plugins are not automatically loaded in batch mode because the analysis .idc file quits and the kernel has no chance to load them.

For more information, please see the analysis.idc file in the IDC subdirectory.

