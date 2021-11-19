
import platform
platform.python_reference  --> CPython

a = 1
b = a

sys.getrefcount(a) #2
del a
sys.getrefcount(a) #0 --> garbage collected. But no gc for inbuilt types

====================

import gc; 
gc.get_threshold ## Num of objs before which GC kicks in; default: (700, 10, 10) --> 700 for youngest generation gen0, 
                                                                                        gen1 = 10 and gen2 = 10

reval - read, evaluating

#import reval

>> gc.get_count() # current value = 667, 8, 9
>> gc.collect() # 0 
>> gc.get_count() # (4, 0, 0)

gc.set_threshold(1000, 15, 15)
gc.set_threshold(0, 0, 0) ### Disable GC!!! YOu can do gc.collect() manually in your code like Instagram did to get 10x efficiency


