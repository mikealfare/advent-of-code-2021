import pytest

from advent_of_code import day_05


@pytest.mark.parametrize("vent_string,expected_start,expected_end", [
    ("0,9 -> 5,9", (0, 9), (5, 9)),
    ("8,0 -> 0,8", (8, 0), (0, 8)),
    ("9,4 -> 3,4", (9, 4), (3, 4)),
    ("2,2 -> 2,1", (2, 2), (2, 1)),
    ("7,0 -> 7,4", (7, 0), (7, 4)),
    ("6,4 -> 2,0", (6, 4), (2, 0)),
    ("0,9 -> 2,9", (0, 9), (2, 9)),
    ("3,4 -> 1,4", (3, 4), (1, 4)),
    ("0,0 -> 8,8", (0, 0), (8, 8)),
    ("5,5 -> 8,2", (5, 5), (8, 2)),
])
def test_parse_vent(vent_string, expected_start, expected_end):
    assert day_05.parse_vent(vent_string) == day_05.Vent(day_05.Point(*expected_start), day_05.Point(*expected_end))


@pytest.mark.parametrize("vent_strings,expected_overlaps", [
    ([
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2"
    ], 5)
])
def test_overlapping_points(vent_strings, expected_overlaps):
    vents = [day_05.parse_vent(vent) for vent in vent_strings]
    assert len(day_05.overlapping_points(vents)) == expected_overlaps
