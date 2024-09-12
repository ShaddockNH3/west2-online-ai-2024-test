import time

def time_test(func):
    def f():
        print(func.__name__)
        start_time=time.perf_counter()
        func()
        end_time=time.perf_counter()
        print(end_time-start_time)
    return f


@time_test
def test():
    return

test()