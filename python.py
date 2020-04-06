import numpy as np


class ChessBoard:
    def __init__(self, size):
        self._size = size
        self._chessboard = None
        self._print_box_size = len(str((self._size ** 2)))
        self._setup_chessboard()
        self._print_msg = None

    def _setup_chessboard(self):
        self._chessboard = np.array([[None] * (self._size) for i in range(self._size)])

    def set_value(self, row, column, value):
        if row not in list(range(self._size)):
            raise ValueError(
                f"Invalid row {row} given for chessboard of size {self._size}"
            )
        elif column not in list(range(self._size)):
            raise ValueError(
                f"Invalid row {column} given for chessboard of size {self._size}"
            )
        else:
            self._chessboard[row][column] = value

    def get_value(self, row, column):
        if row not in list(range(self._size)):
            raise ValueError(
                f"Invalid row {row} given for chessboard of size {self._size}"
            )
        elif column not in list(range(self._size)):
            raise ValueError(
                f"Invalid row {column} given for chessboard of size {self._size}"
            )
        else:
            return self._chessboard[row][column]

    def print_chessboard(self):
        self._print_msg = []
        for row in range(self._size):
            if row == 0:
                self._print_msg.append(self._print_row_seperator("-", "-"))
            else:
                self._print_msg.append(self._print_row_seperator())
            value_row = []
            for column in range(self._size):
                value_row.append(self._print_col_separator())
                value_row.append(self._print_value(self._chessboard[row][column]))
            value_row.append(self._print_col_separator())
            value_row = "".join(value_row)
            self._print_msg.append(value_row)
        self._print_msg.append(self._print_row_seperator("-", "-"))
        print_msg = "\n".join(self._print_msg)
        print(print_msg)

    def _print_row_seperator(self, crosspoint="+", endpoint="|"):
        print_row = [endpoint]
        for i in range(self._size):
            each_box = []
            for j in range(self._print_box_size):
                each_box.append("-")
            each_box = "".join(each_box)
            print_row.append(each_box)
            if i == self._size - 1:
                print_row.append(endpoint)
            else:
                print_row.append(crosspoint)
        print_row = "".join(print_row)
        return print_row

    def _print_col_separator(self):
        return "|"

    def _print_value(self, value):
        if value is None:
            val_str = []
            for i in range(self._print_box_size):
                val_str.append("X")
            val_str = "".join(val_str)
        else:
            val_str = str(value)
        return val_str


class KnightTour:
    def __init__(self, board_size, start_row=None, start_col=None):
        self._chessboard = ChessBoard(BOARD_SIZE)
        self._start_row = start_row
        self._start_col = start_col

    def run_tour(start_row=None, start_col=None):
        if start_row is not None:
            self._start_row
        if start_col is not None:
            self._start_col

        if self._start_row is None or self._start_col is None:
            raise ValueError(
                (
                    "Either start_row or start_col is None. "
                    "Either initialize KnightTour object with "
                    "a start row and column or give a start row "
                    "and column as arguments to run_tour"
                )
            )


if __name__ == "__main__":
    BOARD_SIZE = 6
    START_ROW = 0
    START_COL = BOARD_SIZE - 1

    cb = ChessBoard(6)

    cb.print_chessboard()
