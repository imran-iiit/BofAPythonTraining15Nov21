"""
#singleton
'''
single global access point should be created
give same reference 
DBConnection,HttpCache,API Gateway,SecurityProxy (SSO token)
config,logger

Singleton : name,intent,motivate,class diagram, pariticipant,example,pros /cons
related patterns (factory)

threadpool,objectpool,connectionpool

shareddata(global data) 10 - lock/semaphore
"""

class BankSingleton:
    __instance__ = None ### Apparently this is a "global" variable not an attribute

    def __init__(self) -> None:
        if BankSingleton.__instance__ is None:
            BankSingleton.__instance__ = self
        else:
            raise Exception('Instance is already running!!')
    
    @staticmethod
    def get_instance():
        if not BankSingleton.__instance__:
            BankSingleton()
        
        return BankSingleton.__instance__


# b1 = BankSingleton()
# print(b1)
# b2 = BankSingleton() ## throws

# Method 2
b1 = BankSingleton.get_instance()
b2 = BankSingleton.get_instance()
assert id(b1) == id(b2)
print(b2)
print(BankSingleton.__instance__)