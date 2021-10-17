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


class NoCard:
    def __init__(self):
        self.card_image = 'no_img'


class GameSet:

    @staticmethod
    def check_param(card_a_param, card_b_param, card_c_param):
        """Проверяет параметр у каждой из карт
        :return: True если у карт параметр либо одинаковый, либо отличается
        """

        return card_a_param == card_b_param == card_c_param or \
            card_a_param != card_b_param != card_c_param != card_a_param

    def check_set(self, card_a, card_b, card_c):
        """Проверяет корректность сета"""

        if isinstance(card_a, Card) and isinstance(card_b, Card) and \
         isinstance(card_c, Card):
            return self.check_param(card_a.color, card_b.color, card_c.color) and \
                    self.check_param(card_a.shape, card_b.shape, card_c.shape) and\
                    self.check_param(card_a.fill, card_b.fill, card_c.fill) and \
                    self.check_param(card_a.amount, card_b.amount, card_c.amount)
        else:
            return False


class AllCards:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def generate_new_sequence():
        """Возвращает случайную последовательность из всех карт в колоде"""

        sequence = []

        for color in 'red', 'green', 'blue':
            for shape in 'circle', 'square', 'wave':
                for fill in 'empty', 'strip', 'fill':
                    for amount in 1, 2, 3:
                        sequence.append(Card(color, shape, fill, amount))

        random.shuffle(sequence)
        return sequence

    def get_next_card(self):
        """Забирает карту из колоды"""

        if len(self.game.sequence) > 0:
            return self.game.sequence.pop()
        else:
            return NoCard()

    def fill_open_cards(self):
        """Выложить открытые карты"""

        for card_ind in range(12):
            if self.game.open_cards[card_ind] == 0:
                card = self.get_next_card()
                self.game.open_cards[card_ind] = card

    def reshuffle(self):
        """Перемешать карты. Метод для интерфейсного вызова игроком через кнопку"""

        self.game.help_use = False
        self.put_cards_into_deck()
        self.open_new_cards()

    def put_cards_into_deck(self):
        """Убрать карты в колоду"""

        self.game.sequence = list(itertools.chain(self.game.sequence,
                                                  self.game.open_cards))
        self.game.open_cards = [0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0]

    def open_new_cards(self):

        self.fill_open_cards()
        if not self.find_solutions():
            self.put_cards_into_deck()
            if self.find_solution_in_deck():
                self.fill_open_cards()
                self.find_solutions()
            else:
                return "Finish"

        self.get_card_info()

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

    def find_solution_in_deck(self):
        game_set = GameSet()
        cards_amount = len(self.game.sequence)

        for first_card_ind in range(cards_amount-1):
            for second_card_ind in range(first_card_ind+1, cards_amount):
                for third_card_ind in range(second_card_ind+1, cards_amount):
                    if game_set.check_set(self.game.sequence[first_card_ind],
                                          self.game.sequence[second_card_ind],
                                          self.game.sequence[third_card_ind]):
                        self.get_set_from_deck(self.game.sequence[first_card_ind],
                                               self.game.sequence[second_card_ind],
                                               self.game.sequence[third_card_ind])
                        return True
        return False

    def get_set_from_deck(self, first_el, second_el, third_el):

        for position, element in enumerate((first_el, second_el, third_el)):
            self.game.open_cards[position] = element
            self.game.sequence.remove(element)
        
        random.shuffle(self.game.open_cards)

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
