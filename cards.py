import pygame

class deck_set(pygame.sprite.Sprite):
    def __init__(self, card_pos):
        super().__init__()
        print('nothing')

        # Sprite 


        # Stats

class player_set(pygame.sprite.Sprite):
    def __init__(self, player_class):
        super().__init__()
        health = 5
        self.image = pygame.image.load(f'sprites/player/player_{player_class}_{health}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,180))
        self.rect = self.image.get_rect(topleft = (545,510))
        self.player_class = player_class


    # Stats
    def player_update(self, health):
        self.image = pygame.image.load(f'sprites/player/player_{self.player_class}_{health}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,180))
        self.rect = self.image.get_rect(topleft = (545,510))




class enemy_set(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
 
            # Sprite 


            # Stats
