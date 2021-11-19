import multiprocessing

result = []

# Child process
### As it is a PROCESS and not a Thread, DONT return any value (as process 
###      doesnt share memory)
def square_list(my_list):
    global result

    for num in my_list:
        result.append(num*num)
    
    print('Result of child 1 --> ', result)

def square_list_shared(my_list, result, square_sum):
    for idx, num in enumerate(my_list):
        result[idx] = num * num

    square_sum.value = sum(result)
        
    print('Shared child result -->: ', result[:])
    print('Shared child sum of squares --> ', square_sum.value)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6]

    p1 = multiprocessing.Process(target=square_list, args=(my_list, )) ### NOTE - , 
                                                            ### in args as we need to pass tuple
    p1.start()
    


    """
        'Shared Containers' ('Values' and 'Arrays' multi-container ) to share data 
            between processes

    """    
    square_sum = multiprocessing.Value('i') # i = Int Container!
    result = multiprocessing.Array('i', len(my_list))  # Int Array Container of size 4

    p2 = multiprocessing.Process(target=square_list_shared, args=(my_list, result, square_sum))
    p2.start()

    print('Main process doing smth')
    p1.join()
    p2.join()
    print('Result of main process', result[:]) # Nothin printed here as result is still []
                                        # as this is a different mem space than chile proc

