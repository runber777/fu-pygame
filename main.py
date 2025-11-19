import pygame as pg
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = pg.image.load(f'karti/karti/{suit}{value}.png')
        # Scale the image if needed to match your back card size
        self.image = pg.transform.scale(self.image, (150, 200))


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        random.shuffle(self.cards)  # Shuffle the deck

    def generate_deck(self):
        suits = ['chervi', 'bubi', 'kresti', 'piki']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
        return [Card(value, suit) for suit in suits for value in values]

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

pg.init()
screen = pg.display.set_mode((1200, 600))
pg.display.set_caption("BlackJack")
icon = pg.image.load("karti/karti/icon.jpg")
pg.display.set_icon(icon)

back2 = pg.image.load("karti/karti/backside.jpg")
back = pg.transform.scale(back2, (150, 200))
back_rect = back.get_rect(topleft=(1000, 200))

f1 = pg.font.Font(None, 30)
text = f1.render('Конец хода', True, (222,111,160), (143,190,143))
text_rect = text.get_rect(topleft=(1015, 150))

deck = Deck()
dealer_cards = []
player_cards = []

running = True
while running:
    screen.fill((140, 200, 130))
    screen.blit(back, back_rect)
    screen.blit(text, text_rect)

    for card_obj, x, y in dealer_cards:
        screen.blit(card_obj.image, (x, y))

    for card_obj, x, y in player_cards:
        screen.blit(card_obj.image, (x, y))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()
                if back_rect.collidepoint(pos):
                    card = deck.draw_card()
                    if card:
                        x = 20 + (len(player_cards) * (100+30))
                        y = 410
                        player_cards.append((card, x, y))

                elif text_rect.collidepoint(pos):
                    cards_to_deal = random.randint(2, 5)
                    for i in range(cards_to_deal):
                        card = deck.draw_card()
                        if card:
                            x = 20 + (len(dealer_cards) * (100 + 30))
                            y = 10
                            dealer_cards.append((card, x, y))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()