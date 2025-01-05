import random
from itertools import product

from task_2.cell import Cell


class GamePole:
    pole: list[list[Cell]]
    N: int
    M: int

    def __init__(self, N, M) -> None:
        self.N = N
        if -1 < M < N * N + 1:
            self.M = M
        else:
            raise ValueError("mines amount should be between 0 and total amount of cells (inclusive)")
        self.pole = self.init()

    def init(self) -> list[list[Cell]]:
        """Инициализирует поле, размещая мины и подсчитывая количество мин вокруг клеток"""
        pre_pole = [[Cell(mine=False, fl_open=False) for i in range(self.N)] for j in range(self.N)]
        self.place_mines(pre_pole)
        self.count_mines_around_cells(pre_pole)
        return pre_pole

    def show(self) -> None:
        """
        Отображает поле в консоли в виде таблицы клеток,
        если клетка не открыта, то отображается символ #,
        если клетка открыта, но не содержит мины, то отображается число мин вокруг,
        если клетка открыта и содержит мину, то отображается символ *
        """
        for row in self.pole:
            for cell in row:
                if not cell.fl_open:
                    print("#", end=" ")
                elif cell.mine:
                    print("*", end=" ")
                else:
                    print(cell.around_mines, end=" ")
            print("")

    def place_mines(self, pre_pole: list[list[Cell]]) -> None:
        """Размещает мины случайным образом по игровому полю(макс одна мина на одной клетке)"""
        random_indexes = random.sample([(i, j) for i in range(self.N) for j in range(self.N)], self.M)
        for index in random_indexes:
            i, j = index
            cell = pre_pole[i][j]
            cell.mine = True

    def count_mines_around_cells(self, pre_pole: list[list[Cell]]) -> None:
        """Считает, сколько мин вокруг клетки"""
        N = self.N
        for i in range(N):
            for j in range(N):
                cell = pre_pole[i][j]
                if not cell.mine:
                    y = filter(lambda d: -1 < d < N, [i - 1, i, i + 1])
                    x = filter(lambda d: -1 < d < N, [j - 1, j, j + 1])
                    border_sum = sum(map(lambda c: pre_pole[c[0]][c[1]].mine, product(y, x)))
                    cell.around_mines = border_sum


pole_game = GamePole(10, 12)
