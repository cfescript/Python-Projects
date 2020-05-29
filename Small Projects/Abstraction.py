from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self):
        self.SwordDurability = 100
    @abstractmethod
    def Attack(self, uses):
        pass

class Controller(Player):
    def Attack(self, uses):
        self.SwordDurability -= uses
        print('Your sword has {} hits remaining and Aim Assist was applied'.format(self.SwordDurability))

class Mouse(Player):
    def Attack(self, uses):
        self.SwordDurability -= uses
        print('Your sword has {} hits remaining'.format(self.SwordDurability))


p1 = Controller()
p2 = Mouse()

p1.Attack(3)
p2.Attack(1)
