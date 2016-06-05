import sqlite3 as d

d = d.connect('database/database.db')

c = d.cursor()
c.execute('DROP TABLE IF EXISTS post')
c.execute("CREATE TABLE post(id INT PRIMARY KEY AUTOINCREMENT, data VARCHAR(80), date_post DATE)")
c.close()
print "success make db"
