import csv
import statistics


PROFILE_FILE = "data/typing_profile.csv"


def load_profile():
    """Load saved typing times from the profile."""

    typing_times = []

    with open(PROFILE_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            typing_times.append(float(row["typing_time"]))

    return typing_times


def calculate_profile(typing_times):
    """Calculate the average and variation of the typing profile."""

    average = statistics.mean(typing_times)

    if len(typing_times) > 1:
        variation = statistics.stdev(typing_times)
    else:
        variation = 0

    return average, variation


def compare_typing(new_time, average, variation):
    """Compare a new typing time with the saved profile."""

    difference = abs(new_time - average)

    if variation == 0:
        return difference == 0

    threshold = variation * 2

    return difference <= threshold


def main():

    print("Keystroke Authentication Test")
    profile = load_profile()

    average, variation = calculate_profile(profile)

    print(f"Profile average: {average:.2f} seconds")
    print(f"Profile variation: {variation:.2f} seconds")

    try:
        new_time = float(
            input("\nEnter your new typing time: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    is_similar = compare_typing(
        new_time,
        average,
        variation
    )

    print("\nAuthentication Result")
    if is_similar:
        print("Typing behavior is similar to the profile.")
        print("Result: AUTHENTICATED")
    else:
        print("Typing behavior is noticeably different.")
        print("Result: NOT AUTHENTICATED")


if __name__ == "__main__":
    main()
