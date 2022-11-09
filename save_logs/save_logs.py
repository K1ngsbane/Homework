from functools import wraps
from datetime import datetime
from math import factorial
from random import randint


def save_logs(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        call_moment = datetime.now()
        func_name = func.__name__
        my_args = ''
        for element in args:
            my_args += str(element) + ' '
        for element in kwargs:
            my_args += str(element) + ' '
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as n:
            n.write('{}; {}; {}; {}.\n'.format(call_moment, func_name, my_args, result))

    return wrapper


@save_logs
def sum_nums(a, b):
    return a + b


@save_logs
def cube_volume(a):
    return a ** 3


@save_logs
def my_print(a):
    print(a)


@save_logs
def my_factorial(a):
    return factorial(a)


@save_logs
def my_randint(a, b):
    return randint(a, b)


sum_nums(12, 12)
cube_volume(777)
my_print('Hi there')
my_factorial(54)
my_randint(27, 54)
