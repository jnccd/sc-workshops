class Actor:
    def __init__(self, name, start_hp):
        self.name = name
        self.hp = start_hp
        self.damage = 2
    
    def hit(self, other_actor):
        other_actor.hp -= self.damage
        
def print_hp(actor1, actor2):
    print(actor1.name + ": " + str(actor1.hp))
    print(actor2.name + ": " + str(actor2.hp))


link = Actor("Link", 5)
bokoblin = Actor("Bokoblin", 10)


print_hp(link, bokoblin)

link.hit(bokoblin)

print_hp(link, bokoblin)