
## Instant debugger

The -r command line switch is used to run the built-in debugger without creating a database in advance. The format is this switch is:

```-rdebname{params}:pass@hostname:port+pid```

The explanation of the fields:

  debname       Debugger name. Should contain the debugger
                module name. Examples: win32, linux. This prefix
				can be shortened  or even completely
				omitted if there is no ambiguity
  params        Optional parameter for the debugger module
                The parameters from the appropriate configuation file
				can be specified here, separated by semicolons.
  pass          Password for the remote debugger server
  hostname      Host name or address of the remote debugger server
  port          Port number to use to connect to the debugger server
  pid           PID of the process to attach

All fields except the first one are optional. See examples below for typical command lines:

```
  idaq -rwin32 file args
         Run 'file' with command line 'args' in the local debugger
		 We have to specify the debugger name to avoid ambiguities.
  idaq -rwindbg+450
         Attach to process 450 on the local machine using the windbg backend
  idaq -rl:password@mycom:4567+
         Connect to the remote linux computer 'mycom' at port 4567 using the
		 password 'password' and display the list of processes running on it.
		 Allow the user to select a process and attach to it.
  idaq -rl@mycom /bin/ls e*
         Run '/bin/ls' command on the 'mycom' computers using the
		 remote linux debugger server. Use an empty password and the 
		 default port number. IDA will extract the name of the
		 executable from the whobase.idb file in the local current
		 directory. If the database does not exist, then this command
		 will fail.
  idaq "-rwindbg{MODE=1}@com:port=\\.\pipe\com_1,baud=115200,pipe,reconnect+"
         Attach using windbg in kernel mode. The connection starting is 
		 "com:port=\\.\pipe\com_1,baud=115200,pipe,reconnect". A mini database
		 will be created on the fly.
```

When the -r switch is used, IDA works with the databases in the following way:

  - if a database corresponding to the input file exists and the -c switch has not been specified, then IDA will use the database during the debugging session
  - otherwise, a temporary database will be created

Temporary databases contain only meta-information about the debugged process and not memory contents. The user can make a memory snpshot any time before the process stops. If IDA detects that a command will cause the process to exit or detach IDA, it will purpose to make a snapshot.

  The rest of the command line is passed to the launched process.

  In the case there is no input file (when attaching to existing process, for example), then the temporary database is created in the standard temporary directory. For Windows, this directory is usually "Local Setting\Temp" in the user profile directory.
