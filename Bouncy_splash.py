import os
import time
import sys

# ASCII art representations of "Earth"
earth_frames = [
    """
     __
   _/  \_
   \    /   
    \__/
    """,
    """
     --
   _/  \_
   \    /   
    \__/
    """
]

splash_frames = [
    """
    ~ ~ ~ 
    """,
    """
     ~ ~ 
    """
]

def clear_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_earth():
    bounce = 1  # Initial bounce direction
    height = 0  # Initial height
    splash = False  # Splash effect trigger

    try:
        while True:
            clear_screen()
            print('\n' * height + earth_frames[height % 2])
            if splash:
                print(splash_frames[height % 2])  # Display splash
                splash = False  # Reset splash trigger
            height += bounce

            # Reverse bounce direction at top and bottom
            if height == 5 or height == 0:
                bounce *= -1
                if height == 0:
                    splash = True  # Trigger splash effect

            time.sleep(0.1)
    except KeyboardInterrupt:
        # Exit on Ctrl+C
        pass

if __name__ == "__main__":
    animate_earth()
