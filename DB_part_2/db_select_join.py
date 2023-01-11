import sqlite3

db = sqlite3.connect('users.db')
cur = db.cursor()


cur.execute('''
SELECT position, type, value FROM employees
INNER JOIN contacts ON contacts.id = employees.id
''')

print(cur.fetchall())

cur.execute('''
SELECT type, value, position FROM contacts
INNER JOIN employees ON employees.id=contacts.id 
''')

print(cur.fetchall())

cur.execute('''
SELECT name, position, salary FROM users
INNER JOIN employees ON employees.id=users.id
''')

print(cur.fetchall())
