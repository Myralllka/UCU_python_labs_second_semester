# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    CELL_WALL = " *"
    CELL_PATH = " x"
    CELL_TRIED = " o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self.maze_cells = Array2D(num_rows, num_cols)
        self.start_cell = None
        self.exit_cell = None

    # Returns the number of rows in the maze.
    def num_rows(self):
        return self.maze_cells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols(self):
        return self.maze_cells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def set_wall(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.maze_cells[row, col] = self.CELL_WALL

    # Sets the starting cell position.
    def set_start(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.start_cell = _CellPosition(row, col)

    # Sets the exit cell position.
    def set_exit(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self.exit_cell = _CellPosition(row, col)

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def find_path(self):
        if not self.maze_cells[self.exit_cell.row, self.exit_cell.col] is None:
            return False
        tmp = Stack()
        i, j = self.start_cell.row, self.start_cell.col
        dead_ends = [self.CELL_PATH, self.CELL_TRIED, self.CELL_WALL]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        tmp.push([i, j])
        self.maze_cells[i, j] = self.CELL_PATH
        while True:
            for direction in directions:
                try:
                    i1, j1 = i + direction[0], j + direction[1]
                    t = self.maze_cells[i1, j1]
                except IndexError:
                    continue
                while self.maze_cells[i1, j1] \
                        not in dead_ends:
                    i += direction[0]
                    j += direction[1]
                    tmp.push([i, j])
                    self.maze_cells[i, j] = self.CELL_PATH
                    if i == self.exit_cell.row and j == self.exit_cell.col:
                        return True
                    if i == self.start_cell.row and j == self.start_cell.col:
                        return False
            if self.check_cell(i, j) is None:
                while True:
                    coor = tmp.pop()
                    if tmp.isEmpty():
                        return False
                    self.maze_cells[coor[0], coor[1]] = self.CELL_TRIED
                    coor = tmp.peek()
                    tmpcoor = self.check_cell(coor[0], coor[1])
                    if tmpcoor:
                        i, j = coor[0], coor[1]
                        break
            if i == self.start_cell.row and j == self.start_cell.col:
                return False
            if i == self.exit_cell.row and j == self.exit_cell.col:
                return True

    def check_cell(self, ii, jj):
        if ii == self.start_cell.row and jj == self.start_cell.col:
            return None
        if self.maze_cells[ii + 1, jj] is None:
            return [1, 0]
        elif self.maze_cells[ii, jj + 1] is None:
            return [0, 1]
        elif self.maze_cells[ii, jj - 1] is None:
            return [0, -1]
        elif self.maze_cells[ii - 1, jj] is None:
            return [-1, 0]
        else:
            return None

    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):
        for i in range(self.num_cols()):
            for j in range(self.num_rows()):
                if self.maze_cells[i, j] == self.CELL_PATH or \
                        self.maze_cells[i, j] == self.CELL_TRIED:
                    self.maze_cells[i, j] = None

    # Prints a text-based representation of the maze.
    def draw(self):
        for i in range(self.num_cols()):
            for j in range(self.num_rows()):
                if self.maze_cells[i, j] is None:
                    print('  ', end='')
                else:
                    print(self.maze_cells[i, j], end='')
            print()

    # Returns True if the given cell position is a valid move.
    def _valid_move(self, row, col):
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self.maze_cells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exit_found(self, row, col):
        return row == self.exit_cell.row and col == self.exit_cell.col

    # Drops a "tried" token at the given cell.
    def _mark_tried(self, row, col):
        self.maze_cells[row, col] = self.CELL_TRIED

    # Drops a "path" token at the given cell.
    def _mark_path(self, row, col):
        self.maze_cells[row, col] = self.CELL_PATH


# Private storage class for holding a cell position.
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
