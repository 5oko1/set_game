import random
import itertools


class Card:
    def __init__(self, color, shape, fill, amount):
        self.color = color
        self.shape = shape
        self.fill = fill
        self.amount = amount
        self.position = None
        self.card_image = f'{amount}{color[0]}{shape[0]}{fill[0]}'

    def __str__(self):
        return f'{self.color}, {self.shape}, {self.fill}, {self.amount}'


class GameSet:
    def check_param(self, card_a_param, card_b_param, card_c_param):
        """Проверяет параметр у каждой из карт
        :return: True если у карт параметр либо одинаковый, либо отличается
        """

        return card_a_param == card_b_param == card_c_param or \
            card_a_param != card_b_param != card_c_param != card_a_param

    def check_set(self, card_a, card_b, card_c):

        return self.check_param(card_a.color, card_b.color, card_c.color) and \
                self.check_param(card_a.shape, card_b.shape, card_c.shape) and\
                self.check_param(card_a.fill, card_b.fill, card_c.fill) and \
                self.check_param(card_a.amount, card_b.amount, card_c.amount)


class AllCards:
    def __init__(self, game):
        self.game = game

    def generate_new_sequence(self):
        """Возвращает последовательность из всех карт в колоде"""

        for color in 'red', 'green', 'blue':
            for shape in 'circle', 'square', 'wave':
                for fill in 'empty', 'strip', 'fill':
                    for amount in 1, 2, 3:
                        self.game.sequence.append(Card(color, shape,
                                                       fill, amount))

    def get_next_card(self):
        """Забирает случайную карту из колоды"""

        random_card_ind = random.randint(0, len(self.game.sequence)-1)
        return self.game.sequence.pop(random_card_ind)

    def fill_open_cards(self):
        """Выложить открытые карты"""

        for card_ind in range(12):
            if self.game.open_cards[card_ind] == 0:
                card = self.get_next_card()
                card.position = card_ind
                self.game.open_cards[card_ind] = card

        #Доработать! В конце игры зациклится
        while not self.find_solutions():
            self.reshafle()
        self.get_card_info()

    def reshafle(self):

        self.game.sequence = list(itertools.chain(self.game.sequence,
                                                  self.game.open_cards))
        self.game.open_cards = [0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0]
        self.fill_open_cards()

    def find_solutions(self):

        game_set = GameSet()
        self.game.all_sets = []

        for first_card_ind in range(11):
            for second_card_ind in range(first_card_ind+1, 12):
                for third_card_ind in range(second_card_ind+1, 12):
                    if game_set.check_set(self.game.open_cards[first_card_ind],
                                          self.game.open_cards[second_card_ind],
                                          self.game.open_cards[third_card_ind]):
                        print('Сет найден: ', first_card_ind, second_card_ind,
                              third_card_ind)
                        self.game.all_sets.append((first_card_ind, second_card_ind,
                              third_card_ind))

        return bool(self.game.all_sets)

    def delete_cards_on_table(self, *cards):
        """Убрать карты в сброс"""

        for card in cards:
            card_index = self.game.open_cards.index(card)
            self.game.open_cards[card_index] = 0

    def get_card_info(self):
        for card_ind in range(12):
            card_on_position = self.game.open_cards[card_ind]
            button = self.game.all_buttons[card_ind]
            button.set_card(card_on_position)
