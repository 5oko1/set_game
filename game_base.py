from cards import GameSet, AllCards
from card_button import AllButtons
import pygame


class GameBase:
    sequence = []
    open_cards = [0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0]
    result = []
    all_buttons = []
    all_images = dict
    root = None
    all_sets = []
    pygame.mixer.init()
    correct = pygame.mixer.Sound("audio/correct.wav")
    wrong = pygame.mixer.Sound("audio/mistake.wav")

    def check_result(self):

        if len(self.result) == 3:
            all_cards = AllCards(self)
            if GameSet().check_set(*self.result):
                print('Верно!')
                self.correct.play()
                all_cards.delete_cards_on_table(*self.result)
                all_cards.fill_open_cards()
                AllCards(self).get_card_info()
            else:
                print('Ошибка!')
                self.wrong.play()
                
            AllButtons(self, self.root).cancel_highlight()
            self.result = []
