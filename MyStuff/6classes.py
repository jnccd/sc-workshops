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


link = Actor("Link", 5)
bokoblin = Actor("Bokoblin", 10)


print_hp(link, bokoblin)

link.hit(bokoblin)

print_hp(link, bokoblin)