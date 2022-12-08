import pygame

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLUMNS = 8
SQUARE_SIZE = WIDTH // COLUMNS

# colors
LIGHT = (254, 255, 233)
DARK = (121, 96, 60)
LIGHT_PIECE = (237, 230, 214)
DARK_PIECE = (43, 42, 35)
GOLD = (255, 215, 0)
SILVER = (187, 194, 204)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

CROWN = pygame.transform.scale(pygame.image.load('checkers\crown.png'), (50, 60))
