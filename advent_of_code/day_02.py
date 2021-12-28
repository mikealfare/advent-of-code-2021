from typing import Tuple
from pathlib import Path
from math import prod


Position = int
Depth = int
Aim = int
Command = Tuple[str, int]


def moves(position: Position, depth: Depth, commands: Tuple[Command, ...]) -> Tuple[Position, Depth]:
    for command in commands:
        position, depth = move(position, depth, command)
    return position, depth


def moves_with_aim(
        position: Position,
        depth: Depth,
        aim: Aim,
        commands: Tuple[Command, ...]
) -> Tuple[Position, Depth, Aim]:
    for command in commands:
        position, depth, aim = move_with_aim(position, depth, aim, command)
    return position, depth, aim


def move(position: Position, depth: Depth, command: Command) -> Tuple[Position, Depth]:
    direction, units = command
    if direction == "forward":
        return position + units, depth
    elif direction == "up":
        return position, depth - units
    elif direction == "down":
        return position, depth + units
    else:
        raise ValueError(f"Invalid command, received: {direction}")



def move_with_aim(position: Position, depth: Depth, aim: Aim, command: Command) -> Tuple[Position, Depth, Aim]:
    direction, units = command
    if direction == "forward":
        return position + units, depth + aim * units, aim
    elif direction == "up":
        return position, depth, aim - units
    elif direction == "down":
        return position, depth, aim + units
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
    print(prod(moves(0, 0, read_commands("day_02.txt"))))
    position, depth, _ = moves_with_aim(0, 0, 0, read_commands("day_02.txt"))
    print(position*depth)
