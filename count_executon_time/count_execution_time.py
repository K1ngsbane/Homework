from timeit import timeit


def count_time(func):

    def time():
        print(timeit(func))
    return time


@count_time
def test():
    n = 123
    return n


test()
