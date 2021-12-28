from advent_of_code import day_03


def test_rates():
    binary_numbers = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    assert day_03.gamma_rate(binary_numbers) == "10110"
    assert day_03.epsilon_rate(binary_numbers) == "01001"
    assert day_03.power_consumption(binary_numbers) == 198
    assert day_03.oxygen_generator_rate(binary_numbers) == "10111"
    assert day_03.co2_scrubber_rate(binary_numbers) == "01010"
    assert day_03.life_support_rating(binary_numbers) == 230
