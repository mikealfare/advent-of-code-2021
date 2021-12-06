import pytest

from advent_of_code import day_02


@pytest.mark.parametrize("position,command,expected_position", [
    ((0, 0), ("forward", 5), (5, 0)),
    ((0, 0), ("down", 5), (0, 5)),
    ((0, 0), ("up", 3), (0, -3)),
])
def test_move(position, command, expected_position):
    assert day_02.move(position, command) == expected_position


@pytest.mark.parametrize("position,commands,expected_position", [
    (
        (0, 0),
        (
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2)
        ),
        (15, 10)
    )
])
def test_moves(position, commands, expected_position):
    assert day_02.moves(position, commands) == expected_position
