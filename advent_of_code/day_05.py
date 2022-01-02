from pathlib import Path
from typing import List, Set
from collections import Counter, namedtuple


Point = namedtuple("Point", ["x", "y"])
Vent = namedtuple("Vent", ["start", "end"])


def overlapping_points(vents: List[Vent], diagonal: bool = False) -> Set[Point]:
    all_points = []
    for vent in vents:
        all_points.extend(vent_points(vent, diagonal))
    counter = Counter(all_points)
    return set(point for point in counter.elements() if counter[point] > 1)


def vent_points(vent: Vent, diagonal: bool = False) -> List[Point]:
    if is_horizontal(vent):
        return [Point(x, vent.start.y) for x in line(vent.start.x, vent.end.x)]
    elif is_vertical(vent):
        return [Point(vent.start[0], y) for y in line(vent.start.y, vent.end.y)]
    elif diagonal:
        return [Point(x, y) for x, y in zip(line(vent.start.x, vent.end.x), line(vent.start.y, vent.end.y))]
    else:
        return []


def is_horizontal(vent: Vent) -> bool:
    return vent.start.y == vent.end.y


def is_vertical(vent: Vent) -> bool:
    return vent.start.x == vent.end.x


def line(a: int, b: int):
    if a >= b:
        step = -1
    else:
        step = 1
    return range(a, b + step, step)


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
    print(len(overlapping_points(read_vents("day_05.txt"), True)))
