import time
import statistics


SENTENCE = "The quick brown fox jumps over the lazy dog"
NUMBER_OF_SAMPLES = 5


def collect_sample(sample_number):
    print(f"\nSample {sample_number}/{NUMBER_OF_SAMPLES}")
    print(SENTENCE)

    input("Press Enter when you are ready...")

    print("Start typing:")

    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    typing_time = end_time - start_time

    if typed_text != SENTENCE:
        print("Text does not match.")
        return None

    print(f"Typing time: {typing_time:.2f} seconds")

    return typing_time


def collect_typing_profile():
    print("Keystroke Behavioral Authentication")
    print("Let's create your typing profile.")
    print(f"We will collect {NUMBER_OF_SAMPLES} samples.")

    samples = []

    for sample_number in range(1, NUMBER_OF_SAMPLES + 1):
        typing_time = collect_sample(sample_number)

        if typing_time is not None:
            samples.append(typing_time)

    return samples


def analyze_profile(samples):

    if not samples:
        print("\nNo valid samples were collected.")
        return

    average = statistics.mean(samples)
    minimum = min(samples)
    maximum = max(samples)

    print("\nYour Typing Profile")
    print(f"Valid samples: {len(samples)}")
    print(f"Average typing time: {average:.2f} seconds")
    print(f"Minimum typing time: {minimum:.2f} seconds")
    print(f"Maximum typing time: {maximum:.2f} seconds")

    if len(samples) > 1:
        variation = statistics.stdev(samples)
        print(f"Standard deviation: {variation:.2f} seconds")


def main():

    samples = collect_typing_profile()

    analyze_profile(samples)


if __name__ == "__main__":
    main()
