class Cell:
    mine: bool
    around_mines: int
    fl_open: bool

    def __init__(self, mine, around_mines=0, fl_open=False) -> None:
        if -1 < around_mines < 9:
            self.around_mines = around_mines
        else:
            raise ValueError("around_mines should be between 0 and 8 (inclusive)")
        self.mine = mine
        self.fl_open = fl_open
