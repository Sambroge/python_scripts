import random
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

toggle_key = KeyCode(char='s')
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            interval = random.uniform(0.1, 0.17)
            time.sleep(interval)

def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking

def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

if __name__ == "__main__":
    main()
