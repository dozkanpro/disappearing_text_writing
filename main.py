import tkinter as tk
import threading
import time

window = tk.Tk()
window.title("Auto Clear Typing App")

text = tk.Text(window, wrap=tk.WORD)
text.pack()

typing_thread = None
last_typing_time = time.time()
timeout = 5


def start_typing_thread():
    global typing_thread
    typing_thread = threading.Thread(target=monitor_typing)
    typing_thread.daemon = True
    typing_thread.start()


def monitor_typing():
    while True:
        current_time = time.time()
        if current_time - last_typing_time >= timeout:
            clear_text()
        time.sleep(1)  # Check every 1 second


def clear_text():
    text.delete('1.0', tk.END)


def on_keypress(event):
    global last_typing_time
    last_typing_time = time.time()


def run():
    text.bind('<Key>', on_keypress)
    start_typing_thread()
    window.mainloop()


if __name__ == "__main__":
    run()
