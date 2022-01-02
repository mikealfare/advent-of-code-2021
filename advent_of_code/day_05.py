from pathlib import Path
from typing import List, Set
from collections import Counter, namedtuple


Point = namedtuple("Point", ["x", "y"])
Vent = namedtuple("Vent", ["start", "end"])


def overlapping_points(vents: List[Vent]) -> Set[Point]:
    all_points = []
    for vent in vents:
        all_points.extend(cardinal_points(vent))
    counter = Counter(all_points)
    return set(point for point in counter.elements() if counter[point] > 1)


def cardinal_points(vent: Vent) -> List[Point]:
    if is_horizontal(vent):
        return [Point(x, vent.start.y) for x in ordered_range(vent.start.x, vent.end.x)]
    elif is_vertical(vent):
        return [Point(vent.start[0], y) for y in ordered_range(vent.start.y, vent.end.y)]
    else:
        return []


def is_horizontal(vent: Vent) -> bool:
    return vent.start.y == vent.end.y


def is_vertical(vent: Vent) -> bool:
    return vent.start.x == vent.end.x


def ordered_range(a: int, b: int):
    if a >= b:
        lower = b
        upper = a
    else:
        lower = a
        upper = b
    return range(lower, upper + 1)


def read_vents(file_name: str) -> List[Vent]:
    file = Path(__file__).parent / "static_files" / file_name
    file_contents = file.read_text()
    return [parse_vent(vent) for vent in file_contents.split("\n")]


def parse_vent(vent: str) -> Vent:
    start, _, end = vent.split(" ")
    start_x, start_y = start.split(",")
    end_x, end_y = end.split(",")
    return Vent(Point(int(start_x), int(start_y)), Point(int(end_x), int(end_y)))


if __name__ == "__main__":
    print(len(overlapping_points(read_vents("day_05.txt"))))
