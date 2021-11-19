### Structural Design Pattern

### AOP - Aspect Oriented Programming - aspects = behaviours i.e. logging, 
###         security, caching, profiling 

'''
    Decorator - Attaching additional behaviour/responsibilities to the function/method
                at runtime (composition - loosely coupled architecture)
'''

def say_hello(name):
    return f'Hello {name}!'

def appreciate(name):
    return f'You are great {name}!!'

def greet(fptr): # Higher order function - Decorator
    '''
        you can additionally do - logging/profiling/check roles/caching etc. here
    '''
    return fptr('Imran')

print(greet(say_hello))

##############################################

def logger(func):
    def wrapper():
        print(f'about to call {func}')
        func()
        print(f'Called {func}')

    return wrapper

@logger
def invoke():
    print('Welcome to BofA')

invoke()