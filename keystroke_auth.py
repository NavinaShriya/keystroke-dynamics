import time
import csv
import statistics

DATA_FILE = "data/sample_typing_data.csv"
def load_baseline():
    """Load previous typing times and calculate the average."""
    typing_times = []
    try:
        with open(DATA_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                typing_times.append(float(row["typing_time"]))

    except FileNotFoundError:
        print("No typing data found.")
        return 5.0

    if not typing_times:
        return 5.0

    return statistics.mean(typing_times)


def collect_typing_data():
    print("Keystroke Behavioral Authentication")
    sentence = "The quick brown fox jumps over the lazy dog"
    print("\nType the following sentence:")
    print(sentence)

    input("\nPress Enter when you are ready...")

    print("\nStart typing:")

    start_time = time.time()

    typed_text = input()

    end_time = time.time()

    typing_time = end_time - start_time

    return typed_text, typing_time


def analyze_typing(typed_text, typing_time, baseline_time):

    expected_text = "The quick brown fox jumps over the lazy dog"

    print("\nResults")
    print(f"Typing time: {typing_time:.2f} seconds")
    print(f"Baseline time: {baseline_time:.2f} seconds")

    if typed_text != expected_text:
        print("Text does not match.")
        return

    difference = abs(typing_time - baseline_time)

    print(f"Difference from baseline: {difference:.2f} seconds")

    if difference <= 2:
        print("\nResult: Typing behavior is similar to the baseline.")
    else:
        print("\nResult: Typing behavior is noticeably different.")


def main():

    baseline_time = load_baseline()

    typed_text, typing_time = collect_typing_data()

    analyze_typing(
        typed_text,
        typing_time,
        baseline_time
    )


if __name__ == "__main__":
    main()
