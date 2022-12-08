import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, DARK_PIECE, LIGHT_PIECE
from checkers.game import Game
from minimax.algorithm import minimax
from minimax.algorithm import expectimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шашки')


def get_row_and_column_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == LIGHT_PIECE:
            value, new_board = minimax(game.get_board(), 4, LIGHT_PIECE, float('-inf'), float('inf'), game)
            # value, new_board = expectimax(game.get_board(), 3, LIGHT_PIECE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            if game.winner() == LIGHT_PIECE:
                print("Game ended. White wins!")
            else:
                print("Game ended. Black wins!")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_row_and_column_from_mouse(position)
                game.select(row, column)

        game.update()

    pygame.quit()


main()
