import os
import time
import sys

# ASCII art representations of "Earth"
earth_frames = [
    """
     ____
    /    \\
   |      |
    \\____/
    """,
    """
     ----
    /    \\
   |      |
    \\____/
    """
]

def clear_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_earth():
    bounce = 1  # Initial bounce direction
    height = 0  # Initial height

    try:
        while True:
            clear_screen()
            print('\n' * height + earth_frames[height % 2])
            height += bounce

            # Reverse bounce direction at top and bottom
            if height == 5 or height == 0:
                bounce *= -1

            time.sleep(0.1)
    except KeyboardInterrupt:
        # Exit on Ctrl+C
        pass

if __name__ == "__main__":
    animate_earth()
