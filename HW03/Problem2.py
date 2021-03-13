import datetime

class Person:
    
    def __init__(self, name, last_name, age, gender, student, password): 
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
        
    def Greeting(self, second_person):
        print('Welcome dear ' + second_person.name)
        
    def Goodbye(self):
        return 'Bye everyone!'
        
    def Favourite_num(self, num1):
        return 'My favourite number is ' + str(num1)
        
    def Read_file(self, filename):
        filename = filename + '.txt'
        f = open(filename, "r")
        print(f.read())
    
    def get_pass(self):
        return self.__password

    @getTime
    def set_pass(self, password):
        self.__password = password
        
    def getTime(func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            func(*args, **kwargs)
            end = datetime.datetime.now()
            print(end - start)
        return wrapper

p1 = Person('Ann', 'Smith', 16, 'female', True, 'pass1234')
p2 = Person('Bob', 'Smith', 15, 'male', True, 'pass1234')
p1.Greeting(p2)
print(p1.Goodbye())
print(p1.Favourite_num(4))
p1.get_pass()
p1.set_pass('1234pass')
p1.get_pass()
p1.Read_file('test')

