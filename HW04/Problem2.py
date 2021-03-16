class My_Time:
    def __init__(self, t):
        self.t = t
        
    def printTime(self):
            print("The current time is {}.".format(self.t))
            
class My_Date:
    def __init__(self, d):
        self.d = d
        
    def printDate(self):
        print('The Current Date Is {}'.format(self.d))
        
class Date_Time(My_Time, My_Date):
    def __init__(self, t, d):
        My_Time.__init__(self, t)
        My_Date.__init__(self, d)
        
d = Date_Time('12 PM', '13.03.2013')
d.printDate()
d.printDate()
print(d.t)