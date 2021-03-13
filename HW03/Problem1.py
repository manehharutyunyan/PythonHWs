class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        
    def compareCar(self, car2): 
        if self.max_speed > car2.max_speed:
            print('car1 is better than car2')
        else:
            print('car2 is better than car1')
            
car1 = Car('BMW', 'Black', 64)
car2 = Car('Toyota', 'Red', 164)

car1.compareCar(car2)