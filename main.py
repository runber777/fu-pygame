import pygame as pg

pg.init()
screen = pg.display.set_mode((900, 600))
pg.display.set_caption("BlackJack")
icon = pg.image.load("karti/karti/icon.jpg")
pg.display.set_icon(icon)

back2 = pg.image.load("karti/karti/backside.jpg")
back = pg.transform.scale(back2, (150, 200))
back_rect = back.get_rect(topleft=(700, 200))

tets = pg.image.load("karti/karti/bubi1.png")
card_clicked = False

running = True
while running:
    screen.fill((140, 200, 130))
    screen.blit(back, (700, 200))

    if card_clicked:
        screen.blit(tets, (400, 400))

    screen.blit(tets, (400, 50))
    pg.display.update()

    mouse_buttons = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()

    if mouse_buttons[0] and back_rect.collidepoint(pos):
        card_clicked = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()