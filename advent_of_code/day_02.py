from typing import Tuple
from pathlib import Path
from math import prod


Position = Tuple[int, int]
Command = Tuple[str, int]


def moves(position: Position, commands: Tuple[Command, ...]) -> Position:
    for command in commands:
        position = move(position, command)
    return position


def move(position: Position, command: Command) -> Position:
    horizontal, depth = position
    direction, units = command
    if direction == "forward":
        return horizontal + units, depth
    elif direction == "up":
        return horizontal, depth - units
    elif direction == "down":
        return horizontal, depth + units
    else:
        raise ValueError(f"Invalid command, received: {direction}")


def read_commands(file_name: str) -> Tuple[Command, ...]:
    file = Path(__file__).parent / "static_files" / file_name
    file_contents = file.read_text()
    commands = []
    for command in file_contents.split("\n"):
        direction, units = command.split(" ")
        commands.append((direction, int(units.strip())))
    return tuple(commands)


if __name__ == "__main__":
    print(prod(moves((0, 0), read_commands("day_02.txt"))))
