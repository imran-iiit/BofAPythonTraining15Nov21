import multiprocessing

def insert_record(record, records):
    # write db logic here
    records.append(record)
    # print('New record added --> ', records)

def print_records(records):
    print('Records:')
    for r in records:
        print(f'{r[0]} - {r[1]}')

if __name__ == '__main__':
    with multiprocessing.Manager() as manager: # responsible for maintaining shared data
        records = manager.list([('Imran', 1), ('Murthy', 2), ('asdf', 0)]) # shared data under the control 
                                        #   of server proc = manager. This can have any DS in the list
        new_record = ('Mallika', 8)

        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()
        print('Main process...')
        p2.start()
        p2.join()
        print('All work done!')
