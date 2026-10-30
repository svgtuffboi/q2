class Vehicle:
    color = "gray"
    def __init__(self,name,passengers):
        self.name = name
        self.passengers = passengers
    def move(self):
        print("the Vehicle",self.color,name,"is moving")
        print("It has",self.passengers,"passengers")
        
class Car(Vehicle):
    def move(self):
        print("the Car",self.color,self.name,"is travelling along the road.")
        print("It has",self.passengers,"passengers")
        
class Boat(Vehicle):
    def move(self):
        print("the Boat",self.color,self.name,"sailing across the seas")
        print("It has",self.passengers,"passengers")
        
class Skateboard:
    def move(self):
        print("The skateboard is skating in the skatepark")
    
car1 = Car("Toyota Altis",5)
car1.color = "Red"

car2 = Car("BYD Sealion 5",2130)
car2.color = "blue"

boat = Boat("yacht",10)
boat.color = "white"

skbd = Skateboard()

vehicles = [car1,car2,boat,skbd]
for v in vehicles:
    v.move()
