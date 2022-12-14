from copy import deepcopy
import pygame

LIGHT_PIECE = (237, 230, 214)
DARK_PIECE = (43, 42, 35)


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, LIGHT_PIECE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, DARK_PIECE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move

def minimax_alpha_beta(position, depth, max_player, alpha, beta, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, LIGHT_PIECE, game):
            evaluation = minimax_alpha_beta(move, depth - 1, False, alpha, beta, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, DARK_PIECE, game):
            evaluation = minimax_alpha_beta(move, depth - 1, True, alpha, beta, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break

        return min_eval, best_move


def expectimax(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, LIGHT_PIECE, game):
            evaluation = expectimax(move, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        exp_eval = 0
        exp_move = None
        moves = get_all_moves(position, DARK_PIECE, game)
        for move in moves:
            evaluation = expectimax(move, depth - 1, True, game)[0]
            exp_eval = (exp_eval + evaluation) // 2
            if exp_eval == evaluation:
                exp_move = move

        return exp_eval, exp_move


def get_all_moves(board, color, game):
    moves = []

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
    pygame.time.delay(100)
