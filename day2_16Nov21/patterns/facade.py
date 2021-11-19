### Inheritance v/s Composition

"""
    Facade is single, unified interface which hides complex 
    subsystems/modules from clients

    ex: API Gateway (facade, singleton)
"""

''' 
Facade is single, unified interface which hides
complex subsystems/modules from client

Ex. API Gateway (facade/singleton)
'''
#facade pattern for Ordering Pizza
class Ordering:
    #subsystem1 / Module1  order.py
    def order(self):
        #write the business logic
        print("Order received.......")
    
    def cancelOrder(self):
        print("Order cancelled")


class Preparing:
    #subsystem2 / Module2  prepare.py
    def prepare(self):
        #write the business logic
        print("preparing food.....")


class Delivering:
    #subsystem3 / Module3   deliver.py
    def deliver(self):
        #write the business logic
        print("Delevering food.....")


#facade
class Operator:
    def __init__(self):
        self.ordering=Ordering() # composition
        self.preparing=Preparing() # composition
        self.delivering=Delivering() # composition

    def placeOrder(self):
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()

    
if __name__ == "__main__":
    op=Operator()
    op.placeOrder()
    print("Enjoy your food.............")


    
