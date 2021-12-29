from typing import List, Dict
from pathlib import Path
from copy import deepcopy


Board = Dict[int, Dict[str, int]]
Row = Column = Line = Dict[int, bool]


def winning_score(boards: List[Board], numbers: List[int]) -> int:
    for number in numbers:
        boards = mark_boards(boards, number)
        if board := winning_board(boards):
            return score_board(board, number)
    return 0


def losing_score(boards: List[Board], numbers: List[int]) -> int:
    for number in numbers:
        boards = mark_boards(boards, number)
        for board in boards:
            if board_wins(board):
                boards.remove(board)
            if not boards:
                return score_board(board, number)


def mark_boards(boards: List[Board], number: int) -> List[Board]:
    return [mark(board, number) for board in boards]


def mark(board: Board, number: int) -> Board:
    if number in board:
        board[number]["marked"] = True
    return board


def winning_board(boards: List[Board]) -> Board:
    for board in boards:
        if board_wins(board):
            return board


def board_wins(board: Board) -> bool:
    for row in rows(board):
        if all(row.values()):
            return True
    for column in columns(board):
        if all(column.values()):
            return True
    return False


def rows(board: Board) -> List[Row]:
    return lines(board, "row")


def columns(board: Board) -> List[Column]:
    return lines(board, "column")


def lines(board: Board, axis: str) -> List[Line]:
    indices = set(point[axis] for point in board.values())
    return [
        {
            value: point["marked"]
            for value, point in board.items()
            if point[axis] == idx
        }
        for idx in indices
    ]


def score_board(board: Board, number: int) -> int:
    unmarked_numbers = [value for value, point in board.items() if not point["marked"]]
    return number * sum(unmarked_numbers)


def read_numbers(file_name: str, directory: Path = None) -> List[int]:
    if not directory:
        directory = Path(__file__).parent / "static_files"
    file = directory / file_name
    file_contents = file.read_text()
    first_line = file_contents.split("\n")[0]
    return [int(number) for number in first_line.split(",")]


def read_boards(file_name: str, directory: Path = None) -> List[Board]:
    if not directory:
        directory = Path(__file__).parent / "static_files"
    file = directory / file_name
    file_contents = file.read_text()
    cards = file_contents.split("\n")[2:]
    boards = []
    card = []
    for row in cards:
        if row == "":
            boards.append(create_board(card))
            card = []
        else:
            card.append(row)
    if card:
        boards.append(create_board(card))
    return boards


def create_board(card: List[str]) -> Board:
    board = {}
    for row, values in enumerate(card):
        values = [value for value in values.split(" ") if value]
        for column, value in enumerate(values):
            board.update({
                int(value): {
                    "row": row,
                    "column": column,
                    "marked": False
                }
            })
    return board


if __name__ == "__main__":
    puzzle_boards = read_boards("day_04.txt")
    puzzle_numbers = read_numbers("day_04.txt")
    print(winning_score(deepcopy(puzzle_boards), deepcopy(puzzle_numbers)))
    print(losing_score(deepcopy(puzzle_boards), deepcopy(puzzle_numbers)))
