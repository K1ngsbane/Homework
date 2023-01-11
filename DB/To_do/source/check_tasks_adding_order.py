import sqlite3

con = sqlite3.connect("tasks_DB.db")
cur = con.cursor()


def check_order(tasks_pool):
    """Shows tasks list ordered by adding time"""
    for element in tasks_pool:
        print(element['title'])

    cur.execute('''SELECT * FROM task''')
    print(cur.fetchall())
