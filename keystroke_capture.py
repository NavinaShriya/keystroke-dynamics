import tkinter as tk
import time


SENTENCE = "The quick brown fox jumps over the lazy dog"


class KeystrokeCapture:
    def __init__(self, root):
        self.root = root

        self.root.title("Keystroke Typing Test")
        self.root.geometry("700x400")

        self.start_time = None
        self.end_time = None

        self.key_press_times = {}
        self.hold_times = []
        self.flight_times = []

        self.previous_release_time = None

        self.create_interface()

    def create_interface(self):
        title = tk.Label(
            self.root,
            text="Keystroke Behavioral Authentication",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        instruction = tk.Label(
            self.root,
            text="Type the sentence below exactly:",
            font=("Arial", 12)
        )
        instruction.pack()

        sentence = tk.Label(
            self.root,
            text=SENTENCE,
            font=("Arial", 12),
            wraplength=650
        )
        sentence.pack(pady=15)

        self.text_box = tk.Entry(
            self.root,
            font=("Arial", 14),
            width=55
        )
        self.text_box.pack(pady=20)

        self.text_box.bind(
            "<KeyPress>",
            self.key_pressed
        )

        self.text_box.bind(
            "<KeyRelease>",
            self.key_released
        )

        self.text_box.focus()

        self.result_label = tk.Label(
            self.root,
            text="Start typing...",
            font=("Arial", 12)
        )
        self.result_label.pack(pady=20)

    def key_pressed(self, event):
        current_time = time.time()

        if self.start_time is None:
            self.start_time = current_time

        key = event.keysym

        self.key_press_times[key] = current_time

        if self.previous_release_time is not None:
            flight_time = current_time - self.previous_release_time
            self.flight_times.append(flight_time)

    def key_released(self, event):
        current_time = time.time()

        key = event.keysym

        if key in self.key_press_times:
            press_time = self.key_press_times[key]

            hold_time = current_time - press_time

            self.hold_times.append(hold_time)

            del self.key_press_times[key]

        self.previous_release_time = current_time

    def finish_test(self):
        if self.start_time is None:
            return

        self.end_time = time.time()

        typing_time = self.end_time - self.start_time

        typed_text = self.text_box.get()

        print("\nTyping Test Results")
        print("-------------------")

        print(f"Typed text: {typed_text}")
        print(f"Total typing time: {typing_time:.2f} seconds")

        if self.hold_times:
            average_hold = sum(self.hold_times) / len(self.hold_times)
            print(f"Average hold time: {average_hold:.4f} seconds")

        if self.flight_times:
            average_flight = sum(self.flight_times) / len(self.flight_times)
            print(f"Average flight time: {average_flight:.4f} seconds")

        print(f"Number of key events: {len(self.hold_times)}")

        if typed_text == SENTENCE:
            self.result_label.config(
                text="Typing test completed successfully."
            )
        else:
            self.result_label.config(
                text="Text does not match the required sentence."
            )


def main():
    root = tk.Tk()

    app = KeystrokeCapture(root)

    finish_button = tk.Button(
        root,
        text="Finish Test",
        command=app.finish_test,
        font=("Arial", 11)
    )

    finish_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
