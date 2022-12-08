from copy import deepcopy
import pygame

LIGHT_PIECE = (237, 230, 214)
DARK_PIECE = (43, 42, 35)


def negamax(position, depth, color, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    value = float('-inf')
    best_move = None
    for move in get_all_moves(position, color, game):
        evaluation = -negamax(move, depth - 1, -color, game)[0]

        if value <= -evaluation:
            value = -evaluation
            best_move = move

    return value, best_move


def negamax_alpha_beta(position, depth, color, alpha, beta, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    value = float('-inf')
    best_move = None
    for move in get_all_moves(position, color, game):
        evaluation = -negamax_alpha_beta(move, depth - 1, -color, -beta, -alpha, game)[0]
        if value <= -evaluation:
            value = -evaluation
            best_move = move
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value, best_move


def negascout(position, depth, color, alpha, beta, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    value = float('-inf')
    best_move = None
    b = beta
    for i, move in enumerate(get_all_moves(position, color, game)):

        evaluation = -negascout(position, depth - 1, color, -b, -alpha, game)[0]
        if alpha < evaluation < beta and i > 1:
            evaluation = -negascout(position, depth - 1, color, -beta, -alpha, game)[0]

        if value <= -evaluation:
            value = -evaluation
            best_move = move

        alpha = max(alpha, value)
        if alpha >= beta:
            break
        b = alpha + 1

    return value, best_move


def get_all_moves(board, clr, game):
    moves = []
    if clr == 1:
        color = LIGHT_PIECE
    elif clr == -1:
        color = DARK_PIECE

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.column)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(50)
