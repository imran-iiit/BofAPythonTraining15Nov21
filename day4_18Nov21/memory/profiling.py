import gc
# pip install memory-profiler

@profile # run below command in shell
def myfunc():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)

    del b
    gc.collect()

    return a

if __name__ == '__main__':
    myfunc()
    print('Done')

    ### RUN locally - python3 -m memory_profiler profiling.py
    ### ******* There is a MODULE level profiler as well!! pip3 install guppy  *********