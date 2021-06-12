from game_base import GameBase
from cards import AllCards
from tkinter import Tk
from card_button import AllButtons
from set_cards.cards_pic import Images


root = Tk()
root.title('Set Game')
root.geometry('600x480')
root.configure(background='light gray')

game_base = GameBase()
game_base.root = root
Images(game_base).get_images()
all_buttons = AllButtons(game_base, root)
all_buttons.create_buttons()
all_cards = AllCards(game_base)
all_cards.generate_new_sequence()
all_cards.fill_open_cards()
all_cards.get_card_info()

root.mainloop()
