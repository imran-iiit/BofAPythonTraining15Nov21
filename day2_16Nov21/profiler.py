import time
# from typing_extensions import runtime


def profile(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Num times: {args[0]}')

        runtime = end_time - start_time
        print(f'Finished {func.__name__} in {runtime:.4} secs')

        return value
    
    return wrapper_timer


@profile
def task(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

task(999)