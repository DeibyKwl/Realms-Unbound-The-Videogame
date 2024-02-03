import pygame
import time
import random

duration = 2

def draw_dice(number, screen, result=False):
    screen.fill("black")
    dice_number = pygame.font.Font(None, 45).render(str(number), True, "White")
    screen.blit(dice_number, (500,500))
    pygame.display.flip()
    pygame.time.delay(10)

def dice_rolling(screen):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Display numbers 1 to 6
        for i in range(1, 7):
            draw_dice(i, screen)
            # Display a random number after 2 seconds
            random_number = random.randint(1, 6)
            draw_dice(random_number, screen)            