import pygame
import math
import random
import time

import cards as card
import dice

game_over = False
roll_dice = True

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
dice_number = None
dice_number_view = None

# Select Player
player = pygame.sprite.Group()
player_class = None
player_clicked = False
player_selected = True

while player_selected:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_selected = False
    
    screen.fill("black")

    mouse_pos = pygame.mouse.get_pos()

    selection_text = pygame.font.Font(None, 50).render('Select your character', False, 'White')
    screen.blit(selection_text,(80,100))

    swordman_text = pygame.font.Font(None, 30).render('SWORDMAN', False, 'White')
    swordman_rect = swordman_text.get_rect(topleft = (50,250))
    screen.blit(swordman_text,(50,250))

    archer_text = pygame.font.Font(None, 30).render('ARCHER', False, 'White')
    archer_rect = archer_text.get_rect(topleft = (230,250))
    screen.blit(archer_text,(230,250))

    mage_text = pygame.font.Font(None, 30).render('MAGE', False, 'White')
    mage_rect = mage_text.get_rect(topleft = (380,250))
    screen.blit(mage_text,(380,250))

    if swordman_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'swordman'
            player_selected = False

    if archer_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'archer'
            player_selected = False

    if mage_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'mage'
            player_selected = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


player_instance = card.player_set(player_class)
player.add(player_instance)


# main gameplay
while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if roll_dice:
        dice.dice_rolling(screen)
        dice_number = random.randint(1,7)
        dice_number_view = pygame.font.Font(None, 45).render(str(dice_number), True, "White")
        roll_dice = False
    
    screen.blit(dice_number_view, (500,500))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw player
    player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()