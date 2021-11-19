
import threading, time

thread_lock = threading.Lock()

shared_data = {'balance': 5000}

def longRunningTask(): # upload, downloading, bulk emails, export, complex algos etc.
    # long task 
    x = 1
    print('complex task')
    while True:
        thread_lock.acquire()
        print('I am in child thread', x)
        x += 1
        time.sleep(1)
        thread_lock.release()
        if x == 5:
            break

if __name__ == '__main__':
    thread_obj = threading.Thread(target=longRunningTask) ### can pass arguments as well
    thread_obj.start() ## two trains running parallelly but with ROUND ROBIN Algo
    print('Doing something else')
    thread_obj.join()
    print('All done')


