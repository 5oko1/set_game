from game_base import GameBase


def new_game():

    game_base = GameBase()
    game_base.all_cards.open_new_cards()
    game_base.root.mainloop()


if __name__ == '__main__':
    new_game()
