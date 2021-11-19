from collections import namedtuple

## pip install pympler  -- installed it manually in Terminal
from pympler import asizeof  ### Python Memory Profiler

Point = namedtuple('Point', 'x y z')
# pt = Point(10, {'a': 20}, ['20', 'murthy'])
pt = Point(10, 20, 30)

print(pt.x)

### Run this in the Terminal manually

namedtuple_size = asizeof.asizeof(pt)
dict_size = asizeof.asizeof(pt._asdict())

gain = 100 - namedtuple_size/dict_size * 100

print(f'namedtuple:{namedtuple_size} bytes {gain:.2f}% smaller')
print(f'dict_size: {dict_size} bytes')

### Run this in the Terminal manually
### Hence, namedtuple takes much less space and super fast compared to dict!!!
### 70% more efficient than dicts! 