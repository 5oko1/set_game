from cards import GameSet, AllCards
from card_button import Interface
from set_cards.cards_pic import Images
import pygame


class GameBase:

    def __init__(self):
        """Инициализируем основные компоненты игры и создаём окно интерфейса"""

        self.sequence = []
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

    def check_result(self):

        if len(self.result) == 3:

            if GameSet().check_set(*self.result):
                print('Верно!')
                self.correct.play()
                self.all_cards.delete_cards_on_table(*self.result)
                self.all_cards.fill_open_cards()
                # Доработать! В конце игры зациклится
                while not self.all_cards.game.all_sets:
                    self.all_cards.reshafle()
            else:
                print('Ошибка!')
                self.wrong.play()

            self.interface.cancel_highlight()
            self.result = []
