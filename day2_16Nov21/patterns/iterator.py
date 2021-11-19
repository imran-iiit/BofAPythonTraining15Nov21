### Behavioral Pattern

nums = [1,2 ,3, 4]

# for n in nums: #iterator internally
#     print(n)

it = iter(nums)
print(type(it))
print(it.__next__()) #1
print(it.__next__()) #2
print(next(it)) #3
print(next(it)) #4
# print(next(it)) # Exception

### Implement smth like df.head(n=5) which returns top n records
# Custom iterator
class Head: # make this iterable
    def __init__(self, max=5) -> None:
        self.num = 1
        self.max = max

    def __iter__(self):
        return self ### IMPORTANT
    
    def __next__(self):
        if self.num <= self.max:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Head()
print(values.__next__()) #1
print(values.__next__()) #2
print(values.__next__()) #3
print(values.__next__()) #4
print(values.__next__()) #5
# print(values.__next__()) # exception

values = Head()
for v in values:
    print(v)