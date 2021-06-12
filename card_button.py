from tkinter import Button, Frame
from cards import AllCards


class CardButton(Button):
    def __init__(self, game, **kwargs):
        super().__init__(command=self.click, **kwargs)
        self.game = game
        self.state = False
        self.card = None
        self.all_cards = AllCards(game)

        self.pack(side='left', padx=10, pady=10)

    def click(self):
        self.switch_highlight()
        if self.card not in self.game.result:
            self.game.result.append(self.card)
        else:
            self.game.result.remove(self.card)
        print(*self.game.result)
        self.game.check_result()

    def switch_highlight(self):
        if not self.state:
            self['bg'] = 'green'
        else:
            self['bg'] = 'SystemButtonFace'
        self.state = not self.state

    def highlight_error(self):
        self['bg'] = 'SystemButtonFace'
        self['bg'] = 'red'

    def set_card(self, card):
        self.card = card
        self.change_img(card.card_image)

    def change_img(self, new_img):
        self.config(image=self.game.all_images[new_img])


class AllButtons():

    def __init__(self, game, root):
        self.game = game
        self.root = root
        self.all_cards = AllCards(self.game)

    def create_buttons(self):

        top_frame = Frame(self.root)
        top_frame.pack()
        top_frame.place(x=30, y=30)
        top_frame.configure(background='light gray')

        mid_frame = Frame(self.root)
        mid_frame.pack()
        mid_frame.place(x=30, y=150)
        mid_frame.configure(background='light gray')

        bot_frame = Frame(self.root)
        bot_frame.pack()
        bot_frame.place(x=30, y=270)
        bot_frame.configure(background='light gray')

        for frame in top_frame, mid_frame, bot_frame:
            for i in range(4):
                self.game.all_buttons.append(CardButton(game=self.game,
                                                        master=frame, bd=4))

        refresh_btn = Button(self.root, text='Обновить', bd=4, width=10,
                             height=1, command=self.all_cards.reshafle)
        refresh_btn.pack()
        refresh_btn.place(x=400, y=40)

        help_btn = Button(self.root, text='Помощь', bd=4, width=10, height=1,
                          command=self.set_help)
        help_btn.pack()
        help_btn.place(x=400, y=80)
    
    def set_help(self):
        """Добавить подсветку существующего сета"""

        for card_ind in self.game.all_sets[0]:
            self.game.all_buttons[card_ind]['bg'] = 'blue'

    def cancel_highlight(self):
        """Убрать подсветку у всех кнопок"""

        for button in self.game.all_buttons:
            button['bg'] = 'SystemButtonFace'
            button.state = False


