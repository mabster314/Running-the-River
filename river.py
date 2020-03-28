import random

# Class representing a deck of cards
class Deck:
    def __init__(self):
        # loads as an unshuffled deck
        self.cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,14]
        self.shuffleDeck()

    # method to shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.cards)

    # function to deal a card from the top of the deck
    def deal(self):
        return self.cards.pop() if len(self.cards) > 0 else 0

class Game:
    # Sets up the game board
    def __init__(self, numberCards):
        self.gameDeck = Deck()

        # Stack the piles
        self.pile = []
        for i in range(int(numberCards * (numberCards + 1 ) / 2)):
            self.pile.append(self.gameDeck.deal())

    def play(self, numberCards):
        # Start with zero drinks
        self.drinkCount = 0

        # Current drinks holder
        self.currentDrinks = 0

        # Determine drinking threshold
        if numberCards == 5:
            threshold = 9
        if numberCards == 6:
            threshold = 10
        if numberCards == 7:
            threshold = 11

        print(threshold)

        # Continue until the deck is gone
        while self.pile:
            # Increase the number of drinks
            self.currentDrinks += 1

            if self.pile.pop() >= threshold:
                # Add drinks equal to the number of stacks turned
                self.drinkCount += (self.currentDrinks)
                # Refill the stacks
                self.refill(self.currentDrinks)

                self.currentDrinks = 0

            # The winning condition
            if self.currentDrinks == numberCards:
                return self.drinkCount

            print("Current drinks: " + str(self.currentDrinks) + ". Total drinks: " + str(self.drinkCount) + ".")

    # Refills n stacks
    def refill(self, n):
        for i in range(n):
            dealtCard = self.gameDeck.deal()
            if dealtCard != 0:
                self.pile.append(dealtCard)


theGame = Game(6)
print(theGame.pile)
print(theGame.gameDeck.cards)
print(theGame.play(6))
