from cards import AllCards, Card, GameSet


""" assert GameSet().check_param('red', 'red', 'red') == True
assert GameSet().check_param('red', 'blue', 'red') == False
assert GameSet().check_param('red', 'red', 'blue') == False
assert GameSet().check_param('blue', 'red', 'red') == False

assert GameSet().check_param(1, 2, 3)==True
assert GameSet().check_param(3, 2, 3)==False """


cards = AllCards()
cards.open_cards = [
    [Card('r', 'w', 'e', 1),
    Card('g', 'c', 'e', 1),
    Card('r', 'c', 's', 3),
    Card('b', 's', 's', 2) ],
    [Card('g', 's', 'e', 2),
    Card('g', 's', 'f', 2),
    Card('b', 's', 'f', 1),
    Card('g', 'w', 'f', 1)],
    [Card('b', 'c', 'e', 2),
    Card('g', 'w', 'f', 3),
    Card('r', 'c', 's', 2),
    Card('b', 's', 'f', 2)]
]
print(cards.find_solutions())
