import mortoray_path_finding as mpf
import math


def lee_algorithm(board, start, end, max_distance=math.inf):
    # Створює дублікат дошки і заповнює поле `Cell.count` відстанню від старту до цієї клітинки.
    work_board = board.clone()
    work_board.clear_count(math.inf)

    # позначити початок і кінець для інтерфейсу користувача
    work_board.at(start).mark = mpf.maze.CellMark.Start
    work_board.at(end).mark = mpf.maze.CellMark.End

    # ми починаємо звідси, таким чином, відстань 0
    open_list = [start]
    work_board.at(start).count = 0

    # (x,y) зміщення від поточної комірки
    neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while open_list:
        cur_pos = open_list.pop(0)
        cur_cell = work_board.at(cur_pos)

        for neighbour in neighbours:
            ncell_pos = mpf.maze.add_point(cur_pos, neighbour)
            if not work_board.is_valid_point(ncell_pos):
                continue

            cell = work_board.at(ncell_pos)

            if cell.type != mpf.maze.CellType.Empty:
                continue

            dist = cur_cell.count + 1

            if dist > max_distance:
                continue

            if cell.count > dist:
                cell.count = dist
                cell.path_from = cur_cell
                open_list.append(ncell_pos)

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
    filled = lee_algorithm(maze.board, maze.start, maze.end)
    path = backtrack_to_start(filled, maze.end)

    finder = mpf.draw.Finder()
    finder.set_board(filled)
    finder.set_path(path)
    finder.run()


if __name__ == '__main__':
    main()
