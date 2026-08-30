import time


def calculate_hold_time(press_time, release_time):
    """Calculate how long a key was held."""

    return release_time - press_time


def calculate_flight_time(previous_release, current_press):
    """Calculate the time between two consecutive key presses."""

    return current_press - previous_release


def calculate_typing_speed(typing_time, character_count):
    """Calculate characters typed per second."""

    if typing_time <= 0:
        return 0

    return character_count / typing_time


def display_features(typing_time, character_count):
    """Display basic typing features."""

    typing_speed = calculate_typing_speed(
        typing_time,
        character_count
    )

    print("\nTyping Features")
    print("----------------")
    print(f"Total typing time: {typing_time:.2f} seconds")
    print(f"Characters typed: {character_count}")
    print(f"Typing speed: {typing_speed:.2f} characters/second")
