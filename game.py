from deck import Deck


class Game:
    # Sets up the game board
    def __init__(self, numberCards):
        self.gameDeck = Deck()
        self.drinkCount = 0

        self.numberCards = numberCards

        # Set up the discard
        # self.discard = []

        # Stack the piles
        self.pile = []
        for i in range(numberCards):
            self.pile.append(self.gameDeck.deal())

    def play(self):
        # Start with zero drinks
        self.drinkCount = 0

        # Current drinks holder
        self.currentDrinks = 0

        # Determine drinking threshold
        if self.numberCards == 5:
            threshold = 9
        if self.numberCards == 6:
            threshold = 10
        if self.numberCards == 7:
            threshold = 11

        # Continue until the deck is gone
        while self.pile:
            currentCard = self.pile.pop()
            # self.discard.append(currentCard)

            # Increase the number of drinks
            self.currentDrinks += 1

            if currentCard >= threshold:
                # Add drinks equal to the number of stacks turned
                self.drinkCount += self.currentDrinks
                # Refill the stacks
                self.refill(self.currentDrinks)

                self.currentDrinks = 0

            # The winning condition
            if len(self.pile) == 0:
                return self.drinkCount

    # Refills n stacks
    def refill(self, n):
        for i in range(n):
            dealtCard = self.gameDeck.deal()
            if dealtCard != 0:
                self.pile.append(dealtCard)