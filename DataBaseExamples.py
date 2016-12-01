
"""
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
import sys
import pygame
import pypyodbc

#pypyodbc.win_create_mdb('D:\\sona232.mdb')
#open database connection
conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.Mdb)}; DBQ=/home/muhammad/Downloads/sona232.mdb')
#prepare a cursor object using cursor
cur = conn.cursor()
sql1 = "SELECT * FROM names"
try:
   cur.execute(sql1)
   results = cur.fetchall()
   for row in results:
        id = row[0]
        name = row[1]
        print("id=%d , name=%s" % (id, name))



    #print(fid= "%d" ,fname="%s")
except:

    print("error xsona")
cur.commit()
conn.close()
"""
#######################################################################3
"""

import sqlite3

conn = sqlite3.connect("samlpe.db")         #entering the name of your database file to be created automaticlly
cur = conn.cursor()

def create_table():                         #creating tables and we do it once
    cur.execute("CREATE TABLE example(LANGUAGE VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    cur.execute("INSERT INTO example VALUES('Python', 2.7,'Beginner')")
    cur.execute("INSERT INTO example VALUES('Python', 2.7,'Intermediate')")
    cur.execute("INSERT INTO example VALUES('Python', 2.7,'Expret')")
    cur.execute("INSERT INTO example VALUES('Python', 3.3,'Intermediate')")
    cur.execute("INSERT INTO example VALUES('Python', 3.5,'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What Languge you gonna use ? ")
    version = float(input("Which version is prefered ? "))
    skill = input("Thw Skills is ? ")
    cur.execute("INSERT INTO example('LANGUAGE, Version, Skill') VALUES(?, ?, ?), (lang, version, skill)")
    conn.commit()

def read_data():

    sql = "SELECT * FROM example"           #how to print data in one shoot
    for row in cur.execute(sql):
        print(row)
        print(row[0])

def read_data_dynamic():
    what_skill = input("What skill level you looking for ? ")       #printing specific row with pre-requests
    what_lang = input("What Language you prefer ? ")

    sql1 = "SELECT * FROM example WHERE Skill = ? AND LANGUAGE = ?"
    for row in cur.execute(sql1, [(what_skill), (what_lang)]):
        print(row)

def update_data():                              #updating values and changing them
    sql2 = "UPDATE example SET Skill = '(b)eginner' WHERE Skill = 'Beginner'"
    cur.execute(sql2)
    sql2 = "SELECT * FROM example"
    for row in cur.execute(sql2):
        print(row)
    conn.commit()

def delete_data():
    sql3 = "SELECT * FROM example"
    for row in cur.execute(sql3):               #see how data is before deleting
        print(row)
    conn.commit()

    print(20*"#")

    sql3 = "DELETE FROM example WHERE Version = 2.7"    #the deleting operation
    cur.execute(sql3)
    conn.commit()

    sql3 = "SELECT * FROM example"              #see the rest of data after deleting
    for row in cur.execute(sql3):
        print(row)



#create_table()                             #we do it once
#enter_data()                               #function that creates values inside tables but manually
#enter_dynamic_data()                       #function that creates values inside tables but dynamiclly
#read_data()
#read_data_dynamic()
#update_data()
#delete_data()



conn.close()

"""
##############################################################################

"""

from peewee import *

db = SqliteDatabase("students.db")


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)

"""
###############################################################################

"""
Python is one of the most diverse and best languages to learn, here is how to make a simple
database in Python.



# Most common DBAPI conversion modules
# MySQL - MySQLdb
# PostrgeSQL - psycopg(2)
# SQLite - sqlite3
# Oracle - oracle
# M$ SQL server - adodbapi
# to create user (as root) with necessary privilages:
# mysql&gt; grant all on *.* to test_user@localhost identified by 'showmedo' with grant option;
# import relevant module
import pymysql


# test variables for database access
HOST = 'localhost'
USER = 'test_user'
PASSWD = 'showmedo'
DATABASE = 'showmedo_test'

# test DB data to insert into new tables
# name, email, join-date, author-status
table_data = {
        'showmedo_user':(
        ('kyran dale', 'kg@showmedo.com', '2007-09-11',0),
        ('ian ozsvald', 'ian@showmedo.com', '2008-01-11',1),
        ('thomas eddison', 'tom@gec.com', '2007-11-24',1),
        ('richard coates', 'rc@tinburgen.org', '2008-04-22',0),
        ('karl von frisch', 'kvf@maxplank.ac.de', '2008-01-09',0),
        ('susan mortimer', 'suzie@backlogger.com', '2007-08-15',1),
        ('alan sussman', 'alan.sussman@gmail.com', '2007-07-15',0),
        ('bernard reeves', 'bernie@abc.com', '2007-07-23',0),
        ('phil tensing', 'phit@mmd.com', '2008-02-05',0),
        ('elaine dean', 'ellie@lotech.com', '2007-11-24',1),
        )
    }

def prettyPrint(data):
    print("There are %d data items"%len(data))
    for i,d in enumerate(data):
        print("%d --- "%i, d)

# make a connection to the DATABASE database
# if we were using, for example, a Postrgres database this line would start:
# db_connection = psycopg.connect( ...

db_connection = pymysql.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        #db=DATABASE
        )



db_connection = pymysql.connect("ma7amd.mysql.pythonanywhere.services.com", "ma7amd", "0103068999", "ma7amd$defualt")
# we'll need a cursor to this database to execute commands
cursor = db_connection.cursor()

# demonstrate the creation of a database
#cursor.execute('show databases')
#prettyPrint(cursor.fetchall())
#cursor.execute('create database showmedo_test')
#cursor.execute('show databases')
#prettyPrint(cursor.fetchall())

## switch to using the newly-created database
cursor.execute('use showmedo_test')

# use the cursor to execute a 'create table' command
#cursor.execute(
#CREATE TABLE showmedo_user(
  #id INTEGER  NOT NULL AUTO_INCREMENT,
  #name VARCHAR(255)  NOT NULL,
  #email VARCHAR(255),
  #join_date DATE,
  #author_status TINYINT(1),
  #PRIMARY KEY(id)
#)
#)

# loop through our table-data, inserting items into the database
for data in table_data['showmedo_user']:
    qstr = "INSERT INTO showmedo_user " +\
            "(name, email, join_date, author_status) values ('%s', '%s', '%s', %d)"%(data[0], data[1], data[2], data[3])
    print(qstr)
    cursor.execute(qstr)

"""
###################################################################################