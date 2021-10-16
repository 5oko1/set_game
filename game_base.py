from cards import GameSet, AllCards
from card_button import Interface
from set_cards.cards_pic import Images
import pygame


class GameBase:

    def __init__(self):
        """Инициализируем основные компоненты игры и создаём окно интерфейса"""

        self.open_cards = [0, 0, 0, 0,
                           0, 0, 0, 0,
                           0, 0, 0, 0]
        self.result = []
        self.all_buttons = []
        self.root = None
        self.all_sets = []

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
            self.all_cards.delete_cards_on_table(*self.result)
            if self.all_cards.open_new_cards() == 'Finish':
                self.end_game()
                return
        else:
            print('Ошибка!')
            self.wrong.play()

        self.interface.cancel_highlight()
        self.result = []

    def end_game(self):
        self.interface.finish_message()
        self.root.destroy()
