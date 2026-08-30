import time


SENTENCE = "The quick brown fox jumps over the lazy dog"


def run_typing_test():
    print("Keystroke Typing Test")
    print("\nType the following sentence:")
    print(SENTENCE)

    input("\nPress Enter when you are ready...")

    print("\nStart typing:")

    start_time = time.time()

    typed_text = input()

    end_time = time.time()

    typing_time = end_time - start_time

    print(f"\nTyping time: {typing_time:.2f} seconds")

    if typed_text == SENTENCE:
        print("Text matched successfully.")
        return typing_time

    print("Text does not match.")
    return None


if __name__ == "__main__":
    run_typing_test()
