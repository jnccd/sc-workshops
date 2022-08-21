class Actor:
    def __init__(self, name, start_hp):
        self.name = name
        self.hp = start_hp
        self.damage = 2
    
    def hit(self, other_enemy):
        other_enemy.hp -= self.damage
        
def print_hp(enemy1, enemy2):
    print(enemy1.name + ": " + str(enemy1.hp))
    print(enemy2.name + ": " + str(enemy2.hp))


albert = Actor("Albert", 5)
gandalf = Actor("Gandalf", 10)


print_hp(albert, gandalf)

gandalf.hit(albert)

print_hp(albert, gandalf)