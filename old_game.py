import curses

def main(stdscr):
    # Initialize the current screen coordinates (row, column)
    current_screen = [0, 0]

    # In this script, `current_screen` is a list of two numbers representing the row and column of the current screen in a 2D grid.
    # The right and left arrow keys change the column number, and the up and down arrow keys change the row number.
    # This allows you to navigate to four different screens ([0,0], [0,1], [1,0], [1,1]) using the arrow keys.
    # i.e. you can display different content based on the screen a user has navigated too

    while True:
        stdscr.clear()

        # Display different content based on the current screen
        if current_screen == [0, 0]:
            stdscr.addstr("This is screen 0,0. Press the right or down arrow key to navigate.")
        elif current_screen == [0, 1]:
            stdscr.addstr("This is screen 0,1. Press the left or down arrow key to navigate.")
        elif current_screen == [1, 0]:
            stdscr.addstr("This is screen 1,0. Press the right or up arrow key to navigate.")
        elif current_screen == [1, 1]:
            stdscr.addstr("This is screen 1,1. Press the left or up arrow key to navigate.")

        # Get the next key press
        key = stdscr.getch()

        # Change the current screen based on the key press
        if key == curses.KEY_RIGHT and current_screen[1] < 1:
            current_screen[1] += 1
        elif key == curses.KEY_LEFT and current_screen[1] > 0:
            current_screen[1] -= 1
        elif key == curses.KEY_DOWN and current_screen[0] < 1:
            current_screen[0] += 1
        elif key == curses.KEY_UP and current_screen[0] > 0:
            current_screen[0] -= 1

if __name__ == "__main__":
    curses.wrapper(main)
