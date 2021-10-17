from cards import GameSet, AllCards
from card_button import Interface
from set_cards.cards_pic import Images
from datetime import datetime
import pygame


class GameBase:

    def __init__(self):
        """Инициализируем основные компоненты игры и создаём окно интерфейса"""

        self.play = True
        self.open_cards = [0, 0, 0, 0,
                           0, 0, 0, 0,
                           0, 0, 0, 0]

        self.start_time = datetime.now()
        self.result = []
        self.all_buttons = []
        self.root = None
        self.all_sets = []
        self.score = 0
        self.help_use = False

        pygame.mixer.init()
        self.correct = pygame.mixer.Sound("audio/correct.wav")
        self.wrong = pygame.mixer.Sound("audio/mistake.wav")

        self.interface = Interface(self)
        self.all_images = Images().get_images()
        self.all_cards = AllCards(self)
        self.sequence = self.all_cards.generate_new_sequence()

    def check_result(self):

        if GameSet().check_set(*self.result):
            print('Верно!')
            self.correct.play()
            self.raise_score()
            self.all_cards.delete_cards_on_table(*self.result)
            if self.all_cards.open_new_cards() == 'Finish':
                self.play = False
                self.end_game()
                return
        else:
            print('Ошибка!')
            self.wrong.play()

        self.interface.cancel_highlight()
        self.result = []

    def raise_score(self):

        if not self.help_use:
            self.score += 1
            self.interface.score_var.set(str(self.score))
        self.help_use = False

    def end_game(self):
        self.interface.finish_message()
        self.root.destroy()
