from random import randint
class PlayersStatus:
    def __init__(self,name):
        self.name = name
        self.armor_rating = 0






    def attack_type(self):
        rand = randint(1,3)
        attack_with = None
        if rand == 1:
            attack_with = 'knife'
        elif rand == 2:
            attack_with = 'sword'
        elif rand == 3:
            attack_with = 'ax'
        return attack_with

    def calc_att(self, att_ty):

        if att_ty == 'knife':
            return 0.5
        elif att_ty == 'sword':
            return 1
        elif att_ty == 'ax':
            return 1.5
        else:
            return None

