from typing_test import run_typing_test
from authenticate import load_profile, calculate_profile, compare_typing


def main():
    print("   Keystroke Authentication System")
    # Load the saved typing profile
    profile = load_profile()

    if not profile:
        print("No typing profile found.")
        return

    # Calculate the user's normal typing behavior
    average, variation = calculate_profile(profile)

    print("\nSaved Typing Profile")
    print(f"Average typing time: {average:.2f} seconds")
    print(f"Standard deviation: {variation:.2f} seconds")

    # Collect a new typing attempt
    new_time = run_typing_test()

    if new_time is None:
        print("\nAuthentication stopped because the text did not match.")
        return

    # Compare the new attempt with the saved profile
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
