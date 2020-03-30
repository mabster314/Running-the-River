import random


class Deck:

    def __init__(self):
        # loads as an unshuffled deck
        self.cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                  10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14]
        self.shuffleDeck()

    # method to shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.cards)

    # function to deal a card from the top of the deck
    def deal(self):
        return self.cards.pop() if len(self.cards) > 0 else 0
