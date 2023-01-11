import sqlite3

db = sqlite3.connect('users.db')
cur = db.cursor()


cur.execute('''SELECT * FROM employees''')

print(cur.fetchall())
