import pytest

from advent_of_code import day_02


@pytest.mark.parametrize("position,depth,command,expected", [
    (0, 0, ("forward", 5), (5, 0)),
    (0, 0, ("down", 5), (0, 5)),
    (0, 0, ("up", 3), (0, -3)),
])
def test_move(position, depth, command, expected):
    assert day_02.move(position, depth, command) == expected


@pytest.mark.parametrize("position,depth,commands,expected", [
    (
        0, 0,
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
def test_moves(position, depth, commands, expected):
    assert day_02.moves(position, depth, commands) == expected


@pytest.mark.parametrize("position,depth,aim,command,expected", [
    (0, 0, 0, ("forward", 5), (5, 0, 0)),
    (5, 0, 0, ("down", 5), (5, 0, 5)),
    (5, 0, 5, ("forward", 8), (13, 40, 5)),
    (13, 40, 5, ("up", 3), (13, 40, 2)),
    (13, 40, 2, ("down", 8), (13, 40, 10)),
    (13, 40, 10, ("forward", 2), (15, 60, 10)),
])
def test_move_with_aim(position, depth, aim, command, expected):
    assert day_02.move_with_aim(position, depth, aim, command) == expected


@pytest.mark.parametrize("position,depth,aim,commands,expected", [
    (
        0, 0, 0,
        (
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2)
        ),
        (15, 60, 10)
    )
])
def test_moves_with_aim(position, depth, aim, commands, expected):
    assert day_02.moves_with_aim(position, depth, aim, commands) == expected
