from helpers.get_task import get_task
import sqlite3

con = sqlite3.connect("tasks_DB.db")
cur = con.cursor()


def del_task(tasks_pool):
    """Deletes the task from task pool"""
    my_obj = input('Введіть назву справи: ')
    if my_obj:
        cur.execute(f'''DELETE FROM task WHERE title=?''', [my_obj])
        con.commit()
