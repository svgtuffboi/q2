
class Warrior():
    def special_move(self):
        print("The Warrior swings a mighty sword!")

    
        
class Mage():
    def special_move(self):
        print("The Mage casts a powerful spell!")


class Archer():
    def special_move(self):
        print("The Archer shoots a precise arrow!")
        
def perform_move(character):
    character.special_move()
    
warrior = Warrior()
archer = Archer()
mage = Mage()
character = [warrior,mage,archer]

for v in character:
    perform_move(v)