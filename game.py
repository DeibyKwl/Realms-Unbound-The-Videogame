import pygame
import math
import random
import time

import cards as card
import dice

game_over = False
roll_dice = False

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
player_class_code = None # Use to determine if card attack receive bonus


# TODO: Change this while loop into its own file
while player_selected:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_selected = False
    
    screen.fill("black")

    mouse_pos = pygame.mouse.get_pos()

    selection_text = pygame.font.Font(None, 50).render('Select your character', False, 'White')
    screen.blit(selection_text,(430,200))

    swordman_text = pygame.font.Font(None, 30).render('SWORDMAN', False, 'White')
    swordman_rect = swordman_text.get_rect(topleft = (560,350))
    screen.blit(swordman_text,(560,350))

    archer_text = pygame.font.Font(None, 30).render('ARCHER', False, 'White')
    archer_rect = archer_text.get_rect(topleft = (580,450))
    screen.blit(archer_text,(580,450))

    mage_text = pygame.font.Font(None, 30).render('MAGE', False, 'White')
    mage_rect = mage_text.get_rect(topleft = (595,550))
    screen.blit(mage_text,(595,550))

    if swordman_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'swordman'
            player_selected = False
            player_class_code = 0

    if archer_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'archer'
            player_selected = False
            player_class_code = 1

    if mage_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1:
            player_class = 'mage'
            player_selected = False
            player_class_code = 2

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


player_instance = card.player_set(player_class)
player.add(player_instance)

# Determine number of enemies
enemy_num = dice.roll_dice(screen)
dice_num = enemy_num

enemies = pygame.sprite.Group()
enemy_list = []
enemy_classes = ['swordman', 'archer', 'mage']
enemy_x_pos, enemy_y_pos = 25,10

# Creation of enemies
for _ in range(enemy_num):
    # TODO: find a way to sparce enemies evenly depending on the number of enemies
    enemy_instance = card.enemy_set(enemy_classes[random.randint(0,2)],enemy_x_pos,enemy_y_pos)
    enemies.add(enemy_instance)
    enemy_x_pos += 170

    # To keep track of the enemies?
    enemy_list.append(enemy_instance)

cards_set = pygame.sprite.Group()
card_list = []
card_classes = ['sword_attack', 'arrow_shot', 'magic_attack', 'heal', 'defense']
card_x_pos, card_y_pos = 25, 700

# Creation of card set
for _ in range(7):
    card_class = random.randint(0,4)
    if player_class_code == card_class:
        card_instance = card.deck_set(card_classes[card_class], card_x_pos, card_y_pos, True)
    else:
        card_instance = card.deck_set(card_classes[card_class], card_x_pos, card_y_pos, False)
    cards_set.add(card_instance)
    card_x_pos += 170

# main gameplay
while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    if not roll_dice:
        dice_number_view = pygame.font.Font(None, 45).render(str(dice_num), True, "White")
    screen.blit(dice_number_view, (1100,500))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw player
    player.draw(screen)

    # Draw enemies
    enemies.draw(screen)

    # Draw Card set
    cards_set.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()