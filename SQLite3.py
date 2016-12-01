
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
read_data_dynamic()
#update_data()
#delete_data()



conn.close()


