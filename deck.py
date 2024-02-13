import random
from card import Card


class Deck:

    def __init__(self):
        self.deck = []
        i = 0
        while i != 52:
            card = Card().random_choice()
            if not (card in self.deck):
                self.deck.append(card)
                i += 1

    def give_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card


    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return f'{self.deck}'