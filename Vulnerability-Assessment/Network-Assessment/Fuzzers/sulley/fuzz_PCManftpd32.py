# Video 1 Practical Fuzzing Basic using the Sulley Framework
# http://www.dfate.de/public/index.php/post/exploit-development-series-video-1-practical-fuzzing-basics-using-the-sulley-framework
# https://www.exploit-db.com/exploits/37731/

# -------------------------------------------------------------------
# Usage:
# C:\Fuzzing\sulley>python network_monitor.py -d 0 -f "port 21" -P audit
# C:\Fuzzing\sulley>python process_monitor.py -c audit\pcmanftpd_crashbin -p "PCManFTPD2.exe"

# -------------------------------------------------------------------
# Analysis:

"""
220 PCMan's FTP Server 2.0 Ready.
USER anonymous
331 User name okay, need password.
PASS password12345
230 User logged in
PORT 192,168,1,106,206,27
200 Command okay.
STOR demo2.txt
150 File status okay; Open data connection.
226 Data Sent okay.
PORT 192,168,1,106,206,28
200 Command okay.
LIST
150 File status okay; Open data connection.
226 Data Sent okay.
PORT 192,168,1,106,206,29
200 Command okay.
RETR demo2.txt
150 File status okay; Open data connection.
226 Data Sent okay.
QUIT
"""

from sulley import *

# General Overview
# 1. Create requests (define fuzzing grammar)
# 2. Define sessions
# 3. Define target
# 4. Fuzz!

# s_initialize - Construct a new request
# s_static ("USER") - A string that is static (umutated) and does not get fuzzed
# s_delin(" ") - A delimiter that can be fuzzed. Will have different mutations that using s_string
# s_string("anonymous") - A string that will be mutated. Includes more mutations than s_delim

# -------------------------------------------------------------------
# Grammar to be tested
s_initialize("user")
s_static("USER")
s_delim(" ", fuzzable=False)
s_string("anonymous")
s_static("\r\n")

s_initialize("pass")
s_static("PASS")
s_delim(" ", fuzzable=False)
s_string("pass12345")
s_static("\r\n")

s_initialize("put")
s_static("PUT")
s_delim(" ", fuzzable=False)
s_string("fuzz_strings")
s_static("\r\n")

s_initialize("stor")
s_static("STOR")
s_delim(" ", fuzzable=True)
s_string("AAAA")
s_static("\r\n")

s_initialize("mkd")
s_static("MKD")
s_delim(" ", fuzzable=False)
s_string("AAAA")
s_static("\r\n")

# -------------------------------------------------------------------
# Define pre_send function. Will be executed right after the three-way handshake
def receive_ftp_banner(sock):
    data = sock.recv(1024)
    print(data)

# -------------------------------------------------------------------
# Define session
# Session parameters
SESSION_FILENAME = "pcmanftpd-session"  # Keeps track of the current fuzzing state
SLEEP_TIME = 0.5                        # Pause between two fuzzing attempts
TIMEOUT = 5                             # Fuzzer will time out after 5 seconds of no connection
CRASH_THRESHOLD = 4                     # After 4 crashes parameter will be skipped

mysession = sessions.session(
    session_filename=SESSION_FILENAME,
    sleep_time=SLEEP_TIME,
    timeout=TIMEOUT,
    crash_threshold=CRASH_THRESHOLD)

mysession.pre_send = receive_ftp_banner
mysession.connect(s_get("user"))
mysession.connect(s_get("user"), s_get("pass"))
mysession.connect(s_get("pass"), s_get("stor"))
mysession.connect(s_get("pass"), s_get("mkd"))
mysession.connect(s_get("pass"), s_get("put"))

# -------------------------------------------------------------------
# Draw graph representing the fuzzing paths.
with open("session_test.udg", "w+") as f:
    f.write(mysession.render_graph_udraw())

# -------------------------------------------------------------------
# Just some overview output

print("Number of mutation during one case: %s\n" % str(s_num_mutations()))
print("Total number of mutations: %s\n" % str(s_num_mutations() * 5))

decision = raw_input("Do you want to continue?(y/n): ")
if decision == "n":
    exit()

# -------------------------------------------------------------------
# Define target paramsters
host = "192.168.1.107"
ftp_port = 21
netmon_port = 26001
procmon_port = 26002
target = sessions.target(host, ftp_port)
target.procmon = pedrpc.client(host, procmon_port)
target.netmon = pedrpc.client(host, netmon_port)

target.procmon_options = {
    "proc_name": "pcmanftpd2.exe",
    "stop_commands": ["wmic process where (name='PCManFTPD2.exe') call terminate"],
    "start_commands": ["C:\\PCManFTP\\PCManFTPD2.exe"]
}

# Add target to the session
mysession.add_target(target)

# -------------------------------------------------------------------
# Lets get rollin

print("Starting fuzzing now")
mysession.fuzz()

# Starts the fuzzing process and
# also the web interface (http://127.0.0.1:26000) to see the current state
