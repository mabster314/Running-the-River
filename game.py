from deck import Deck


class Game:
    # Sets up the game board
    def __init__(self, numberCards):
        self.gameDeck = Deck()
        self.drinkCount = 0

        # Set up the discard
        self.discard = []

        # Stack the piles
        self.pile = []
        for i in range(numberCards):
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
            print(self.pile)
            print(self.gameDeck.cards)
            # Increase the number of drinks
            self.currentDrinks += 1

            currentCard = self.pile.pop()
            self.discard.append(currentCard)

            if currentCard >= threshold:
                # Add drinks equal to the number of stacks turned
                self.drinkCount += self.currentDrinks
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