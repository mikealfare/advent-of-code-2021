from typing import List
from pathlib import Path
from collections import Counter


BinaryNumber = str
Bit = str


def power_consumption(binary_numbers: List[BinaryNumber]) -> int:
    gamma = gamma_rate(binary_numbers)
    epsilon = epsilon_rate(binary_numbers)
    return int(gamma, 2) * int(epsilon, 2)


def life_support_rating(binary_numbers: List[BinaryNumber]) -> int:
    oxygen = oxygen_generator_rate(binary_numbers)
    co2 = co2_scrubber_rate(binary_numbers)
    return int(oxygen, 2) * int(co2, 2)


def gamma_rate(binary_numbers: List[BinaryNumber]) -> BinaryNumber:
    gamma = ""
    for position in range(len(binary_numbers[0])):
        bit = most_common_bit_in_position(binary_numbers, position)
        gamma += bit
    return gamma


def epsilon_rate(binary_numbers: List[BinaryNumber]) -> BinaryNumber:
    epsilon = ""
    for position in range(len(binary_numbers[0])):
        bit = most_common_bit_in_position(binary_numbers, position)
        bit = {"0": "1", "1": "0"}[bit]
        epsilon += bit
    return epsilon


def oxygen_generator_rate(binary_numbers: List[BinaryNumber], position: int = 0) -> BinaryNumber:
    bit = most_common_bit_in_position(binary_numbers, position)
    filtered_binary_numbers = [number for number in binary_numbers if number[position] == bit]
    if len(filtered_binary_numbers) == 1:
        return filtered_binary_numbers[0]
    else:
        return oxygen_generator_rate(filtered_binary_numbers, position + 1)


def co2_scrubber_rate(binary_numbers: List[BinaryNumber], position: int = 0) -> BinaryNumber:
    bit = most_common_bit_in_position(binary_numbers, position)
    bit = {"0": "1", "1": "0"}[bit]
    filtered_binary_numbers = [number for number in binary_numbers if number[position] == bit]
    if len(filtered_binary_numbers) == 1:
        return filtered_binary_numbers[0]
    else:
        return co2_scrubber_rate(filtered_binary_numbers, position + 1)


def most_common_bit_in_position(binary_numbers: List[BinaryNumber], position: int) -> Bit:
    bits = Counter([number[position] for number in binary_numbers])
    if bits["1"] >= bits["0"]:
        return "1"
    else:
        return "0"


def read_numbers(file_name: str) -> List[BinaryNumber]:
    file = Path(__file__).parent / "static_files" / file_name
    file_contents = file.read_text()
    return file_contents.split("\n")


if __name__ == "__main__":
    print(power_consumption(read_numbers("day_03.txt")))
    print(life_support_rating(read_numbers("day_03.txt")))
