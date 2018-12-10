from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
import random


false = False
true = True
r = (0,0,255)
w = (255,255,255)
b = (0,0,0)
k = (255,0,0)
g = (0,255,0)
wins = 0
losses = 0


maze1 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,r,b,b,b,r,],
    [r,b,r,r,b,r,b,r,],
    [r,b,b,b,b,r,g,r,],
    [r,b,r,k,b,r,r,r,],
    [r,r,r,r,b,r,b,r,],
    [r,k,b,b,b,b,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze2 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,r,k,r,k,b,r,],
    [r,b,r,b,r,r,b,r,],
    [r,b,r,b,b,b,b,r,],
    [r,b,b,b,r,k,b,r,],
    [r,b,r,b,r,r,b,r,],
    [r,k,r,b,r,g,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze3 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,b,b,b,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,b,b,b,b,b,g,r,],
    [r,r,r,r,r,r,r,r,],
    ]
mazes = [maze1,maze2,maze3]
maze = random.choice(mazes)
y=1
x=1
nX=1
nY=1
gameOver = False
win = False
while gameOver == False:
    maze[y][x] = w
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    sleep(0.0625
          )
    if 10 < pitch and pitch < 170:
        if maze[y][x-1]==b:
            maze[y][x]=b
            x -= 1
        if maze[y][x-1]==g:
            maze[y][x]=b
            x -= 1
            win = true
        if maze[y][x-1]==k:
            maze[y][x]=b
            x -= 1
            gameOver=true
    if 170 < pitch and pitch < 350:
        if maze[y][x+1]==b:
            maze[y][x]=b
            x += 1
        if maze[1][x+1]== g:
            maze[y][x]= b
            x += 1
            win = true
        if maze[y][x+1]== k:
            maze[y][x]=b
            x += 1
            gameOver=true
    if 10 < roll and roll < 170:
        if maze[y+1][x]==b:
            maze[y][x]=b
            y += 1
        if maze[y+1][x]==g:
            maze[y][x]=b
            y += 1
            win=true
        if maze[y+1][x]==k:
            maze[y][x]=b
            y += 1
            gameOver=true
    if 170 < roll and roll < 350:
        if maze[y-1][x]==b:
            maze[y][x]=b
            y -= 1
        if maze[y-1][x]==g:
            maze[y][x]=b
            y -= 1
            win = true
        if maze[y-1][x]==k:
            maze[y][x]=b
            y -= 1
            gameOver=true
    maze[y][x] = w
    if not win and not gameOver:
        sense.set_pixels(sum(maze,[]))
    if win:
        wins += 1
        maze[y][x] = g
        sense.show_letter(str(wins),w,g)
        sleep(1)
        maze = random.choice(mazes)
        win = false
        x=1
        y=1
        sense.set_pixels(sum(maze,[]))
        sleep(.5)
    if gameOver:
        losses += 1
        maze[y][x]=k
        sense.show_letter(str(losses),w,k)
        sleep(1)
        gameOver = false
        x=1
        y=1
        sense.set_pixels(sum(maze,[]))