import mysql.connector
from mysql.connector import errorcode, connect

cnx = connect(
          user= 'root',
          password= '',
          host= '127.0.0.1',
          database= 'PythonTest'
)

cursor = cnx.cursor(buffered=True)

# 4 main opertions on DB
# C(reate)R(ead)U(pdate)D(delete) = CRUD

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Creating table in DB

cursor.execute('''
    CREATE TABLE EMPLOYEE(
          FIRST_NAME CHAR (20) NOT NULL,
          LAST_NAME CHAR (20),
          AGE INT,
          GENDER CHAR (1),
          INCOME FLOAT
          )
    ''')


# SQL statement will be run in the execute() func
# Way (1)
sql = """
    INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME)
    VALUES ("MUHAMMAD", "ABU SALAH", 110, 'M', 50000)
      """


# If error will appear during the posting process for data on DB error will be thrown

try:
    cursor.execute(sql)
    cnx.commit()
except:
    cnx.rollback()


# Way (2)
fname = "Salem"
lname = "Harbi"
age = 50
gender = "M"
income = 90065

sql2 = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME) \
        VALUES ('%s', '%s', '%d', '%c', '%d') " % (fname, lname, age, gender, income)

try:
    cursor.execute(sql2)
    cnx.commit()
except:
    cnx.rollback()

# Way (3)
data = {
    0:{
        "fname": "Hala",
        "lname": "Hamido",
        "age": 60,
        "gender": "F",
        "income": 79125
    },
    1:{
        "fname": "Dodi",
        "lname": "Talat",
        "age": 92,
        "gender": "F",
        "income": 12557
    },
    2:{
        "fname": "Haridi",
        "lname": "Elwardy",
        "age": 41,
        "gender": "M",
        "income": 76216
    },
    3:{
        "fname": "Rady",
        "lname": "Kamal",
        "age": 30,
        "gender": "M",
        "income": 5326534
    }
}

for i in data:
    sql3 = ("INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d') " % (data[i]["fname"], data[i]["lname"], data[i]["age"], data[i]["gender"], data[i]["income"]))
    #print(sql3)
    try:
        cursor.execute(sql3)
        cnx.commit()
    except:
        cnx.rollback()

# Read data from DB
limit = 150000
sql4 = ("SELECT * FROM EMPLOYEE WHERE INCOME > %d" % (limit))

def retriveData(sql):
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        one = cursor.fetchone()
        return result, one
    except:
        cnx.rollback()

print(retriveData(sql4))

sql5 = "UPDATE EMPLOYEE SET AGE = AGE + 1"
try:
    cursor.execute(sql5)
    cnx.commit()
except:
    cnx.rollback()


# Delete data from DB
agelimit = 50

sql6 = ("DELETE FROM EMPLOYEE WHERE AGE > %d" % agelimit)
try:
    cursor.execute(sql6)
    cnx.commit()
except:
    cnx.rollback()



cnx.close()

# ********************************************************************* #
# ********************************************************************* #


from datetime import date, datetime, timedelta


cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
data_salary = {
  'emp_no': emp_no,
  'salary': 50000,
  'from_date': tomorrow,
  'to_date': date(9999, 1, 1),
}
cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

# ********************************************************************* #
# ********************************************************************* #