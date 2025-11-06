from random import randint

from core.player import Player
from core.orc import Orc
from core.goblin import Goblin





class Game:
    @staticmethod
    def start():
        print("start the game")

    @staticmethod
    def show_menu():
        print('this is a buttle game')

    @staticmethod
    def create_player():
        rand = randint(1,2)
        if rand == 1:
            return  Player('Meir', 'fighter')
        elif rand == 2:
            return  Player("Meir", "cure")
        else:
            return None

    @staticmethod
    def choose_random_monster():

        rand = randint(1,2)
        if rand == 1:
            return Orc('orc')
        elif rand == 2:
            return Goblin('monster')
        return None

    @staticmethod
    def roll_dice(sides):
        rand6 = randint(1, 6)
        rand20 = randint(1, 20)
        if sides == 6:
            return rand6
        elif sides == 20:
            return rand20
        else:
            return None

    @staticmethod
    def battle(player, monster, p1_roll, m1_roll):


        if m1_roll > p1_roll:
            if monster.armor_rating > player.armor_rating:
                print('success')
                damage = monster.roll_dice(6)
                player.hp -= damage
                return True
            else:
                print('fail')
                return False
        else:
            player.attack()
            if player.armor_rating > monster.armor_rating:
                print('success')
                damage = player.roll_dice(6)
                monster.hp -= damage
                return True
            else:
                print("fail")
                return False



