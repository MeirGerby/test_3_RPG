from players_status import PlayersStatus
from random import randint
class Orc(PlayersStatus):
    def __init__(self, name):
        super().__init__(name)
        self.mon_type = 'orc'
        self.weapon = None
        self.speed = randint(5, 10)
        self.power = randint(10, 15)
        self.hp = 50
        self.armor_rating = randint(2, 8)


    def speak(self):
        print(f"Monster: {self.name} Type: {self.mon_type} "
              f"very angry")

    def rand20(self):
        rand = randint(1, 20)
        rand += self.speed
        return rand

    def attack_type(self):
        attack_with = super().attack_type()
        return attack_with

    def calc_att(self, att_ty):
        val = super().calc_att(att_ty)
        num = self.rand20()
        return val * num

    def attack(self):
        attack_type = self.attack_type()
        calc = self.calc_att(attack_type)
        return [attack_type, calc]


    def speed(self):
        self.power = randint(0, 5)
