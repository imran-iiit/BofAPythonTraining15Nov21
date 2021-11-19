### Any anonymous function like expression without statements = lambdas
### Lamdbdas are single line functions
### Prefer to pass function as a parameter to another function

def add5(x):
    return x + 5

add5_l = lambda x: x + 5
print(add5_l(10))

#Interceptor/Broker
def do_something(f, val): # "Higher Order Function"/"Pure Function" 
                          #  - function that takes a function and does something on it
    return f(val)

func = lambda x: x + 1
print(func(10))

print(do_something(func, 50))

starts_with_M = lambda x: True if x.startswith('M') else False
print(starts_with_M('Murthy'))

list1 = [('eggs', 5.45), ('honey', 8.75), ('carrots', 2.35)]
list1.sort(key=lambda x:x[0], reverse=False)
print(list1)