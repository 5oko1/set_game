from tkinter import Tk, Button, Frame, messagebox, StringVar, Label
from datetime import datetime
from cards import AllCards
import random


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
        if len(self.game.result) == 3:
            self.game.check_result()

    def switch_highlight(self):
        if not self.state:
            self['bg'] = 'green'
        else:
            self['bg'] = 'SystemButtonFace'
        self.state = not self.state

    def set_card(self, card):
        self.card = card
        self.change_img(card.card_image)

    def change_img(self, new_img):
        self.config(image=self.game.all_images[new_img])


class Interface:

    def __init__(self, game):
        self.game = game
        self.root = self.game.root = self.create_window()

        self.score_var = StringVar()
        self.score_var.set('0')

        self.timer_var = StringVar()
        self.timer_var.set('00:00')
        self.root.after(1000, self.update_timer)

        self.create_buttons()

    @staticmethod
    def create_window():

        root = Tk()
        root.title('Set Game')
        root.geometry('600x480')
        root.configure(background='light gray')
        return root

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
                             height=1, command=self.refresh)
        refresh_btn.pack()
        refresh_btn.place(x=400, y=40)

        help_btn = Button(self.root, text='Помощь', bd=4, width=10, height=1,
                          command=self.set_help)
        help_btn.pack()
        help_btn.place(x=400, y=80)

        timer = Label(self.root, textvariable=self.timer_var, background='light gray', font=('Arial', 18))
        timer.pack()
        timer.place(x=400, y=155)

        score_label = Label(self.root, text='Счёт:', background='light gray', font=('Arial', 18))
        score_label.pack()
        score_label.place(x=400, y=190)

        score_amount = Label(self.root, textvariable=self.score_var, background='light gray', font=('Arial', 18),
                             fg='blue')
        score_amount.pack()
        score_amount.place(x=420, y=220)

    def update_timer(self):

        current_time = datetime.now()
        difference = current_time - self.game.start_time
        diff_seconds = int(difference.total_seconds())
        self.game.session_time = f'{diff_seconds//60:0>2d}:{diff_seconds%60:0>2d}'
        if self.game.play:
            self.timer_var.set(self.game.session_time)
            self.root.after(1000, self.update_timer)

    def set_help(self):
        """Добавить подсветку существующего сета"""

        self.game.help_use = True
        self.cancel_help_highlight()
        for card_ind in random.choice(self.game.all_sets):
            self.game.all_buttons[card_ind]['bg'] = 'blue'

    def refresh(self):

        self.cancel_highlight()
        self.game.result = []
        AllCards(self.game).reshuffle()

    def cancel_highlight(self):
        """Убрать подсветку у всех кнопок"""

        for button in self.game.all_buttons:
            button['bg'] = 'SystemButtonFace'
            button.state = False

    def cancel_help_highlight(self):
        """Убрать подсветку у карт с обводкой помощи"""

        for button in self.game.all_buttons:
            if button['bg'] == 'blue':
                button['bg'] = 'SystemButtonFace'
                button.state = False

    def finish_message(self):

        messagebox.showinfo('Игра окончена', f'Поздравляю, вы смогли найти {self.game.score} сетов!\n'
                                             f'Ваше время составило {self.game.session_time}')
