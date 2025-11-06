from game import Game

if __name__ == "__main__":
    Game.start()
    Game.show_menu()
    player = Game.create_player()
    monster = Game.choose_random_monster()
    p_roll = Game.roll_dice(6)
    m_roll = Game.roll_dice(6)
    p_roll += player.speed
    m_roll += monster.speed
    play = True
    while play:
        if m_roll > p_roll:
            win = Game.battle(player, monster, p_roll, m_roll)
            if player.hp <= 0:
                break
            while win:
                win = Game.battle(player, monster, p_roll, m_roll)
                if player.hp <= 0:
                    break

        elif p_roll > m_roll or p_roll == m_roll:
            win = Game.battle(player, monster, p_roll, m_roll)
            if monster.hp <= 0:
                break
            while win:
                win = Game.battle(player, monster, p_roll, m_roll)
                if monster.hp <= 0:
                    break




