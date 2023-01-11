from helpers.get_task import get_task
import sqlite3

con = sqlite3.connect("tasks_DB.db")
cur = con.cursor()


def change_priority(tasks_pool):
    my_object = get_task(tasks_pool)
    if my_object:
        my_object['done'] = True
        input_number = input('Оновлений пріорітет: ')
        while True:
            if input_number.isdigit() and int(input_number) <= 10:
                my_object['priority'] = int(input_number)
                break
            else:
                input_number = input('Ведіть корректне значення пріорітету (число від 1 до 10): ')


def change_priority_db():
    task_name = input('Введіть назву справи: ')
    new_priority = input('Введіть новий пріорітет: ')
    cur.execute(f'''UPDATE task
        SET priority = ?
        WHERE title = ?''', [new_priority, task_name])
    con.commit()
