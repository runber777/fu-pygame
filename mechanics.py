import pygame as pg
import random


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        suits = ['chervi', 'bubi', 'kresti', 'piki']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
        return [Card(value, suit) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = pg.image.load(f'karti/karti/{suit}{value}.png')
        # Scale the image if needed to match your back card size
        self.image = pg.transform.scale(self.image, (150, 200))
    def __repr__(self):
        return f"{self.suit}{self.value}"

class Player:
    def __init__(self):
        self.hand = []
        self.positions = []

    def add_card(self, card, y=410):
        self.hand.append((card, 20 + (len(self.hand)) * 130, y))
        #self.positions.append((20 + (len(self.hand)) * 130, 10))

    def get_score(self):
        score = 0
        aces = 0

        for card, x, y in self.hand:
            if card.value in ['11', '12', '13']:
                score += 10
            elif card.value == "1":
                score += 11
                aces += 1
            else:
                score += int(card.value)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score



class Dealer(Player):
    def should_hit(self):
        return self.get_score() < 17




# deck = Deck()
# player = Player()
# dealer = Dealer()
#
# print(deck.cards)
# player.add_card(deck.deal_card())
# player.add_card(deck.deal_card())
#
#
# print(player.hand)
# print(player.get_score())
#
# while dealer.should_hit():
#     dealer.add_card(deck.deal_card())