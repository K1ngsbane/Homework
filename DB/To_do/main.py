from source import *
from helpers import *
from data.test_data import TASK_TEST, tasks
import sqlite3

#Додав функціонал по створенню sqlite таблиці, додавання справи до таблиці, показати таблиці з датабази,
# змінити пріорітет, видалити справу.

con = sqlite3.connect("tasks_DB.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS task(
    id INT, 
    title TEXT, 
    priority INT, 
    due_date INT, 
    done TEXT
)''')
con.commit()


print('Доступні функції:')
for index in functional.functions:
    print(index + ': ' + functional.functions[index])

chosen = input('Виберіть функцію та введіть відповідну букву: ')
while True:
    if chosen.lower() == 'm':
        clear_screen.cls()
        print('Данні збережено. До зустрічі!')
        break
    elif chosen.lower() in functional.answer_option:
        if chosen.lower() == 'a':
            clear_screen.cls()
            add_task.add_new_task(tasks)
            con.commit()
            print(tasks)
            skip.skip()
        elif chosen.lower() == 'b':
            clear_screen.cls()
            find_task.find_task(tasks)
            skip.skip()
        elif chosen.lower() == 'c':
            clear_screen.cls()
            find_change_done.change_done_status(tasks)
            skip.skip()
        elif chosen.lower() == 'd':
            clear_screen.cls()
            find_change_priority.change_priority_db()
            skip.skip()
        elif chosen.lower() == 'e':
            clear_screen.cls()
            remove_task.del_task(tasks)
            skip.skip()
        elif chosen.lower() == 'f':
            clear_screen.cls()
            '''SELECT * FROM task'''
            check_tasks_adding_order.check_order(tasks)
            skip.skip()
        elif chosen.lower() == 'g':
            clear_screen.cls()
            check_tasks_priority_order.check_priority(tasks)
            skip.skip()
        elif chosen.lower() == 'h':
            clear_screen.cls()
            check_uncompleted.check_uncompleted(tasks)
            skip.skip()
        elif chosen.lower() == 'i':
            clear_screen.cls()
            check_completed.check_completed(tasks)
            skip.skip()
        elif chosen.lower() == 'j':
            clear_screen.cls()
            check_overdue.check_overdue(tasks)
            skip.skip()
        elif chosen.lower() == 'k':
            clear_screen.cls()
            check_statistics.check_stat(tasks)
            skip.skip()
        elif chosen.lower() == 'l':
            clear_screen.cls()
            print('Тестові данні збережено.')
            skip.skip()
        for index in functional.functions:
            print(index + ': ' + functional.functions[index])
        chosen = input('Виберіть функцію та введіть відповідну букву: ')
    else:
        chosen = input('Виберіть корректний індекс задачі: ')
