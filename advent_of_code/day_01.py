from typing import Tuple
from pathlib import Path


def increases(depths: Tuple[int, ...]) -> int:
    return len([
        x
        for x, y in zip(depths[:-1], depths[1:])
        if y > x
    ])


def window_sums(depths: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(
        sum(depths[idx:idx + 3])
        for idx in range(len(depths)-2)
    )


def read_depths(file_name: str) -> Tuple[int, ...]:
    file = Path(__file__).parent / "static_files" / file_name
    file_contexts = file.read_text()
    return tuple([int(depth.strip()) for depth in file_contexts.split("\n")])


if __name__ == "__main__":
    print(increases(read_depths("day_01.txt")))
    print(increases(window_sums(read_depths("day_01.txt"))))
