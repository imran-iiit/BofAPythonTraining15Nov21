class Student(object):
    def __init__(self, id, name, city) -> None:
        super().__init__()
        self.id = id # Public
        self.name = name
        self.city = city

s1 = Student(101, 'Imran', 'Hyderabad ')
print(s1.city)

# to encapsulate the data, we cannot allow others to do this
s1.id = 1232
print(s1.id)

class Student1(object):
    def __init__(self, id, name, city) -> None:
        super().__init__()
        self.__id = id # Private - encapsulation!!
        self.__name = name
        self.__city = city

    def getID(self):
        return self.__id

    @property # Data Encapsulation - 
    def getCity(self):
        return self.__city

s2 = Student1(123, 'Imran', 'Hyderabad')
# Anti-pattern! Always have specific getters/setters with private attributes
# print(s2.__id) ###Error - AttributeError: 'Student1' object has no attribute '__id'
print(s2.getID())
s2.__id = 123232  ### It is going to add a new __id attribute with this line which 
print(s2.__id)   ### gets printed here! Not the actual attribute from the class

