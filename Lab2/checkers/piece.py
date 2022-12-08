import pygame.draw

from .constants import LIGHT_PIECE, DARK_PIECE, GOLD, SILVER, SQUARE_SIZE, CROWN


class Piece:
    PADDING = 15
    BORDER = 4

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def become_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        if self.color == LIGHT_PIECE:
            pygame.draw.circle(win, GOLD, (self.x, self.y), radius + self.BORDER)
        elif self.color == DARK_PIECE:
            pygame.draw.circle(win, SILVER, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.column = col
        self.calculate_position()

    def __repr__(self):
        return str(self.color)
