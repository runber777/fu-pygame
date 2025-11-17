class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        # Создать все 52 карты
        suits = ['chervi', 'bubi', 'kresti', 'piki']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
        return [Card(value, suit) for suit in suits for value in values]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

import pygame

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = pygame.image.load(f'karti/karti/{suit}{value}.png')
    def __str__(self):
        return f"{self.value}{self.suit}"


deck = Deck()
for card in deck.generate_deck():
    print(card)