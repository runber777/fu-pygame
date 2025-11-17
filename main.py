import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("BlackJack")
#icon = pygame.image.load("")
#pygame.display.set_icon(icon)

running = True
while running:

    screen.fill((140, 200, 130))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
# bubu