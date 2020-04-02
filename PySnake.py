import random
import curses
from curses import textpad

# initialising the screen
s = curses.initscr()
curses.curs_set(0)
# height and the width of screen
sh,sw=s.getmaxyx()
# opening new window
w = curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)
# initial positions of the snake(left center)
snk_x = sw/4
snk_y = sh/2
# snake body head and two lefts
snake = [[snk_y, snk_x],[snk_y,snk_x-1],[snk_y, snk_x-2]]

# initial position of food(center of screen)
food = [sh/2, sw/2]
# add food to the screen , ACS_P1 -> our food is Pi symbol
w.addch(food[0], food[1], curses.ACS_PI)

# the snake moves initially right and the next direction is specified by key
key = curses.KEY_RIGHT

while True:
    next_key=w.getch()
    key = key if next_key == -1 else next_key
# check if the person has lost the game four corners or eating itself
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]
# direct the snake as per input arrow keys
    if key == curses.KEY_DOWN:
        new_head[0] +=1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[0] -=1
    if key == curses.KEY_RIGHT:
        new_head[0] +=1

    snake.insert(0, new_head)
# random positioning the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)

            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0],tail[1],' ')

    w.addch(food[0], food[1], curses.ACS_PI)












