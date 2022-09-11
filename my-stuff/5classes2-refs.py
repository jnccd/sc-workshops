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


link = Actor("Link", 10)
blin = Actor("Blin", 5)


print_hp(link, blin)

link.hit(blin)

print_hp(link, blin)

link2 = link
link2.name = "Zelda"

print_hp(link, link2)