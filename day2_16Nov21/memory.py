import random, time, os, gc
import psutil ### Memory profiler

names = ['A', 'B', 'C', 'D', 'E']
majors = ['Maths', 'Arts', 'MBA', 'CSC']

def people_list(num_people):
    result = []

    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                 }
        result.append(person)

    return result

def people_generator(num_people):

    for i in range(num_people):
        yield    {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                 }


# t1 = time.process_time()
# people = people_list(100000)
# t2 = time.process_time()
# print(f'Time taken for list: {t2-t1} seconds')
# print(psutil.Process(os.getpid()).memory_info()) # memory consumed:
                                                     # - vms (Virtual Memory System)
                                                     # = 121Mb

# ### run manually --> $ python3 memory.py 
# '''
# For LIST:
# aniron@Imrans-MacBook-Air:~/Documents/BofA_Python_Training_15Nov21/day2$ python3 memory.py 
# Time taken for list: 0.330578 seconds
# pmem(rss=42070016, vms=121860096, pfaults=11307, pageins=735)
# '''

t1 = time.process_time()
people = people_generator(100000)
t2 = time.process_time()
print(f'Time taken for list: {t2-t1} seconds')
print(psutil.Process(os.getpid()).memory_info()) # memory consumed = 93Mb only!!

'''
For Generator implementation:
aniron@Imrans-MacBook-Air:~/Documents/BofA_Python_Training_15Nov21/day2$ python3 memory.py 
Time taken for list: 5.0000000000050004e-06 seconds
pmem(rss=13922304, vms=93495296, pfaults=4121, pageins=735)
'''

#### GC
del people
gc.collect()

t1 = time.process_time()
people = people_generator(10000000)
t2 = time.process_time()
print(f'Time taken for list: {t2-t1} seconds') ## This runs much faster! 
print(psutil.Process(os.getpid()).memory_info()) # memory consumed same = 93Mb

'''
aniron@Imrans-MacBook-Air:~/Documents/BofA_Python_Training_15Nov21/day2$ python3 memory.py 
Time taken for list: 5.0000000000050004e-06 seconds
pmem(rss=13983744, vms=93495296, pfaults=4133, pageins=735)
Time taken for list: 1.6999999999989246e-05 seconds
pmem(rss=13983744, vms=93495296, pfaults=4133, pageins=735)
'''