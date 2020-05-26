



class NPC:
    name = "NPC"
    health = 20
    damage = 5

    def onAttack(self, attackDmg):
        self.health -= attackDmg
        print("The {} has taken {} damage!".format(self.name, attackDmg))
        if self.health <= 0:
            self.onDeath()
        else:
            print("It has {} health remaining.".format(self.health))

    def onDeath(self):
        print("The {} has died!".format(self.name))
            

class Friendly(NPC):
    name = "Villager"
    model = "villager_forrest"
    inventory = ["Gold", 6, "Bread", 1]

    def onAttack(self, attackDmg):
        self.health -= attackDmg
        print("The {} has taken {} damage!".format(self.name, attackDmg))
        if self.health <= 0:
            self.onDeath()
        else:
            print("It has {} health remaining and is now running away.".format(self.health))

    def onDeath(self):
        print("The {} has died!".format(self.name))
        # Fake TODO: add for loop to add inventory stuff to this message
        print("You have gained {} {} and {} {}".format(self.inventory[1], self.inventory[0], self.inventory[3], self.inventory[2]))


class Enemy(NPC):
    name = "Zombie"
    enemyType = "Crawler"
    inventory = ["Rotten Flesh", 2]

    def onAttack(self, attackDmg):
        self.health -= attackDmg
        print("The {} has taken {} damage!".format(self.name, attackDmg))
        if self.health <= 0:
            self.onDeath()
        else:
            print("It has {} health remaining and is now attacking you!".format(self.health))
            print("You have taken {} damage!".format(self.damage))

    def onDeath(self):
        print("The {} has died!".format(self.name))
        # Fake TODO: add for loop to add inventory stuff to this message
        print("You have gained {} {}".format(self.inventory[1], self.inventory[0]))


NPC1 = Enemy()
NPC2 = Friendly()

NPC1.onAttack(10)
NPC2.onAttack(10)
NPC2.onAttack(10)
