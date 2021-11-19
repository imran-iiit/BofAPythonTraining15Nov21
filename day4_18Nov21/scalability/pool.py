import multiprocessing, os

def square(n):
    print(f'Worker process {n} with PID = {os.getpid()}') ### 4 PIDs to process 6 numbers! Really good
                                                ### for data analysis! NICE!!!
    return n * n

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6]

    p = multiprocessing.Pool()
    result = p.map(square, my_list)
    print('In main process: ', result) 