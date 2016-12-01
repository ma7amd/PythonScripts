import sqlite3

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#fname = input('Enter file name: ')
#if ( len(fname) < 1 ) : fname = r"C:\Users\Mohamed.Salah\Desktop\Newfolder\nbox.txt"
fh = open(r"E:\Programming\Python\my project while learning Python\Eclipse\testing\mbox.txt")
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split("@")
    mail_org = pieces[1].rstrip()
    #print(mail_org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (mail_org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( mail_org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (mail_org, ))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts'

for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])

cur.close()
