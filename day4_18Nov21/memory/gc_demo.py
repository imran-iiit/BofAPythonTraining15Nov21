### REFERENCE CYCLE: 

import gc, sys

# Anti pattern
def create_cycle():
    lst = [1, 2, 3, 4]
    lst.append(lst)

def no_cycle(mylist):
    mylist.append(mylist)
    print(mylist)

def main():
    print('Creating some garbage')
    my_list = [1, 2, 3, 4]
    for i in range(8):
        # create_cycle()
        no_cycle(my_list)

    print('Before gc, ref_count = ', gc.get_count())
    print('Collecting now')
    n = gc.collect()
    print('Num of unreachable objs collected by GC = ', n)
    print('Uncollected garbage = ', gc.garbage)
    print('After GC, ref_count = ', gc.get_count())

if __name__ == '__main__':
    main()
    print('Done')