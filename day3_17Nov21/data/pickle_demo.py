"""
    Pickling/serialization/marshalling is used to improve the performance 
    of data oriented modules

    convert list, dict, tuple, sets ---> byte streams (0s and 1s) - binary data

    Difference b/w pickling and serialization is, pickle is always in binary format 
    whereas serialization can be to files etc.

    Pros:
    - very performant - less size (almost halved)
    - easy to code
    - pickled file in binary format not readable - secure - "binary data secured" WTF!

    Cons:
    - other languages cannot reconstruct pickled python objects
"""

import pickle, requests, json

FOLDER = '/Users/aniron/Documents/BofA_Python_Training_15Nov21/day3/data/'

emps = {'a': 1, 'b': 2}

with open(FOLDER+'emp.pickle', 'wb') as pkl_on:
    pickle.dump(emps, pkl_on)
    print('pickled')

with open(FOLDER+'emp.pickle', 'rb') as pkl_off:
    data = pickle.load(pkl_off)
    print('unpickled: ', data)

response = requests.get("https://jsonplaceholder.typicode.com/todos", verify=False)
todos = json.loads(response.text)


with open(FOLDER+'data.pk', 'wb') as pkl_on:
    pickle.dump(todos, pkl_on)
    print("Pickling done...")

with open(FOLDER+'data.pk', 'rb') as pkl_off:
    data = pickle.load(pkl_off)
    print(data)