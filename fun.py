import curses
import time

# Dragon frames for animation
dragon_frames = [
    r"""
       \                    / \  //\
        \    |\___/|      /   \//  \\
             /0  0  \__  /    //  | \ \    
            /     /  \/_/    //   |  \  \  
            \_^_|\_/   \/_   //    |   \   \ 
            /_/  |  \    \/_ //     |    \    \
           //    |   \     \//      |     \     \
          //     |    \     /       |      \     _\
         /       |     \  /        |       \  / / 
        /        |      \/         |        \/_/ 
    """,
    r"""
       \                    / \  //\
        \    |\___/|      /   \//  \\
             /0  0  \__  /    //  | \ \    
            /     /  \/_/    //   |  \  \  
            \_^_|\_/   \/_   //    |   \   \ 
            /_/  |  \    \/_ //     |    \    \
           //    |   \     \//      |     \     \
          //     |    \     /       |      \     _\
         /       |     \  /        |       \  / / 
        /        |      \/         |        \/_/ 
    """,
]

def animate_dragon(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)

    frame_index = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        frame = dragon_frames[frame_index]

        for i, line in enumerate(frame.splitlines()):
            stdscr.addstr(i + height // 2 - len(frame.splitlines()) // 2, width // 2 - len(line) // 2, line)

        stdscr.refresh()
        frame_index = (frame_index + 1) % len(dragon_frames)

        key = stdscr.getch()
        if key == ord('q'):
            break

        time.sleep(0.1)

curses.wrapper(animate_dragon)