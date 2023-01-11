import sqlite3

db = sqlite3.connect('users.db')
cur = db.cursor()


cur.execute('''
INSERT INTO users(name, birthdate) VALUES
('Alex', '18.05.99'),
('Dima', '31.04.98'),
('Glad', '54.54.54')
''')


cur.execute('''
INSERT INTO employees(position, salary) VALUES
('Software Developer', '54000'),
('Game Developer', '54000'),
('Thief', '27')
''')


cur.execute('''
INSERT INTO contacts(id, type, value) VALUES
('1', 'e-mail', 'alex@gmail.com'),
('1', 'phone', '+3809714882280'),
('2', 'e-mail', 'dima@gmail.com'),
('2', 'phone', '+3809714882281'),
('3', 'e-mail', 'glad54@gmail.com')
''')

db.commit()
db.close()