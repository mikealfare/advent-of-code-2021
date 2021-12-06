import pytest

from advent_of_code import day_01


@pytest.mark.parametrize("depths,expected_increases", [
    ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 7)
])
def test_increases(depths, expected_increases):
    assert day_01.increases(depths) == expected_increases


@pytest.mark.parametrize("depths,expected_sums", [
    ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), (607, 618, 618, 617, 647, 716, 769, 792))
])
def test_window_sums(depths, expected_sums):
    assert day_01.window_sums(depths) == expected_sums
