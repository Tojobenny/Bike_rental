Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: D:\mybike\manage.py =========================

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
>>> from django.db import connection
>>> c=connection.cursor()
>>> c.execute("create table logind(lid integer primary key autoincrement,mail text,pass text(20) )")
<django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x04A8B7A8>
>>> c.execute("insert into logind(mail,pass)values('tojobennynill@gmail.com','1234567')")
<django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x04A8B7A8>
>>> c.execute("create table booking(bid integer primary key autoincrement,bike text,pdate date,ddate date,bname text,bemail text,bpno integer)")
<django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x0411B758>
c.execute("create table admins (adid integer primary key autoincrement,mail text,pass text(20))")
>>> c.execute("insert into admins(mail,pass)values('tojo@gmail.com','123')")
c.execute("create table bikelist (id integer primary key autoincrement,regno text,engno text,rent integer,model text,desc text,colour text,image text)") 

