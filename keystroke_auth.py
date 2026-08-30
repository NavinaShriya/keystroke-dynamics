import time
import statistics


def collect_typing_data():
    print("Keystroke Behavioral Authentication")
    print("-----------------------------------")
    print("Type the sentence below exactly as shown:")
    print()
    
    sentence = "The quick brown fox jumps over the lazy dog"
    print(sentence)
    print()

    input("Press Enter when you are ready...")
    
    print("\nType the sentence and press Enter:")
    
    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    total_time = end_time - start_time

    print("\nResults")
    print("-------")
    print(f"Typed text: {typed_text}")
    print(f"Typing time: {total_time:.2f} seconds")

    return typed_text, total_time


def analyze_typing(typed_text, typing_time):
    expected_text = "The quick brown fox jumps over the lazy dog"

    if typed_text != expected_text:
        print("\nText does not match.")
        return

    print("\nText matched successfully.")

    # Simple baseline for demonstration
    baseline_time = 5.0
    difference = abs(typing_time - baseline_time)

    print(f"Baseline typing time: {baseline_time:.2f} seconds")
    print(f"Difference: {difference:.2f} seconds")

    if difference <= 2:
        print("Result: Typing behavior is similar to the baseline.")
    else:
        print("Result: Typing behavior is noticeably different.")


if __name__ == "__main__":
    typed_text, typing_time = collect_typing_data()
    analyze_typing(typed_text, typing_time)
