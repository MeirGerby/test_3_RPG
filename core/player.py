from players_status import PlayersStatus
from random import randint

class Player(PlayersStatus):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession
        self.power = randint(5, 10)
        self.speed = randint(5, 10)
        self.hp = 50





    def speak(self):
        print(f'my name: {self.name} '
              f'hello for every one')

    def attack(self):
        rand = randint(1, 20)
        rand += self.speed
        return rand



