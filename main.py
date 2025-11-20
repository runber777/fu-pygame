import pygame as pg
import random
from mechanics import Card, Deck, Player, Dealer

# class Card:
#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit
#         self.image = pg.image.load(f'karti/karti/{suit}{value}.png')
#         # Scale the image if needed to match your back card size
#         self.image = pg.transform.scale(self.image, (150, 200))
#
#
# class Deck:
#     def __init__(self):
#         self.cards = self.generate_deck()
#         random.shuffle(self.cards)  # Shuffle the deck
#
#     def generate_deck(self):
#         suits = ['chervi', 'bubi', 'kresti', 'piki']
#         values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
#         return [Card(value, suit) for suit in suits for value in values]
#
#     def draw_card(self):
#         if self.cards:
#             return self.cards.pop()
#         return None

pg.init()
screen = pg.display.set_mode((1200, 600))
pg.display.set_caption("BlackJack")
icon = pg.image.load("karti/karti/icon.jpg")
pg.display.set_icon(icon)

back2 = pg.image.load("karti/karti/backside.jpg")
back = pg.transform.scale(back2, (150, 200))
back_rect = back.get_rect(topleft=(1000, 200))

f1 = pg.font.Font(None, 30)
f2 = pg.font.Font(None, 72)
f3 = pg.font.Font(None, 30)
f4 = pg.font.Font(None, 30)
text = f1.render('Конец хода', True, (222,111,160), (143,190,143))
text_rect = text.get_rect(topleft=(1015, 150))

def draw_message(screen, message):
    text_surf2 = f2.render(message, True, (222,111,160))
    text_rect2 = text_surf2.get_rect(center=(600, 300))
    screen.blit(text_surf2, text_rect2)

def player_score(screen, message):
    text_surf3 = f3.render(message, True, (222,111,160))
    text_rect3 = text_surf3.get_rect(topleft=(1015, 450))
    screen.blit(text_surf3, text_rect3)

def dealer_score(screen, message):
    text_surf4 = f4.render(message, True, (222,111,160))
    text_rect4 = text_surf4.get_rect(topleft=(1015, 50))
    screen.blit(text_surf4, text_rect4)


deck = Deck()
player = Player()
dealer = Dealer()

game_over = False
message = ""
message_score1 = "Ваши очки: 0"
message_score2 = "Очки диллера: 0"
running = True
while running:
    screen.fill((140, 200, 130))
    screen.blit(back, back_rect)
    screen.blit(text, text_rect)

    for card_obj, x, y in dealer.hand:
        screen.blit(card_obj.image, (x, y))

    for card_obj, x, y in player.hand:
        screen.blit(card_obj.image, (x, y))
    player_score(screen, message_score1)
    dealer_score(screen, message_score2)
    if message:
        draw_message(screen, message)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            if event.button == 1:
                pos = pg.mouse.get_pos()
                if back_rect.collidepoint(pos):
                    player.add_card(deck.deal_card())
                    message_score1 = f'Ваши очки: {str(player.get_score())}'
                    if player.get_score() > 21:
                        message = "ВЫ ПРОИГРАЛИ"
                        game_over = True
                elif text_rect.collidepoint(pos):
                    while dealer.should_hit():
                        dealer.add_card(deck.deal_card(), y=10)
                        message_score2 = f'Очки диллера: {str(dealer.get_score())}'
                        if dealer.get_score() >= player.get_score():
                            break
                    if player.get_score() > dealer.get_score():
                        message = "ПОБЕДА"
                    elif player.get_score() == dealer.get_score():
                        message = "НИЧЬЯ"
                    else:
                        message = "ВЫ ПРОИГРАЛИ"
                    game_over = True

pg.quit()