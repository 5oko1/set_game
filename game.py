from game_base import GameBase
from cards import AllCards


def new_game():
    game_base = GameBase()

    all_cards = AllCards(game_base)
    all_cards.generate_new_sequence()
    all_cards.fill_open_cards()

    game_base.root.mainloop()


if __name__ == '__main__':
    new_game()
