import pytest
from pathlib import Path

from advent_of_code import day_04


def test_read_numbers():
    numbers = day_04.read_numbers("day_04.txt", Path(__file__).parent / "static_files")
    assert numbers == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def test_read_boards():
    boards = day_04.read_boards("day_04.txt", Path(__file__).parent / "static_files")
    assert len(boards) == 3


@pytest.mark.parametrize("card,expected_board", [
    (
        [" 1  2 14", "29  3 17", "15 18  6"],
        {
            1: {"row": 0, "column": 0, "marked": False},
            2: {"row": 0, "column": 1, "marked": False},
            14: {"row": 0, "column": 2, "marked": False},
            29: {"row": 1, "column": 0, "marked": False},
            3: {"row": 1, "column": 1, "marked": False},
            17: {"row": 1, "column": 2, "marked": False},
            15: {"row": 2, "column": 0, "marked": False},
            18: {"row": 2, "column": 1, "marked": False},
            6: {"row": 2, "column": 2, "marked": False},
        }
    ),
])
def test_create_board(card, expected_board):
    assert day_04.create_board(card) == expected_board


def test_winning_score():
    boards = day_04.read_boards("day_04.txt", Path(__file__).parent / "static_files")
    numbers = day_04.read_numbers("day_04.txt", Path(__file__).parent / "static_files")
    assert day_04.winning_score(boards, numbers) == 4512
