import tkinter as tk
import time
SENTENCE = "The quick brown fox jumps over the lazy dog"
class KeystrokeCapture:
    def __init__(self, root):
        self.root = root

        self.root.title("Keystroke Typing Test")
        self.root.geometry("750x450")

        self.start_time = None
        self.end_time = None

        self.key_press_times = {}
        self.hold_times = []
        self.flight_times = []

        self.previous_release_time = None

        self.result = None

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
            text="Type the following sentence exactly:",
            font=("Arial", 12)
        )
        instruction.pack()

        sentence = tk.Label(
            self.root,
            text=SENTENCE,
            font=("Arial", 12)
        )
        sentence.pack(pady=15)

        self.text_box = tk.Entry(
            self.root,
            font=("Arial", 14),
            width=60
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
        self.result_label.pack(pady=10)

        finish_button = tk.Button(
            self.root,
            text="Finish Test",
            command=self.finish_test,
            font=("Arial", 11)
        )
        finish_button.pack(pady=10)

    def key_pressed(self, event):

        current_time = time.time()

        # Start timing when the first key is pressed
        if self.start_time is None:
            self.start_time = current_time

        key = event.keycode

        self.key_press_times[key] = current_time

        # Calculate flight time
        if self.previous_release_time is not None:

            flight_time = (
                current_time - self.previous_release_time
            )

            self.flight_times.append(flight_time)

    def key_released(self, event):

        current_time = time.time()

        key = event.keycode

        if key in self.key_press_times:

            press_time = self.key_press_times[key]

            hold_time = (
                current_time - press_time
            )

            self.hold_times.append(hold_time)

            del self.key_press_times[key]

        self.previous_release_time = current_time

    def finish_test(self):

        if self.start_time is None:

            self.result_label.config(
                text="Please type the sentence first."
            )

            return

        self.end_time = time.time()

        typing_time = (
            self.end_time - self.start_time
        )

        typed_text = self.text_box.get()

        # Calculate average hold time
        if self.hold_times:
            average_hold = (
                sum(self.hold_times)
                / len(self.hold_times)
            )
        else:
            average_hold = 0

        # Calculate average flight time
        if self.flight_times:
            average_flight = (
                sum(self.flight_times)
                / len(self.flight_times)
            )
        else:
            average_flight = 0

        if typed_text != SENTENCE:

            self.result_label.config(
                text="Text does not match. Please try again."
            )

            return

        # Store results for main.py
        self.result = {
            "typing_time": typing_time,
            "average_hold": average_hold,
            "average_flight": average_flight
        }

        self.result_label.config(
            text="Test completed successfully!"
        )

        # Close the window after a short delay
        self.root.after(
            1000,
            self.root.destroy
        )


def run_typing_test():

    root = tk.Tk()

    app = KeystrokeCapture(root)

    root.mainloop()

    return app.result


if __name__ == "__main__":

    result = run_typing_test()

    if result:

        print("\nTyping Test Results")
        print(
            f"Typing time: "
            f"{result['typing_time']:.2f} seconds"
        )

        print(
            f"Average hold time: "
            f"{result['average_hold']:.4f} seconds"
        )

        print(
            f"Average flight time: "
            f"{result['average_flight']:.4f} seconds"
        )
