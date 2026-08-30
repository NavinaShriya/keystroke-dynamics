from authenticate import (
    load_profile,
    calculate_profile,
    compare_typing
)

from keystroke_capture import run_typing_test


def main():
    print("   Keystroke Authentication System")

    # Load saved typing profile
    profile = load_profile()

    if not profile:
        print("No typing profile found.")
        return

    # Calculate baseline statistics
    average, variation = calculate_profile(profile)

    print("\nSaved Typing Profile")
    print(f"Average typing time: {average:.2f} seconds")
    print(f"Standard deviation: {variation:.2f} seconds")

    print("\nOpening keystroke typing test...")

    # Run the keystroke capture window
    result = run_typing_test()

    if result is None:
        print("\nTyping test was not completed.")
        return

    new_time = result["typing_time"]

    print("\nNew Typing Attempt")
    print(f"Typing time: {new_time:.2f} seconds")
    print(f"Average hold time: {result['average_hold']:.4f} seconds")
    print(f"Average flight time: {result['average_flight']:.4f} seconds")

    # Compare with saved profile
    authenticated = compare_typing(
        new_time,
        average,
        variation
    )
    print("       Authentication Result")


    if authenticated:
        print("Typing behavior matches the profile.")
        print("Result: AUTHENTICATED")
    else:
        print("Typing behavior is different from the profile.")
        print("Result: NOT AUTHENTICATED")


if __name__ == "__main__":
    main()
