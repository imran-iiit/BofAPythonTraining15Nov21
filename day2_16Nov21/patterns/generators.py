
def square_numbers(nums): # Returns only after completing everything
    result = []
    for i in nums:
        result.append(i*i)

    return result

def square_numbers_efficient(nums):
    for i in nums:
        yield(i*i) # stops here to return this


my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

arr = [1, 2, 3, 4, 5]
print(type(square_numbers_efficient(arr)))
my_nums = square_numbers_efficient(arr)
print(next(my_nums)) #1
print(next(my_nums)) #2*2
print(next(my_nums)) #3*3


### Custom generator - shows generator internally uses next()
def top_five():
    n = 1
    while n <= 5:
        sq = n * n
        yield sq
        n += 1

values = top_five()  ## hovering over values --> shows it is a generator
for i in values:
    print(i)



