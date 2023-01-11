import sqlite3

db = sqlite3.connect('users.db')
cur = db.cursor()


cur.execute(f'''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birthdate INT  
)''')


cur.execute(f'''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position TEXT,
    salary BIGINT
)''')


cur.execute(f'''CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER,
    type TEXT,
    value INT 
)''')


cur.execute('''SELECT contacts.type FROM contacts
    INNER JOIN employees ON contacts.id=employees.id
''')


cur.execute('''SELECT employees.salary, contacts.type, contacts.value 
    FROM employees
    INNER JOIN contacts ON employees.id=contacts.id
''')


db.commit()
db.close()
