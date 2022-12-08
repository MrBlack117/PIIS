import mortoray_path_finding as mpf
import math


def a_star_algorithm(board, start, end):
    # Створює дублікат дошки і заповнює поле `Cell.count` відстанню від старту до цієї клітинки.
    work_board = board.clone()
    work_board.clear_count(math.inf)

    # позначаємо початок і кінець
    start_cell = work_board.at(start)
    end_cell = work_board.at(end)
    start_cell.mark = mpf.maze.CellMark.Start
    end_cell.mark = mpf.maze.CellMark.End

    # ми починаємо звідси, таким чином, відстань 0
    visible_elements = [start_cell]
    accessible_elements = []
    start_cell.count = math.inf
    solution_found = False
    while not solution_found:
        # Перебираємо доступні елементи і рахуємо відстань до кінцевого
        while visible_elements:
            cur_cell = visible_elements.pop(0)
            cur_pos = cur_cell.pos
            cur_cell.hx += (math.fabs(cur_pos[0] - end[0]) + math.fabs(cur_pos[1] - end[1])) * 10
            accessible_elements.append(cur_cell)

        best_cell = start_cell
        # Рахуємо вартість кроку та обираємо найкращу клітинку
        for i in range(len(accessible_elements)):
            cur_cell = accessible_elements[i]
            cur_cell.count = cur_cell.hx + cur_cell.gx
            if cur_cell.count < best_cell.count and cur_cell.watched != True:
                best_cell = cur_cell

        best_cell.watched = True

        print('-----------')
        print(best_cell.pos)
        print(best_cell.mark)
        # (x,y) зміщення від поточної комірки
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, -1], [-1, -1], [1, 1]]

        # Перебираємо сусідні елементи і якщо вони доступні додаємо їх до відповідного списку
        while neighbours:
            neighbour_move = neighbours.pop(0)
            neighbour_pos = [best_cell.pos[0] + neighbour_move[0], best_cell.pos[1] + neighbour_move[1]]
            if not work_board.is_valid_point(neighbour_pos):
                continue

            neighbour_cell = work_board.at(neighbour_pos)

            if neighbour_cell.type == mpf.maze.CellType(2):
                continue

            if neighbour_cell == end_cell:
                print("End found:")
                print(neighbour_pos)
                solution_found = True

            move_type = math.fabs(neighbour_move[0]) + math.fabs(neighbour_move[1])

            if move_type == 1:
                neighbour_cell.gx = best_cell.gx + 10
            elif move_type == 2:
                neighbour_cell.gx = best_cell.gx + 14

            visible_elements.append(neighbour_cell)

    return work_board


def backtrack_to_start(board, end):
    cell = board.at(end)
    path = []
    while cell != None:
        path.append(cell)
        cell = cell.path_from

    return path


def main():
    maze = mpf.maze.create_wall_maze(20, 20)
    start = maze.start
    end = maze.end
    print('start')
    print(start)
    print('end')
    print(end)
    filled = a_star_algorithm(maze.board, start, end)
    path = backtrack_to_start(filled, maze.end)

    finder = mpf.draw.Finder()
    finder.set_board(filled)
    finder.set_path(path)
    finder.run()


if __name__ == '__main__':
    main()

# Проблема в том что алгоритм пересчитывает count там где его уже посчитали
